import requests

GITHUB_API = "https://api.github.com/repos"

def fetch_repo_data(repo_url):
    owner, repo = repo_url.replace("https://github.com/", "").split("/")
    base_url = f"{GITHUB_API}/{owner}/{repo}"

    repo_info = requests.get(base_url).json()
    commits = requests.get(f"{base_url}/commits").json()
    languages = requests.get(f"{base_url}/languages").json()
    contents = requests.get(f"{base_url}/contents").json()

    files = [item["name"] for item in contents if item["type"] == "file"]
    folders = [item["name"] for item in contents if item["type"] == "dir"]

    return {
        "stars": repo_info.get("stargazers_count", 0),
        "languages": languages,
        "commits": len(commits),
        "files": files,
        "folders": folders,
        "has_readme": any("readme" in f.lower() for f in files),
        "has_tests": any("test" in f.lower() for f in folders),
    }
