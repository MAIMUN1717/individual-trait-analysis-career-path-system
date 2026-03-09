from project_backend.roles.role_schema import RoleRequirement


ROLES = {

    "Backend Developer": RoleRequirement(
        domain="software_engineering",
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
        domain="ai_data",
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

    "Full Stack Developer": RoleRequirement(
        domain="software_engineering",
        trait_weights={
            "logical_reasoning": 0.18,
            "analytical_reasoning": 0.15,
            "abstract_reasoning": 0.10,
            "problem_framing": 0.10,
            "adaptability": 0.12,
            "planning_and_monitoring": 0.12,
            "growth_mindset": 0.08,
            "ambiguity_tolerance": 0.08,
            "conscientiousness": 0.07
        },
        min_thresholds={
            "logical_reasoning": 0.5
        },
        eligibility={
            "degree": 0.4
        }
    ),

    "Frontend Developer": RoleRequirement(
        domain="software_engineering",
        trait_weights={
            "abstract_reasoning": 0.18,
            "openness": 0.15,
            "artistic_interest": 0.20,
            "adaptability": 0.10,
            "logical_reasoning": 0.10,
            "growth_mindset": 0.08,
            "planning_and_monitoring": 0.09,
            "conscientiousness": 0.10
        },
        min_thresholds={
            "abstract_reasoning": 0.5
        },
        eligibility={
            "degree": 0.3
        }
    ),

    "ML Engineer": RoleRequirement(
        domain="ai_data",
        trait_weights={
            "analytical_reasoning": 0.22,
            "logical_reasoning": 0.18,
            "abstract_reasoning": 0.15,
            "analytical_evaluation": 0.12,
            "investigative_interest": 0.12,
            "planning_and_monitoring": 0.10,
            "growth_mindset": 0.06,
            "ambiguity_tolerance": 0.05
        },
        min_thresholds={
            "analytical_reasoning": 0.6
        },
        eligibility={
            "degree": 0.5
        }
    ),

    "DevOps Engineer": RoleRequirement(
        domain="cloud_devops",
        trait_weights={
            "logical_reasoning": 0.15,
            "planning_and_monitoring": 0.20,
            "conscientiousness": 0.18,
            "adaptability": 0.15,
            "risk_tolerance": 0.10,
            "growth_mindset": 0.07,
            "problem_framing": 0.10,
            "ambiguity_tolerance": 0.05
        },
        min_thresholds={
            "planning_and_monitoring": 0.5
        },
        eligibility={
            "degree": 0.4
        }
    ),

    "Cloud Engineer": RoleRequirement(
        domain="cloud_devops",
        trait_weights={
            "logical_reasoning": 0.18,
            "analytical_reasoning": 0.15,
            "planning_and_monitoring": 0.18,
            "adaptability": 0.15,
            "conscientiousness": 0.12,
            "risk_tolerance": 0.07,
            "growth_mindset": 0.08,
            "ambiguity_tolerance": 0.07
        },
        min_thresholds={
            "logical_reasoning": 0.5
        },
        eligibility={
            "degree": 0.4
        }
    ),

    "Cybersecurity Analyst": RoleRequirement(
        domain="cybersecurity",
        trait_weights={
            "analytical_reasoning": 0.20,
            "logical_reasoning": 0.18,
            "problem_framing": 0.15,
            "risk_tolerance": 0.12,
            "investigative_interest": 0.15,
            "conscientiousness": 0.10,
            "ambiguity_tolerance": 0.10
        },
        min_thresholds={
            "analytical_reasoning": 0.6
        },
        eligibility={
            "degree": 0.4
        }
    ),

    "Product Manager": RoleRequirement(
        domain="product_design",
        trait_weights={
            "problem_framing": 0.18,
            "tradeoff_analysis": 0.18,
            "social_interest": 0.15,
            "adaptability": 0.15,
            "openness": 0.10,
            "planning_and_monitoring": 0.10,
            "growth_mindset": 0.07,
            "ambiguity_tolerance": 0.07
        },
        min_thresholds={
            "problem_framing": 0.5
        },
        eligibility={
            "degree": 0.4
        }
    ),

    "UI/UX Designer": RoleRequirement(
        domain="product_design",
        trait_weights={
            "artistic_interest": 0.22,
            "openness": 0.18,
            "abstract_reasoning": 0.12,
            "social_interest": 0.12,
            "adaptability": 0.10,
            "planning_and_monitoring": 0.08,
            "growth_mindset": 0.08,
            "conscientiousness": 0.10
        },
        min_thresholds={
            "artistic_interest": 0.6
        },
        eligibility={
            "degree": 0.3
        }
    ),
}