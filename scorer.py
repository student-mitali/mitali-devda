def calculate_score(data):
    score = 0

    if data["has_readme"]:
        score += 15
    if data["has_tests"]:
        score += 15

    if data["commits"] >= 10:
        score += 15
    elif data["commits"] >= 5:
        score += 10

    if len(data["languages"]) >= 1:
        score += 15

    if len(data["folders"]) >= 3:
        score += 15

    if data["stars"] > 0:
        score += 10

    return min(score, 100)
