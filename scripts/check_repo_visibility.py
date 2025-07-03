#!/usr/bin/env python3
"""
Repository Status Checker

This script helps check the current visibility status of the repository.
Note: This cannot change repository visibility - that must be done through GitHub settings.
"""

import requests
import json
import sys

def check_repo_visibility(owner, repo):
    """
    Check if a GitHub repository is public or private.
    
    Args:
        owner (str): Repository owner username
        repo (str): Repository name
    
    Returns:
        dict: Repository information including visibility status
    """
    try:
        # GitHub API endpoint for repository information
        url = f"https://api.github.com/repos/{owner}/{repo}"
        
        response = requests.get(url)
        
        if response.status_code == 200:
            repo_data = response.json()
            return {
                "exists": True,
                "private": repo_data.get("private", False),
                "visibility": "private" if repo_data.get("private", False) else "public",
                "full_name": repo_data.get("full_name"),
                "description": repo_data.get("description"),
                "url": repo_data.get("html_url")
            }
        elif response.status_code == 404:
            return {
                "exists": False,
                "message": "Repository not found (it might be private or doesn't exist)"
            }
        else:
            return {
                "exists": None,
                "error": f"API request failed with status {response.status_code}",
                "message": response.text
            }
            
    except requests.RequestException as e:
        return {
            "exists": None,
            "error": f"Network error: {str(e)}"
        }

def main():
    """Main function to check repository status."""
    
    # Repository details
    owner = "Abhikcpp"
    repo = "CF-AI-Agent"
    
    print(f"🔍 Checking repository visibility for {owner}/{repo}...")
    print("-" * 50)
    
    result = check_repo_visibility(owner, repo)
    
    if result.get("exists") is True:
        visibility = result.get("visibility", "unknown")
        print(f"✅ Repository found!")
        print(f"📊 Current visibility: {visibility.upper()}")
        print(f"🔗 URL: {result.get('url', 'N/A')}")
        if result.get("description"):
            print(f"📝 Description: {result.get('description')}")
            
        if visibility == "public":
            print("\n💡 To make this repository private:")
            print("   1. Go to repository Settings on GitHub")
            print("   2. Scroll to 'Danger Zone' section")
            print("   3. Click 'Change repository visibility'")
            print("   4. Select 'Make private'")
            print("   5. Confirm by typing the repository name")
            print("\n📖 See docs/REPOSITORY_VISIBILITY_GUIDE.md for detailed instructions")
        else:
            print("\n🔒 Repository is already private!")
            
    elif result.get("exists") is False:
        print("❌ Repository not found or is private")
        print("   (This script can only detect public repositories)")
        
    else:
        print(f"⚠️  Error checking repository: {result.get('error', 'Unknown error')}")
        
    print("\n" + "=" * 50)
    print("📝 IMPORTANT NOTE:")
    print("   Repository visibility CANNOT be changed through code.")
    print("   It must be changed through GitHub's web interface.")
    print("   This script only checks the current status.")
    print("=" * 50)

if __name__ == "__main__":
    main()