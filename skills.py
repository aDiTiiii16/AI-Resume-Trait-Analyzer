TECHNICAL_SKILLS = [
    "python",
    "java",
    "c",
    "c++",
    "sql",
    "mysql",
    "postgresql",
    "spring",
    "spring boot",
    "react",
    "html",
    "css",
    "javascript",
    "git",
    "github",
    "docker",
    "aws",
    "machine learning",
    "deep learning",
    "tensorflow",
    "pandas",
    "numpy",
    "scikit-learn",
    "excel",
    "power bi"
]
def extract_skills(text):
    text = text.lower()

    detected_skills = []

    for skill in TECHNICAL_SKILLS:
        if skill in text:
            detected_skills.append(skill)

    return detected_skills


def calculate_score(skills):

    total_skills = len(TECHNICAL_SKILLS)

    detected = len(skills)

    score = (detected / total_skills) * 100

    return round(score)

