import os
import requests
import pytoml
import json
from pathlib import Path


def load_toml(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return pytoml.load(f)


def save_toml(file_path, data):
    with open(file_path, "w", encoding="utf-8") as f:
        pytoml.dump(data, f)


def check_github_archive_status(repo_full_name, token):
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
    }
    url = f"https://api.github.com/repos/{repo_full_name}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json().get("archived", False)
    return None


def get_crates_io_repository(crate_name):
    headers = {"User-Agent": "arewegameyet (gamedev-wg@rust-lang.org)"}
    url = f"https://crates.io/api/v1/crates/{crate_name}"
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes

        data = response.json()
        if not data or "crate" not in data:
            print(f"Warning: Invalid response from crates.io for {crate_name}")
            return None

        repo_url = data["crate"].get("repository")
        if not repo_url:
            print(f"Warning: No repository URL found for crate {crate_name}")
            return None

        if "github.com" not in repo_url:
            print(f"Info: Non-GitHub repository for crate {crate_name}: {repo_url}")
            return None

        parts = repo_url.split("github.com/")
        if len(parts) != 2:
            print(f"Warning: Malformed GitHub URL for crate {crate_name}: {repo_url}")
            return None

        return parts[1].rstrip("/")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching crate {crate_name} from crates.io: {e}")
        return None
    except (KeyError, ValueError, AttributeError) as e:
        print(f"Error parsing response for crate {crate_name}: {e}")
        return None


def extract_github_repo(item):
    if not item or not isinstance(item, dict):
        print(f"Warning: Invalid item format: {item}")
        return None

    if item.get("source") == "github":
        return item.get("name")
    elif item.get("source") == "crates":
        name = item.get("name")
        if not name:
            print(f"Warning: No name found for crates.io item: {item}")
            return None
        return get_crates_io_repository(name)

    repo_url = item.get("repository_url", "")
    if not repo_url:
        return None

    if "github.com" in repo_url:
        parts = repo_url.split("github.com/")
        if len(parts) == 2:
            return parts[1].rstrip("/")

    return None


def main():
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("No GitHub token found")
        return

    content_dir = Path("content")
    changes_made = False

    for data_file in content_dir.rglob("data.toml"):
        # Skip the contributors data file
        if "contributors/data.toml" in str(data_file):
            print(f"Skipping contributors file: {data_file}")
            continue

        print(f"Processing {data_file}")
        data = load_toml(data_file)
        file_changes_made = False

        for item in data.get("items", []):
            # Skip if already archived
            if item.get("archived", False):
                print(f"Skipping already archived item: {item.get('name')}")
                continue

            repo = extract_github_repo(item)
            if not repo:
                continue

            print(f"Checking {repo}")
            is_archived = check_github_archive_status(repo, token)

            if is_archived is True:  # Only update if GitHub says it's archived
                item["archived"] = True
                file_changes_made = True
                changes_made = True
                print(f"Marked {repo} as archived")

        if file_changes_made:
            save_toml(data_file, data)

    if not changes_made:
        print("No changes were needed to archive status")


if __name__ == "__main__":
    main()
