import random
from collections import defaultdict
from core.questions_schema import Priority


class QuestionSampler:
    def __init__(self, questions):
        self.questions = questions

    def sample_per_trait(self, per_trait=3):
        """
        Samples questions per trait with priority awareness.
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

            # Priority-aware selection
            for pool in (high, medium, low):
                random.shuffle(pool)
                for q in pool:
                    if len(selected) < per_trait:
                        selected.append(q)

            sampled_questions.extend(selected)

        random.shuffle(sampled_questions)
        return sampled_questions
