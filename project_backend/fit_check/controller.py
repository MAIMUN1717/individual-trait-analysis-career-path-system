from .domain_models import DOMAIN_ARCHETYPES
from .question_generator import generate_questions
from .cache_manager import get_cached_questions, store_questions
from .trait_engine import ANSWER_MAP, normalize
from .fit_calculator import calculate_fit_score
from .mentor_feedback import generate_feedback


QUESTIONS_PER_TRAIT = 4


def generate_domain_questions(domain, refresh=False):
    if not refresh:
        cached = get_cached_questions(domain)
        if cached:
            print("✅ Using cached questions")
            return cached

    print("⚡ Generating new questions from AI...")

    traits = DOMAIN_ARCHETYPES.get(domain, {}).get("traits", [])

    if not traits:
        return []

    # 🔥 NEW: Use AI generator instead of old generate_question
    generated = generate_questions(domain)

    questions = []

    for i, q in enumerate(generated):
        questions.append({
            "id": f"{domain}-{i}",
            "trait": q.get("trait", "general"),
            "text": q.get("question", "")
        })

    # Store in cache
    store_questions(domain, questions)

    return questions



def evaluate_answers(domain, answers):
    print("🚨 FINAL ANSWERS RECEIVED:", answers)
    traits = DOMAIN_ARCHETYPES.get(domain, {}).get("traits", [])

    if not traits:
        return {
            "fit_score": 0,
            "trait_scores": {},
            "feedback": "Invalid domain"
        }

    # 🔥 Normalize domain traits once
    normalized_traits = [t.lower().replace(" ", "_") for t in traits]

    trait_scores = {}
    trait_counts = {}

    print("📥 RAW ANSWERS:", answers)
    print("📌 DOMAIN TRAITS:", normalized_traits)

    for ans in answers:
        raw_trait = ans.get("trait", "")
        raw_answer = ans.get("answer", "")

        # 🔥 Normalize BOTH
        trait = raw_trait.lower().replace(" ", "_")
        formatted_answer = raw_answer.lower().replace(" ", "_")

        print("➡️ Processing:", raw_trait, "|", raw_answer, "→", trait, "|", formatted_answer)

        if trait not in normalized_traits:
            print("⚠️ Skipped trait:", trait)
            continue

        score_raw = ANSWER_MAP.get(formatted_answer, 0)
        score = normalize(score_raw)

        print("DEBUG SCORE →", formatted_answer, "|", score_raw, "|", score)

        if trait not in trait_scores:
            trait_scores[trait] = 0
            trait_counts[trait] = 0

        trait_scores[trait] += score
        trait_counts[trait] += 1

    # 🔥 Final averaging
    for trait in normalized_traits:
        if trait in trait_scores and trait_counts[trait] > 0:
            trait_scores[trait] = round(
                trait_scores[trait] / trait_counts[trait], 2
            )
        else:
            trait_scores[trait] = 0

    print("📊 Trait Scores:", trait_scores)

    fit_score = calculate_fit_score(domain, trait_scores)
    print("🎯 Fit Score:", fit_score)

    try:
        feedback = generate_feedback(domain, trait_scores, fit_score)
    except Exception as e:
        print("❌ FEEDBACK ERROR:", str(e))
        feedback = "Feedback generation failed. Showing basic analysis."

    return {
        "fit_score": fit_score,
        "trait_scores": trait_scores,
        "feedback": feedback
    }