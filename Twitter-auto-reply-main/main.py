import tweepy
import time

# Replace with your keys
auth = tweepy.OAuthHandler("YOUR_API_KEY_HERE", "YOUR_API_SECRET_HERE")
auth.set_access_token("YOUR_ACCESS_TOKEN_HERE", "YOUR_ACCESS_TOKEN_SECRET_HERE")
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
