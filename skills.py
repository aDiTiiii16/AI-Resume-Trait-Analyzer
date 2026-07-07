ROLE_SKILLS = {
    "Software Developer": [
        "java", "sql", "git", "github", "spring", "spring boot",
        "html", "css", "javascript", "mysql", "docker"
    ],

    "Full Stack Developer": [
        "java", "spring boot", "react", "html", "css",
        "javascript", "git", "github", "docker", "mysql"
    ],

    "Data Analyst": [
        "python", "sql", "excel", "power bi",
        "pandas", "numpy", "statistics"
    ],

    "Machine Learning Engineer": [
        "python", "machine learning", "deep learning",
        "tensorflow", "scikit-learn",
        "numpy", "pandas", "sql"
    ]
}


def extract_skills(text, role):

    text = text.lower()

    detected = []

    required_skills = ROLE_SKILLS[role]

    for skill in required_skills:
        if skill in text:
            detected.append(skill)

    return detected


def calculate_score(skills, role):

    total = len(ROLE_SKILLS[role])

    score = (len(skills) / total) * 100

    return round(score)


def get_missing_skills(skills, role):

    missing = []

    for skill in ROLE_SKILLS[role]:
        if skill not in skills:
            missing.append(skill)

    return missing


def generate_suggestions(score, missing):

    suggestions = []

    if score < 40:
        suggestions.append("Add more technical projects.")
        suggestions.append("Include relevant certifications.")
        suggestions.append("Improve the skills section.")

    if "git" in missing:
        suggestions.append("Mention Git or GitHub experience.")

    if "docker" in missing:
        suggestions.append("Learning Docker will improve your backend profile.")

    if "aws" in missing:
        suggestions.append("Consider learning AWS Cloud.")

    if "sql" in missing:
        suggestions.append("Add SQL or database projects.")

    if "power bi" in missing:
        suggestions.append("Include Power BI projects for analyst roles.")

    if "tensorflow" in missing:
        suggestions.append("Mention TensorFlow if applying for ML roles.")

    return suggestions