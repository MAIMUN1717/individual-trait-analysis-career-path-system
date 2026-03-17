from project_backend.ai.ai_config import groq_client


def generate_feedback(domain, trait_scores, fit_score):

    prompt = f"""
You are a career mentor.

Domain: {domain}

Trait Scores:
{trait_scores}

Fit Score: {fit_score}

Give:

1. Strengths
2. Weaknesses
3. Advice
4. Beginner Projects

Keep it simple and structured.
"""

    try:
        response = groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print("❌ GROQ FEEDBACK ERROR:", str(e))

        return f"""
Strengths:
You show potential in {domain}

Weakness:
Some traits need improvement

Advice:
Practice consistently and build projects

Projects:
Start with beginner-level projects
"""