import json
import random
from project_backend.ai.ai_config import groq_client  # adjust if your file name differs
import re
from .domain_models import DOMAIN_ARCHETYPES


from groq import Groq

# 🔐 Replace with your actual API key
client = Groq(api_key="YOUR_GROQ_API_KEY")


def call_ai_model(prompt):
    try:
        completion = groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "Return ONLY valid JSON. No explanations."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        response = completion.choices[0].message.content

        # 🔥 Clean markdown
        cleaned = re.sub(r"```json|```", "", response).strip()

        return cleaned

    except Exception as e:
        print("❌ GROQ ERROR:", str(e))
        return "[]"
# -----------------------------
# GLOBAL CACHE
# -----------------------------
question_cache = {}
MAX_CACHE = 20


# -----------------------------
# REMOVE DUPLICATES
# -----------------------------
def remove_duplicates(new_questions, existing_questions):
    existing_set = set(q["question"].lower() for q in existing_questions)

    filtered = []
    for q in new_questions:
        if q["question"].lower() not in existing_set:
            filtered.append(q)

    return filtered

# -----------------------------
# BALANCE TRAITS
# -----------------------------
def balance_traits(questions):
    trait_groups = {}

    for q in questions:
        trait = q.get("trait", "general")
        trait_groups.setdefault(trait, []).append(q)

    balanced = []
    while any(trait_groups.values()):
        for trait in list(trait_groups.keys()):
            if trait_groups[trait]:
                balanced.append(trait_groups[trait].pop(0))

    return balanced[:20]


# -----------------------------
# DETERMINE DIFFICULTY
# -----------------------------
def get_difficulty(user_answers):
    if not user_answers:
        return "easy"

    score = sum(user_answers.values()) / len(user_answers)

    if score > 0.7:
        return "hard"
    elif score > 0.4:
        return "medium"
    else:
        return "easy"


# -----------------------------
# GENERATE QUESTIONS
# -----------------------------
def generate_questions(domain, user_answers=None):
    existing_questions = question_cache.get(domain, [])

    existing_texts = [q["question"] for q in existing_questions]

    difficulty = get_difficulty(user_answers or {})

    # ✅ GET TRAITS FROM DOMAIN_ARCHETYPES
    traits = DOMAIN_ARCHETYPES.get(domain, {}).get("traits", [])

    prompt = f"""
Generate 20 NEW psychometric questions for the domain: {domain}

DIFFICULTY LEVEL: {difficulty}

STRICT RULES:
- Do NOT repeat or rephrase these questions:
{existing_texts}

- You MUST ONLY use these traits:
{traits}

- Each trait should have around 2 questions
- DO NOT invent new traits
- Questions must be:
  - Unique
  - Short and clear
  - Trait-based
  - Suitable for Likert scale

Return ONLY JSON:
[
  {{
    "trait": "one_of_the_given_traits",
    "question": "..."
  }}
]
"""

    ai_response = call_ai_model(prompt)

    try:
        new_questions = json.loads(ai_response)

    except:
        new_questions = []

    # ✅ Remove duplicates
    filtered_questions = remove_duplicates(new_questions, existing_questions)

    # ✅ Balance traits
    balanced_questions = balance_traits(filtered_questions)

    # ✅ Update cache
    updated_cache = existing_questions + balanced_questions
    question_cache[domain] = updated_cache[-MAX_CACHE:]

    # ✅ Fallback
    if not balanced_questions:
        return existing_questions[:20]

    return balanced_questions[:20]

