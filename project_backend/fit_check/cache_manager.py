import json
import os

CACHE_FILE = "fit_check_questions_cache.json"


def load_cache():
    if not os.path.exists(CACHE_FILE):
        return {}

    with open(CACHE_FILE, "r") as f:
        return json.load(f)


def save_cache(cache):
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=4)


def get_cached_questions(domain):
    cache = load_cache()
    return cache.get(domain)


def store_questions(domain, questions):
    cache = load_cache()
    cache[domain] = questions
    save_cache(cache)
    