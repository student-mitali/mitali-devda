from analyzer import fetch_repo_data
from scorer import calculate_score
from roadmap import generate_roadmap

repo_url = input("Enter GitHub repository URL: ")

data = fetch_repo_data(repo_url)
score = calculate_score(data)
roadmap = generate_roadmap(data)

level = "Beginner"
if score >= 70:
    level = "Advanced"
elif score >= 40:
    level = "Intermediate"

print("\n===== GitGrade Evaluation =====")
print(f"Score: {score}/100")
print(f"Level: {level}")

print("\nSummary:")
print(
    "The repository shows good structure and language usage, "
    "but improvements are needed in documentation, testing, "
    "and development consistency."
)

print("\nPersonalized Roadmap:")
for step in roadmap:
    print("-", step)
