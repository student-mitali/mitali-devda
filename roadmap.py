def generate_roadmap(data):
    roadmap = []

    if not data["has_readme"]:
        roadmap.append("Add a detailed README with project overview and setup steps")

    if not data["has_tests"]:
        roadmap.append("Write unit tests to improve reliability and maintainability")

    if data["commits"] < 5:
        roadmap.append("Commit code more frequently with meaningful messages")

    if len(data["folders"]) < 3:
        roadmap.append("Improve folder structure for better modularity")

    roadmap.append("Follow Git best practices using branches and pull requests")
    roadmap.append("Add CI/CD pipeline using GitHub Actions")

    return roadmap
