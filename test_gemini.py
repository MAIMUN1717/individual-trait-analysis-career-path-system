#!/usr/bin/env python3
"""
Test script for Gemini API integration
Tests both successful API calls and fallback mechanisms
"""

import sys
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Add project path to Python path
sys.path.append('/Users/rakshanjustin/individual-trait-analysis-career-path-system')

from project_backend.engine.gemini_service import GeminiService
from project_backend.engine.explainer import RoleExplainer

def test_gemini_service():
    """Test Gemini service with sample data"""
    print("=== Testing Gemini Service ===")
    
    # Sample test data
    user_traits = {
        "analytical_reasoning": 0.4,
        "logical_reasoning": 0.5,
        "problem_framing": 0.3,
        "risk_tolerance": 0.4
    }
    
    role_traits = {
        "analytical_reasoning": 0.8,
        "logical_reasoning": 0.7,
        "problem_framing": 0.6,
        "risk_tolerance": 0.8
    }
    
    gaps = {
        "analytical_reasoning": 0.4,
        "logical_reasoning": 0.2,
        "problem_framing": 0.3,
        "risk_tolerance": 0.4
    }
    
    role_name = "Cybersecurity Analyst"
    
    # Test Gemini service
    gemini_service = GeminiService()
    
    print(f"Gemini Service Available: {gemini_service.is_available()}")
    
    # Test gap analysis
    result = gemini_service.analyze_trait_gaps(
        user_traits=user_traits,
        role_traits=role_traits,
        gaps=gaps,
        role_name=role_name
    )
    
    print(f"\nGap Analysis Result:\n{result}")
    print("=" * 50)

def test_explainer_integration():
    """Test explainer integration with Gemini"""
    print("\n=== Testing Explainer Integration ===")
    
    # Sample role result
    role_result = {
        "matched_traits": ["conscientiousness"],
        "weak_traits": ["analytical_reasoning", "logical_reasoning"]
    }
    
    user_traits = {
        "analytical_reasoning": 0.4,
        "logical_reasoning": 0.5,
        "conscientiousness": 0.8,
        "problem_framing": 0.3
    }
    
    role_traits = {
        "analytical_reasoning": 0.8,
        "logical_reasoning": 0.7,
        "conscientiousness": 0.6,
        "problem_framing": 0.6
    }
    
    role_name = "Data Scientist"
    
    # Test new Gemini-powered explainer
    explanations = RoleExplainer.explain_with_gemini(
        role_result=role_result,
        user_traits=user_traits,
        role_traits=role_traits,
        role_name=role_name
    )
    
    print("Strengths:")
    for strength in explanations["strengths"]:
        print(f"- {strength}")
    
    print("\nGaps (Gemini-powered):")
    for gap in explanations["gaps"]:
        print(f"- {gap}")
    
    print("\nGrowth Suggestions (Gemini-powered):")
    for suggestion in explanations["growth_suggestions"]:
        print(f"- {suggestion}")
    
    print("=" * 50)

def test_original_vs_gemini():
    """Compare original template vs Gemini-powered explanations"""
    print("\n=== Comparing Original vs Gemini ===")
    
    role_result = {
        "matched_traits": ["conscientiousness"],
        "weak_traits": ["analytical_reasoning", "logical_reasoning"]
    }
    
    user_traits = {
        "analytical_reasoning": 0.4,
        "logical_reasoning": 0.5,
        "conscientiousness": 0.8
    }
    
    role_traits = {
        "analytical_reasoning": 0.8,
        "logical_reasoning": 0.7,
        "conscientiousness": 0.6
    }
    
    # Original template-based
    original = RoleExplainer.explain(role_result, user_traits)
    
    # Gemini-powered
    gemini_powered = RoleExplainer.explain_with_gemini(
        role_result, user_traits, role_traits, "Data Scientist"
    )
    
    print("ORIGINAL GAPS:")
    for gap in original["gaps"]:
        print(f"- {gap}")
    
    print("\nGEMINI GAPS:")
    for gap in gemini_powered["gaps"]:
        print(f"- {gap}")
    
    print("=" * 50)

if __name__ == "__main__":
    print("Testing Gemini API Integration...")
    print("Note: Make sure GEMINI_API_KEY is set in .env file")
    
    test_gemini_service()
    test_explainer_integration()
    test_original_vs_gemini()
    
    print("\n✅ Gemini integration test completed!")
    print("If Gemini API key is not configured, fallback will be used.")
