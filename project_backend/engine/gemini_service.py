import os
import requests
import hashlib
import json
from typing import Dict, List, Optional
from project_backend.engine.templates import TRAIT_DESCRIPTIONS


class GeminiService:
    
    def __init__(self):
        self.ollama_url = "http://localhost:11434/api/generate"
        self.model_name = "gemma:2b"
        self.cache = {}  # Simple in-memory cache
        self._test_connection()
    
    def _test_connection(self):
        """Test if Ollama is running and model is available"""
        try:
            response = requests.post(
                self.ollama_url,
                json={"model": self.model_name, "prompt": "test", "stream": False},
                timeout=3  # Reduced timeout
            )
            if response.status_code == 200:
                print(f"✅ Using local model: {self.model_name}")
                self.available = True
            else:
                print(f"❌ Ollama model {self.model_name} not available")
                self.available = False
        except Exception as e:
            print(f"❌ Failed to connect to Ollama: {e}")
            self.available = False
    
    def _get_cache_key(self, user_traits: Dict, role_traits: Dict, gaps: Dict, role_name: str) -> str:
        """Generate cache key based on input parameters"""
        # Round values to reduce cache misses
        rounded_data = {
            "user": {k: round(v, 2) for k, v in user_traits.items()},
            "role": {k: round(v, 2) for k, v in role_traits.items()},
            "gaps": {k: round(v, 2) for k, v in gaps.items()},
            "name": role_name
        }
        return hashlib.md5(json.dumps(rounded_data, sort_keys=True).encode()).hexdigest()
    
    def is_available(self) -> bool:
        """Check if Ollama service is available"""
        return self.available
    
    def analyze_trait_gaps(self, user_traits: Dict, role_traits: Dict, gaps: Dict, role_name: str) -> str:
        """
        Generate personalized gap analysis using local Gemma model with caching
        
        Args:
            user_traits: User's current trait scores
            role_traits: Role's required trait weights
            gaps: Calculated gaps between user and role
            role_name: Name of the target role
            
        Returns:
            Personalized gap analysis text or fallback message
        """
        # Check cache first
        cache_key = self._get_cache_key(user_traits, role_traits, gaps, role_name)
        if cache_key in self.cache:
            print("🚀 Using cached response")
            return self.cache[cache_key]
        
        if not self.is_available():
            return self._get_fallback_message(gaps)
        
        try:
            prompt = self._build_gap_analysis_prompt(user_traits, role_traits, gaps, role_name)
            
            response = requests.post(
                self.ollama_url,
                json={
                    "model": self.model_name,
                    "prompt": prompt,
                    "stream": False,
                    "options": {
                        "temperature": 0.3,  # Reduced for more consistent responses
                        "max_tokens": 300,   # Reduced for faster generation
                        "top_p": 0.9,
                        "num_predict": 300
                    }
                },
                timeout=15  # Reduced timeout
            )
            
            if response.status_code == 200:
                result = response.json()
                if "response" in result:
                    response_text = result["response"].strip()
                    # Cache the response
                    self.cache[cache_key] = response_text
                    print("💾 Cached new response")
                    return response_text
            
            return self._get_fallback_message(gaps)
                
        except Exception as e:
            print(f"Ollama API error: {e}")
            return self._get_fallback_message(gaps)
    
    def _build_gap_analysis_prompt(self, user_traits: Dict, role_traits: Dict, gaps: Dict, role_name: str) -> str:
        """Build optimized prompt for faster Gemma response"""
        
        # Only include traits with significant gaps
        significant_gaps = {k: v for k, v in gaps.items() if v > 0.1}
        
        if not significant_gaps:
            return "No significant gaps found. Provide brief encouragement."
        
        # Build shorter prompt
        prompt_parts = [f"Career: {role_name}\n\nGaps to address:"]
        
        for trait, gap_value in significant_gaps.items():
            desc = TRAIT_DESCRIPTIONS.get(trait, trait)
            prompt_parts.append(f"- {desc} (gap: {gap_value:.2f})")
        
        prompt_parts.append("\nProvide 2-3 specific, actionable suggestions. Be concise. Use bullet points.")
        
        return "\n".join(prompt_parts)
    
    def _get_fallback_message(self, gaps: Dict) -> str:
        """Fallback message when Gemini is unavailable"""
        if not gaps:
            return "No significant gaps identified. Continue developing your current skills."
        
        gap_traits = []
        for trait, gap_value in gaps.items():
            if gap_value > 0:
                desc = TRAIT_DESCRIPTIONS.get(trait, trait)
                gap_traits.append(desc)
        
        return f"""
Focus on developing: {', '.join(gap_traits)}.

Recommended actions:
• Take online courses in these areas
• Practice with real-world projects
• Seek mentorship from professionals
• Set specific learning goals with timelines

Consistent practice and targeted learning will help bridge these gaps.
"""
