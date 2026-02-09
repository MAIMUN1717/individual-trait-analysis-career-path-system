from roles.role_schema import RoleRequirement


ROLES = {

    "Backend Developer": RoleRequirement(
        trait_weights={
            "logical_reasoning": 0.18,
            "analytical_reasoning": 0.17,
            "abstract_reasoning": 0.10,
            "problem_framing": 0.10,
            "conscientiousness": 0.12,
            "investigative_interest": 0.08,
            "adaptability": 0.07,
            "growth_mindset": 0.08,
            "ambiguity_tolerance": 0.10
        },
        min_thresholds={
            "logical_reasoning": 0.5,
            "analytical_reasoning": 0.5
        },
        eligibility={
            "degree": 0.4
        }
    ),

    "Data Scientist": RoleRequirement(
        trait_weights={
            "analytical_reasoning": 0.20,
            "logical_reasoning": 0.15,
            "abstract_reasoning": 0.15,
            "analytical_evaluation": 0.12,
            "investigative_interest": 0.15,
            "growth_mindset": 0.08,
            "adaptability": 0.08,
            "ambiguity_tolerance": 0.07
        },
        min_thresholds={
            "analytical_reasoning": 0.6,
            "investigative_interest": 0.6
        },
        eligibility={
            "degree": 0.5,
            "gpa": 0.5
        }
    ),
}
