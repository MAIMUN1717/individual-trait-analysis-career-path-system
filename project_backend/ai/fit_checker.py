from project_backend.ai.ai_config import client, MODEL_NAME


def evaluate_role_fit(role, traits, answers):

    prompt = f"""
You are evaluating a student's suitability for a technology role.

Role: {role}

User cognitive traits:
{traits}

User answers to role-fit questions:
{answers}

Provide:

Fit Score (0–100)
Strengths
Weaknesses
Improvement suggestions
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content