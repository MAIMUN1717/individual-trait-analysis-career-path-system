#!/usr/bin/env python3
"""
Test that the UI API endpoint now returns Gemini-powered explanations
"""

import sys
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add project path to Python path
sys.path.append('/Users/rakshanjustin/individual-trait-analysis-career-path-system')

from project_backend.engine.recommender import recommend_with_explanations

def test_ui_integration():
    """Test the full pipeline that UI will receive"""
    print("🧪 Testing UI Integration with Gemini...")
    
    # Sample user traits (normalized 0-1)
    trait_vector = {
        "analytical_reasoning": 0.4,
        "logical_reasoning": 0.5,
        "problem_framing": 0.3,
        "risk_tolerance": 0.4,
        "conscientiousness": 0.8,
        "openness": 0.6,
        "adaptability": 0.7
    }
    
    standard_error = {
        "analytical_reasoning": 0.1,
        "logical_reasoning": 0.1,
        "problem_framing": 0.15,
        "risk_tolerance": 0.12,
        "conscientiousness": 0.08,
        "openness": 0.09,
        "adaptability": 0.07
    }
    
    # Call the same function that UI API endpoint uses
    result = recommend_with_explanations(trait_vector, standard_error)
    
    print(f"📊 Detected Domain: {result['domain']}")
    print(f"🎯 Number of Recommendations: {len(result['recommendations'])}")
    
    print("\n🌟 Top Recommendation Analysis:")
    top_rec = result['recommendations'][0]
    print(f"Role: {top_rec['role']}")
    print(f"Fit Score: {top_rec['fit_score']}")
    
    explanation = top_rec['explanation']
    print(f"\n💬 Strengths ({len(explanation['strengths'])}):")
    for strength in explanation['strengths']:
        print(f"  • {strength}")
    
    print(f"\n⚠️  Gaps ({len(explanation['gaps'])}):")
    for gap in explanation['gaps']:
        print(f"  • {gap[:100]}...")
    
    print(f"\n🚀 Growth Suggestions ({len(explanation['growth_suggestions'])}):")
    for suggestion in explanation['growth_suggestions']:
        print(f"  • {suggestion[:100]}...")
    
    # Check if Gemini responses are present
    gap_text = ' '.join(explanation['gaps'])
    growth_text = ' '.join(explanation['growth_suggestions'])
    
    gemini_indicators = ['Resources:', 'Timeline:', 'Strategy:', 'Projects:', 'Enroll in', 'Kaggle', 'Coursera']
    has_gemini_content = any(indicator in gap_text or indicator in growth_text for indicator in gemini_indicators)
    
    print(f"\n✅ Gemini Content Detected: {has_gemini_content}")
    
    if has_gemini_content:
        print("🎉 UI will now receive personalized Gemini-powered advice!")
    else:
        print("⚠️  Still using template-based responses")
    
    return has_gemini_content

if __name__ == "__main__":
    success = test_ui_integration()
    print(f"\n{'='*50}")
    if success:
        print("🎉 SUCCESS: Gemini integration working for UI!")
    else:
        print("❌ ISSUE: Gemini responses not reaching UI")
