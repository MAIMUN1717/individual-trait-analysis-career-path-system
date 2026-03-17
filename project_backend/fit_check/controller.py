from .domain_models import DOMAIN_TRAITS
from .question_generator import generate_question
from .cache_manager import get_cached_questions, store_questions
from .trait_engine import ANSWER_MAP, normalize
from .fit_calculator import calculate_fit_score
from .mentor_feedback import generate_feedback


# 🔧 CONFIG
QUESTIONS_PER_TRAIT = 4   # 5 traits × 4 = 20 questions


# 🧠 GENERATE QUESTIONS (WITH CACHE)
def generate_domain_questions(domain, refresh=False):

    # 🔍 Check cache
    if not refresh:
        cached = get_cached_questions(domain)
        if cached:
            print("✅ Using cached questions")
            return cached

    print("⚡ Generating new questions from AI...")

    traits = DOMAIN_TRAITS.get(domain)

    if not traits:
        return []

    questions = []

    # 🔁 Generate multiple questions per trait
    for trait in traits:

        for i in range(QUESTIONS_PER_TRAIT):

            q = generate_question(domain, trait)

            questions.append({
                "trait": trait,
                "question": q
            })

    # 💾 Save to cache
    store_questions(domain, questions)

    return questions


# 🧠 EVALUATE ANSWERS
def evaluate_answers(domain, answers):

    traits = DOMAIN_TRAITS.get(domain)

    if not traits:
        return {
            "fit_score": 0,
            "trait_scores": {},
            "feedback": "Invalid domain"
        }

    trait_scores = {}
    trait_counts = {}

    # 🔁 Process answers
    for ans in answers:

        trait = ans.get("trait")
        answer = ans.get("answer")

        if trait not in traits:
            continue

        score = normalize(ANSWER_MAP.get(answer, 0))

        if trait not in trait_scores:
            trait_scores[trait] = 0
            trait_counts[trait] = 0

        trait_scores[trait] += score
        trait_counts[trait] += 1

    # 🧮 Average scores per trait
    for trait in traits:

        if trait in trait_scores:
            trait_scores[trait] = round(
                trait_scores[trait] / trait_counts[trait], 2
            )
        else:
            trait_scores[trait] = 0

    # 📊 Debug logs
    print("📊 Trait Scores:", trait_scores)

    # 🎯 Calculate fit score
    fit_score = calculate_fit_score(domain, trait_scores)

    print("🎯 Fit Score:", fit_score)

    # 🤖 Generate AI feedback
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