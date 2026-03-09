from dataclasses import dataclass
from typing import Dict, Optional


@dataclass(frozen=True)
class RoleRequirement:

    # domain the role belongs to
    domain: str

    # role trait weights
    trait_weights: Dict[str, float]

    # minimum thresholds
    min_thresholds: Dict[str, float]

    # optional eligibility filters
    eligibility: Optional[Dict[str, float]] = None