def normalize_score(value: float, min_value: float, max_value: float) -> float:
    if max_value == min_value:
        return 0.0
    return max(0.0, min(1.0, (value - min_value) / (max_value - min_value)))


def likert_to_score(option_index: int, scale_size: int = 4) -> float:
    return normalize_score(option_index, 1, scale_size)


def correctness_score(is_correct: bool) -> float:
    return 1.0 if is_correct else 0.0
