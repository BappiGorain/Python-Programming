import tweepy

# Twitter API credentials
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAIO90AEAAAAAqdIio3u2Iqg3NakBb7iJG8F3p3c%3D4rO3pY8CU8xyjUzPPMQeK0HgQ6ksMMxjGnrnZFmMY6FO0nyd4f"
# Authenticate with Twitter API v2
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Twitter username (replace with your username)
username = "bappigorain"

# Fetch user details
user = client.get_user(username=username, user_fields=["public_metrics"])

# Get follower count
if user.data:
    print("User ID:", user.data.id)
    print("Username:", user.data.username)
    print("Name:", user.data.name)
    print("Followers Count:", user.data.public_metrics["followers_count"])
else:
    print("User not found.")