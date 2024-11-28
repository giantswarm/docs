#!/bin/bash

# Check if jq is installed
if ! command -v jq &>/dev/null; then
    echo "jq is required but not installed. Please install jq and try again."
    exit 1
fi

# Check if yq is installed
if ! command -v yq &>/dev/null; then
    echo "yq is required but not installed. Please install yq and try again."
    exit 1
fi

CONFIG="config.yaml"

# Function to update the commit_reference with the latest release
update_commit_reference() {
    local url="$1"
    local latest_release

    # Extract the repo name from the URL for API call
    repo_name=$(echo "$url" | awk -F '/' '{print $(NF-1)"/"$NF}')

    # Fetch the latest release tag from GitHub API
    latest_release=$(curl -s "https://api.github.com/repos/$repo_name/releases/latest" | jq -r '.tag_name')

    # If the API call was successful and we got a tag name
    if [[ "$latest_release" != "null" ]]; then
        echo "Updating $repo_name to latest release: $latest_release"
        # Update the YAML file with the new commit_reference
        yq eval -i "(.source_repositories[] | select(.url == \"$url\").commit_reference) = \"$latest_release\"" "$CONFIG"
    else
        echo "Failed to fetch latest release for $repo_name"
    fi
}

# Loop through each source repository in the YAML file
yq eval '.source_repositories[] | .url' "$CONFIG" | while read -r url; do
    update_commit_reference "$url"
done

echo "Update complete."
