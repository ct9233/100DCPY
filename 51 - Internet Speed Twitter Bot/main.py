from speed_test import SpeedTest
from twitter_bot import TwitterBot

PROMISED_DOWN = 150
PROMISED_UP = 10

speeds = SpeedTest()
actual_speeds = speeds.get_internet_speed()
actual_down = float(actual_speeds["download_speed"])
actual_up = float(actual_speeds["upload_speed"])

if PROMISED_DOWN > actual_down or PROMISED_UP > actual_up:
    complaint_tweet = f"Hey Internet Provider, why is my connection speed only {actual_down} Down/{actual_up} Up when I am paying for {PROMISED_DOWN} Down/{PROMISED_UP} Up?!"
    twitter = TwitterBot()
    twitter.tweet_at_provider(complaint_tweet)
else:
    print("No internet speed issues today.")