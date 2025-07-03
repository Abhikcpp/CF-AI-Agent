from backend.tools.data_fetcher import fetch_user_submissions

# Replace "tourist" with a valid Codeforces handle to test
handle = "tourist"

try:
    print(f"Fetching submissions for handle: {handle}...")
    submissions = fetch_user_submissions(handle)
    print("API call successful. Submissions fetched:")
    print(submissions[:5])  # Print the first 5 submissions (if available)
except Exception as e:
    print(f"Error while fetching submissions: {e}")