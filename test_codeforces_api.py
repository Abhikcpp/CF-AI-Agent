import requests

def test_codeforces_api():
    # API endpoint
    url = "https://codeforces.com/api/user.info?handles=tourist"
    # Parameter: user handle
    params = {"handles": "tourist"}
    
    try:
        # Send the GET request
        response = requests.get(url, params=params)
        
        # Check response status
        if response.status_code == 200:
            print("API is working correctly!")
            print("Response:", response.json())
        else:
            print(f"API returned an error. Status code: {response.status_code}")
            print("Error message:", response.text)
    except Exception as e:
        print("An error occurred while testing the API:", e)

if __name__ == "__main__":
    test_codeforces_api()