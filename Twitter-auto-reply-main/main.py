import tweepy
import time

# Replace with your keys
auth = tweepy.OAuthHandler("7EPPcZzplJA25sKRAaNqMdMwD", "dg0UekFizUj8sW1l28O3QSzf8FR3j9iOjUnTzSnuxrpwCMsyDk")
auth.set_access_token("1962147919429259265-kM1FybPbeBJr0s9xZShqQlChpesITf", "YLMZPxHMqKTT1KtBMx0M0ppM20AS22C27Dh5pdYYQKleZ")
api = tweepy.API(auth)

# Customize your search terms here
search_terms = "#India OR politics"

# Customize your reply here
reply_message = "This is a reply from my Gemini bot!"

while True:
    for sn in tweepy.Cursor(api.search, q=search_terms).items(1):
        try:
            api.update_status("@" + sn.user.screen_name + " " + reply_message, in_reply_to_status_id=sn.id)
            print("Replied to @" + sn.user.screen_name)
        except tweepy.TweepError as e:
            print(e.reason)
    time.sleep(60)  # Wait 1 minute between checks
