from project_backend.ai.ai_config import client, MODEL_NAME


def generate_ai_analysis(role, traits):

    trait_text = "\n".join(
        [f"{trait}: {score:.2f}" for trait, score in traits.items()]
    )

    prompt = f"""
You are an expert AI career advisor.

A user completed a psychometric assessment.

Recommended Career Role:
{role}

User Cognitive Traits:
{trait_text}

Provide a clean analysis.

Format the response exactly like this:

Pros:
- point
- point

Cons:
- point
- point

Growth Suggestions:
- point
- point

Keep the explanation concise and practical.
"""

    try:

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )

        return response.choices[0].message.content

    except Exception as e:

        print("⚠️ GROQ AI ERROR:", e)

        # Fallback response so system never crashes
        return f"""
Pros:
- Strong alignment with analytical thinking
- Demonstrates potential for the {role} career path

Cons:
- Some cognitive traits may require further development

Growth Suggestions:
- Work on structured problem solving
- Build small projects related to {role}
- Strengthen technical foundations gradually
"""