from project_backend.ai.ai_config import client, MODEL_NAME


def generate_skill_plan(traits, role):

    prompt = f"""
User cognitive traits:
{traits}

Target role:
{role}

Create a structured learning roadmap.

Include:
1. Fundamental skills
2. Intermediate skills
3. Advanced skills
4. Recommended projects
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content