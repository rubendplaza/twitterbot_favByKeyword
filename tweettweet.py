import tweepy
import time
import keys

# User will need to create twitter developer account to get keys
# Once user receives keys, make a "keys.py" file and make four string variables named apiKey, apiSecretKey, accessToken, secretAccessToken and fill with corresponding keys.
auth = tweepy.OAuthHandler(keys.apiKey,
                           keys.apiSecretKey)
auth.set_access_token(keys.accessToken,
                      keys.secretAccessToken)

api = tweepy.API(auth)
user = api.me()
# print(user.name)
# print(user.screen_name)
# print(user.followers_count)


searchString = 'Python'
numOfTweets = 3

for tweet in tweepy.Cursor(api.search, searchString).items(numOfTweets):
    try:
        tweet.favorite()
        # tweet.retweet()
        print(f'I liked that tweet: {tweet.text}\n')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

# def limit_handler(cursor):
#     # tweep allows us to work with the rate limit by twitter
#     try:
#         while True:
#             yield cursor.next()
#     except tweepy.RateLimitError:
#         time.sleep(1000)

# # generous bot
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     if follower.name == 'rubendplaza':
#         follower.follow()
#         break
#     if follower.followers_count > 100:
#         follower.follow()
#         break
