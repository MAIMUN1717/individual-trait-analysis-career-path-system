from project_backend.ai.ai_config import groq_client


def generate_question(domain, trait):

    prompt = f"""
You are a psychometric assessment designer.

Generate ONE SHORT statement to evaluate a person's thinking style.

Domain: {domain}
Trait: {trait}

IMPORTANT:
- Keep it under 15 words
- Must be a statement (not a question)
- Must work with:
  Strongly Agree / Agree / Neutral / Disagree / Strongly Disagree
- DO NOT create long explanations

Example:
"I enjoy analyzing complex problems deeply."

Return ONLY the statement.
"""

    try:
        response = groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # ✅ safer model
            messages=[{"role": "user", "content": prompt}],
            temperature=0.6,
        )

        print("✅ GROQ RESPONSE:", response)

        return response.choices[0].message.content.strip()

    except Exception as e:
        print("❌ GROQ ERROR:", str(e))
        return f"Fallback question for {trait}"