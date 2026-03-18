DOMAINS = {

# =========================
# 1. DATA SCIENCE
# =========================
"data-science": {
    "name": "Data Science",

    "overview": "Data Science focuses on extracting insights from data using statistics, machine learning, and visualization techniques.",

    "why_this_domain": "Organizations rely on data to make decisions. Data Science enables prediction, optimization, and automation across industries.",

    "core_concepts": [
        {"title": "Statistics", "content": "Probability, distributions, hypothesis testing, and inference form the backbone."},
        {"title": "Machine Learning", "content": "Algorithms that learn patterns from data."},
        {"title": "Data Cleaning", "content": "Handling missing data and preprocessing."}
    ],

    "tools": ["Python", "Pandas", "NumPy", "Scikit-learn", "Matplotlib"],

    "roadmap": {
        "beginner": ["Python basics", "Statistics fundamentals", "Pandas"],
        "intermediate": ["ML algorithms", "Feature engineering", "Model evaluation"],
        "advanced": ["Deep learning", "MLOps", "Big Data"]
    },

    "projects": [{
        "name": "House Price Prediction",
        "description": "Predict house prices using regression.",
        "steps": ["Collect dataset", "Clean data", "Train model", "Evaluate"],
        "tech_stack": ["Python", "Scikit-learn"]
    }],

    "interview_prep": [
        "Bias vs Variance",
        "Overfitting",
        "Supervised vs Unsupervised"
    ],

    "resources": ["Kaggle", "Coursera ML", "Fast.ai"]
},

# =========================
# 2. AI / ML
# =========================
"ai-ml": {
    "name": "AI / Machine Learning",

    "overview": "AI/ML focuses on building intelligent systems that learn from data and improve over time.",

    "why_this_domain": "AI powers automation, recommendation systems, chatbots, and autonomous systems.",

    "core_concepts": [
        {"title": "Supervised Learning", "content": "Learning from labeled data."},
        {"title": "Neural Networks", "content": "Deep learning architectures inspired by the brain."},
        {"title": "Model Optimization", "content": "Improving model performance."}
    ],

    "tools": ["TensorFlow", "PyTorch", "Scikit-learn"],

    "roadmap": {
        "beginner": ["Python", "Linear Algebra", "Basic ML"],
        "intermediate": ["Deep Learning", "CNN, RNN"],
        "advanced": ["Transformers", "LLMs", "MLOps"]
    },

    "projects": [{
        "name": "Image Classifier",
        "description": "Classify images using CNN.",
        "steps": ["Prepare dataset", "Train CNN", "Evaluate"],
        "tech_stack": ["Python", "TensorFlow"]
    }],

    "interview_prep": ["What is gradient descent?", "Explain CNN"],

    "resources": ["DeepLearning.ai", "PapersWithCode"]
},

# =========================
# 3. BACKEND ENGINEERING
# =========================
"backend-engineering": {
    "name": "Backend Engineering",

    "overview": "Backend development focuses on server-side logic, databases, and APIs.",

    "why_this_domain": "Backend systems power applications, ensuring scalability, security, and performance.",

    "core_concepts": [
        {"title": "APIs", "content": "Communication between frontend and backend."},
        {"title": "Databases", "content": "Storage systems like SQL and NoSQL."},
        {"title": "Authentication", "content": "User identity and security."}
    ],

    "tools": ["Node.js", "Django", "Flask", "PostgreSQL"],

    "roadmap": {
        "beginner": ["HTTP basics", "Python/Node", "REST APIs"],
        "intermediate": ["Databases", "Authentication", "Caching"],
        "advanced": ["System Design", "Scaling", "Microservices"]
    },

    "projects": [{
        "name": "REST API System",
        "description": "Build scalable APIs.",
        "steps": ["Design API", "Implement routes", "Connect DB"],
        "tech_stack": ["FastAPI", "PostgreSQL"]
    }],

    "interview_prep": ["REST vs GraphQL", "What is caching?"],

    "resources": ["Backend Roadmap", "System Design Primer"]
},

# =========================
# 4. FRONTEND ENGINEERING
# =========================
"frontend-engineering": {
    "name": "Frontend Engineering",

    "overview": "Frontend focuses on building user interfaces and experiences.",

    "why_this_domain": "UI determines user experience and engagement.",

    "core_concepts": [
        {"title": "HTML/CSS", "content": "Structure and styling."},
        {"title": "JavaScript", "content": "Dynamic behavior."},
        {"title": "React", "content": "Component-based UI."}
    ],

    "tools": ["React", "Tailwind CSS", "JavaScript"],

    "roadmap": {
        "beginner": ["HTML", "CSS", "JS"],
        "intermediate": ["React", "State Management"],
        "advanced": ["Performance Optimization", "SSR"]
    },

    "projects": [{
        "name": "Portfolio Website",
        "description": "Personal website.",
        "steps": ["Design UI", "Build components", "Deploy"],
        "tech_stack": ["React", "CSS"]
    }],

    "interview_prep": ["Virtual DOM", "Closures"],

    "resources": ["Frontend Masters", "MDN"]
},

# =========================
# 5. CLOUD COMPUTING
# =========================
"cloud-computing": {
    "name": "Cloud Computing",

    "overview": "Cloud computing provides scalable infrastructure and services over the internet.",

    "why_this_domain": "Modern apps rely on cloud for scalability and reliability.",

    "core_concepts": [
        {"title": "IaaS/PaaS/SaaS", "content": "Cloud service models."},
        {"title": "Virtualization", "content": "Resource abstraction."},
        {"title": "Networking", "content": "Cloud architecture."}
    ],

    "tools": ["AWS", "Azure", "GCP"],

    "roadmap": {
        "beginner": ["Cloud basics", "AWS basics"],
        "intermediate": ["Deploy apps", "Networking"],
        "advanced": ["Architecture", "Security"]
    },

    "projects": [{
        "name": "Deploy Web App",
        "description": "Deploy using AWS.",
        "steps": ["Setup EC2", "Deploy app"],
        "tech_stack": ["AWS"]
    }],

    "interview_prep": ["What is EC2?"],

    "resources": ["AWS Docs"]
},

# =========================
# 6. DEVOPS
# =========================
"devops": {
    "name": "DevOps",

    "overview": "DevOps combines development and operations for faster delivery.",

    "why_this_domain": "Ensures smooth deployment and scaling.",

    "core_concepts": [
        {"title": "CI/CD", "content": "Automated pipelines."},
        {"title": "Containers", "content": "Dockerization."},
        {"title": "Monitoring", "content": "System tracking."}
    ],

    "tools": ["Docker", "Kubernetes", "Jenkins"],

    "roadmap": {
        "beginner": ["Linux", "Git"],
        "intermediate": ["Docker", "CI/CD"],
        "advanced": ["Kubernetes"]
    },

    "projects": [{
        "name": "CI/CD Pipeline",
        "description": "Automate deployment.",
        "steps": ["Setup pipeline"],
        "tech_stack": ["Jenkins"]
    }],

    "interview_prep": ["What is CI/CD?"],

    "resources": ["DevOps Roadmap"]
},

# =========================
# 7. CYBERSECURITY
# =========================
"cybersecurity": {
    "name": "Cybersecurity",

    "overview": "Protecting systems and networks from attacks.",

    "why_this_domain": "Security is critical for all systems.",

    "core_concepts": [
        {"title": "Encryption", "content": "Secure data."},
        {"title": "Network Security", "content": "Protect networks."},
        {"title": "Ethical Hacking", "content": "Test vulnerabilities."}
    ],

    "tools": ["Wireshark", "Metasploit"],

    "roadmap": {
        "beginner": ["Networking basics"],
        "intermediate": ["Security tools"],
        "advanced": ["Pen testing"]
    },

    "projects": [{
        "name": "Vulnerability Scanner",
        "description": "Scan system vulnerabilities.",
        "steps": ["Scan network"],
        "tech_stack": ["Python"]
    }],

    "interview_prep": ["What is firewall?"],

    "resources": ["OWASP"]
},

# =========================
# 8. MOBILE DEVELOPMENT
# =========================
"mobile-development": {
    "name": "Mobile Development",

    "overview": "Building applications for mobile devices.",

    "why_this_domain": "Mobile apps dominate user interaction.",

    "core_concepts": [
        {"title": "Android/iOS", "content": "Platforms."},
        {"title": "UI Design", "content": "User interfaces."},
        {"title": "APIs", "content": "Backend communication."}
    ],

    "tools": ["Flutter", "React Native"],

    "roadmap": {
        "beginner": ["Basics", "UI"],
        "intermediate": ["API integration"],
        "advanced": ["Performance"]
    },

    "projects": [{
        "name": "Todo App",
        "description": "Mobile task manager.",
        "steps": ["Design UI", "Build app"],
        "tech_stack": ["Flutter"]
    }],

    "interview_prep": ["What is Activity?"],

    "resources": ["Flutter Docs"]
},

# =========================
# 9. PRODUCT MANAGEMENT
# =========================
"product-management": {
    "name": "Product Management",

    "overview": "Managing product lifecycle and strategy.",

    "why_this_domain": "Bridges business, tech, and users.",

    "core_concepts": [
        {"title": "User Research", "content": "Understanding users."},
        {"title": "Roadmapping", "content": "Planning features."},
        {"title": "Metrics", "content": "KPIs and growth."}
    ],

    "tools": ["Jira", "Notion"],

    "roadmap": {
        "beginner": ["Basics"],
        "intermediate": ["Execution"],
        "advanced": ["Strategy"]
    },

    "projects": [{
        "name": "Product Case Study",
        "description": "Analyze product.",
        "steps": ["Research", "Analyze"],
        "tech_stack": ["Docs"]
    }],

    "interview_prep": ["What is MVP?"],

    "resources": ["PM Guides"]
},

# =========================
# 10. UI/UX DESIGN
# =========================
"ui-ux": {
    "name": "UI/UX Design",

    "overview": "Designing user interfaces and experiences.",

    "why_this_domain": "Good design improves usability.",

    "core_concepts": [
        {"title": "Wireframing", "content": "Basic layouts."},
        {"title": "User Research", "content": "Understand users."},
        {"title": "Design Systems", "content": "Consistency."}
    ],

    "tools": ["Figma", "Adobe XD"],

    "roadmap": {
        "beginner": ["Design basics"],
        "intermediate": ["Prototyping"],
        "advanced": ["UX research"]
    },

    "projects": [{
        "name": "App Redesign",
        "description": "Improve UX.",
        "steps": ["Research", "Design"],
        "tech_stack": ["Figma"]
    }],

    "interview_prep": ["What is UX?"],

    "resources": ["Design Blogs"]
}

}