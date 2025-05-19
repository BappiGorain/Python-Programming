import requests

# Replace with your actual Bearer Token from X Developer Portal
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAIO90AEAAAAAqdIio3u2Iqg3NakBb7iJG8F3p3c%3D4rO3pY8CU8xyjUzPPMQeK0HgQ6ksMMxjGnrnZFmMY6FO0nyd4f"

def get_user_info(username):
    url = f"https://api.twitter.com/2/users/by/username/{username}?user.fields=id,name,username,description,public_metrics"
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        user_data = response.json()["data"]
        print("User ID:", user_data["id"])
        print("User Name:", user_data["name"])
        print("Screen Name:", user_data["username"])
        print("Description:", user_data["description"])
        print("Followers Count:", user_data["public_metrics"]["followers_count"])
    else:
        print("Error:", response.status_code, response.text)

# Replace 'elonmusk' with any Twitter username
get_user_info("bappigorain")



