from project_backend.ai.ai_config import client, MODEL_NAME


def career_chat(message, traits=None, domain=None, roles=None):

    prompt = f"""
You are an AI career advisor helping a student choose technology careers.

User cognitive trait profile:
{traits}

Detected career domain:
{domain}

Recommended roles from assessment:
{roles}

User question:
{message}

Give personalized guidance based on the user's cognitive strengths and weaknesses.

Explain:
- relevant skills
- learning suggestions
- possible career directions
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )

    return response.choices[0].message.content