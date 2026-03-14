#!/usr/bin/env python3
"""
Check available Gemini models and their details
"""

import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

def check_available_models():
    """Check what Gemini models are available"""
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        print("❌ GEMINI_API_KEY not found in .env")
        return
    
    print(f"✅ API Key found: {api_key[:20]}...")
    
    try:
        genai.configure(api_key=api_key)
        
        # List all available models
        print("\n📋 Available Models:")
        models = genai.list_models()
        
        text_models = []
        for model in models:
            if 'generateContent' in model.supported_generation_methods:
                text_models.append(model.name)
                print(f"  ✅ {model.name}")
        
        if not text_models:
            print("  ❌ No text generation models found")
        else:
            print(f"\n🎯 Found {len(text_models)} text models")
            
            # Test each model
            print("\n🧪 Testing Models:")
            for model_name in text_models:
                try:
                    model = genai.GenerativeModel(model_name)
                    response = model.generate_content("Say 'Hello'")
                    print(f"  ✅ {model_name}: {response.text.strip()}")
                except Exception as e:
                    print(f"  ❌ {model_name}: {str(e)[:50]}...")
                    
    except Exception as e:
        print(f"❌ Error: {e}")

def test_current_service():
    """Test the current GeminiService configuration"""
    print("\n🔧 Testing Current Service:")
    
    import sys
    sys.path.append('/Users/rakshanjustin/individual-trait-analysis-career-path-system')
    
    from project_backend.engine.gemini_service import GeminiService
    
    service = GeminiService()
    print(f"Service Available: {service.is_available()}")
    
    if service.model:
        print(f"Current Model: {service.model.model_name}")
        
        # Test with a simple prompt
        try:
            response = service.model.generate_content("What career advice would you give?")
            print(f"Test Response: {response.text[:100]}...")
        except Exception as e:
            print(f"Test Error: {e}")

if __name__ == "__main__":
    print("🔍 Checking Gemini Models...")
    check_available_models()
    test_current_service()
