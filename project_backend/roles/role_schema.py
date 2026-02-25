from dataclasses import dataclass
from typing import Dict, Optional


@dataclass(frozen=True)
class RoleRequirement:
    trait_weights: Dict[str, float]   # sum <= 1.0
    min_thresholds: Dict[str, float]  # hard cutoffs
    eligibility: Optional[Dict[str, float]] = None
