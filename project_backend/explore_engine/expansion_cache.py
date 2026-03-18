import json
import os

CACHE_FILE = "explore_expansion_cache.json"


def load_cache():
    if not os.path.exists(CACHE_FILE):
        return {}
    with open(CACHE_FILE, "r") as f:
        return json.load(f)


def save_cache(cache):
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=2)


def get_cached(domain, concept):
    cache = load_cache()
    return cache.get(domain, {}).get(concept)


def set_cache(domain, concept, data):
    cache = load_cache()

    if domain not in cache:
        cache[domain] = {}

    cache[domain][concept] = data
    save_cache(cache)