from collections import defaultdict
from typing import List, Dict


class TraitAggregator:
    """
    Aggregates scores per trait and normalizes them.
    """

    def __init__(self):
        self.trait_scores = defaultdict(list)

    def add(self, trait: str, score: float):
        self.trait_scores[trait].append(score)

    def aggregate(self) -> Dict[str, float]:
        final_scores = {}

        for trait, scores in self.trait_scores.items():
            if not scores:
                final_scores[trait] = 0.0
            else:
                final_scores[trait] = sum(scores) / len(scores)

        return final_scores
