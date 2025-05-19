import tweepy


client = tweepy.Client(bearer_token="AAAAAAAAAAAAAAAAAAAAAIO90AEAAAAAqdIio3u2Iqg3NakBb7iJG8F3p3c%3D4rO3pY8CU8xyjUzPPMQeK0HgQ6ksMMxjGnrnZFmMY6FO0nyd4f")

query = "Python programming"  # Replace with your search term

tweets = client.search_recent_tweets(query=query, max_results=15)

# Print tweets
for tweet in tweets.data:
    print(f"Tweet: {tweet.text}\n")