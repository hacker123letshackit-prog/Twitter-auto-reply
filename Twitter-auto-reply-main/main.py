import tweepy
import time

# Replace with your keys
auth = tweepy.OAuth1UserHandler(
    "YOUR_API_KEY_HERE",
    "YOUR_API_SECRET_HERE",
    "YOUR_ACCESS_TOKEN_HERE",
    "YOUR_ACCESS_TOKEN_SECRET_HERE"
)
api = tweepy.API(auth)

# Customize your search terms here
search_terms = "#India OR politics"

# Customize your reply here
reply_message = "This is a reply from my Gemini bot!"

while True:
    # Updated search method
    tweets = api.search_tweets(q=search_terms, count=1)
    for tweet in tweets:
        try:
            api.update_status(
                f"@{tweet.user.screen_name} {reply_message}",
                in_reply_to_status_id=tweet.id
            )
            print(f"Replied to @{tweet.user.screen_name}")
        except tweepy.TweepError as e:
            print(e.reason)
    time.sleep(60)
