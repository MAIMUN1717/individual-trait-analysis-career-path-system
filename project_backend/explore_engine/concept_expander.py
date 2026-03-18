from project_backend.explore_engine.expansion_cache import get_cached, set_cache
from project_backend.ai.ai_config import groq_client as client

def expand_concept(domain, concept):
    cached = get_cached(domain, concept)
    if cached:
        return cached

    prompt = f"""
    You are an expert mentor.

    Explain the concept "{concept}" in the domain "{domain}".

    Provide:
    - Simple explanation
    - Real-world example
    - Key insights
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )

        result = response.choices[0].message.content

        data = {
            "concept": concept,
            "explanation": result,
            "domain": domain
        }

        set_cache(domain, concept, data)

        return data

    except Exception as e:
        return {
            "concept": concept,
            "explanation": f"Fallback: Unable to generate explanation now. Error: {str(e)}"
        }