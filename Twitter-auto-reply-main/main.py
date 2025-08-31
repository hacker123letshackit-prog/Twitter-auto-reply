import tweepy
import time

# Replace with your keys
auth = tweepy.OAuth1UserHandler(
    "7EPPcZzplJA25sKRAaNqMdMwD",
    "dg0UekFizUj8sW1l28O3QSzf8FR3j9iOjUnTzSnuxrpwCMsyDk",
    "1962147919429259265-kM1FybPbeBJr0s9xZShqQlChpesITf",
    "YLMZPxHMqKTT1KtBMx0M0ppM20AS22C27Dh5pdYYQKleZ"
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
