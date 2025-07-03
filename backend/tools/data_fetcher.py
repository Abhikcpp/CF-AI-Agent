import requests

CODEFORCES_API_URL = "https://codeforces.com/api"

def fetch_user_submissions(handle):
    """
    Fetch recent submissions of a Codeforces user.
    :param handle: Codeforces user handle.
    :return: List of submission data.
    """
    url = f"{CODEFORCES_API_URL}/user.status"
    params = {"handle": handle}
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json().get("result", [])
    else:
        raise Exception(f"Failed to fetch submissions for handle: {handle}. Status Code: {response.status_code}")