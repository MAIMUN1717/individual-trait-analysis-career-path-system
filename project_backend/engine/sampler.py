import random
from collections import defaultdict
from project_backend.core.questions_schema import Priority

class QuestionSampler:
    def __init__(self, questions):
        self.questions = questions

    def sample_per_trait(self, per_trait=3):
        """
        Original uniform sampling method (kept for backward compatibility)
        """
        trait_groups = defaultdict(list)

        for q in self.questions:
            trait_groups[q.trait].append(q)

        sampled_questions = []

        for trait, qs in trait_groups.items():
            high = [q for q in qs if q.priority == Priority.HIGH]
            medium = [q for q in qs if q.priority == Priority.MEDIUM]
            low = [q for q in qs if q.priority == Priority.LOW]

            selected = []

            for pool in (high, medium, low):
                random.shuffle(pool)
                for q in pool:
                    if len(selected) < per_trait:
                        selected.append(q)

            sampled_questions.extend(selected)

        random.shuffle(sampled_questions)
        return sampled_questions

    def sample_with_distribution(self, distribution: dict):
        """
        Custom distribution sampling.
        Example:
        {
            "cognitive_ability": 4,
            "critical_thinking": 4,
            ...
        }
        """
        trait_groups = defaultdict(list)

        for q in self.questions:
            trait_groups[q.trait].append(q)

        sampled_questions = []

        for trait, required_count in distribution.items():
            qs = trait_groups.get(trait, [])

            if not qs:
                continue

            required_count = min(required_count, len(qs))

            high = [q for q in qs if q.priority == Priority.HIGH]
            medium = [q for q in qs if q.priority == Priority.MEDIUM]
            low = [q for q in qs if q.priority == Priority.LOW]

            selected = []

            for pool in (high, medium, low):
                random.shuffle(pool)
                for q in pool:
                    if len(selected) < required_count:
                        selected.append(q)

            sampled_questions.extend(selected)

        random.shuffle(sampled_questions)
        return sampled_questions