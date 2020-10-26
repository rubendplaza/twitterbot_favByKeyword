import tweepy
import time

auth = tweepy.OAuthHandler('CNfxkwoRGEBPRjFpWdpT4JVpE',
                           'I4u1jtENv08G515bt4hlRefksuutHvh16iaTKKQmijNKmpeBan')
auth.set_access_token('1271899099143512064-mVywX9wt3fy4HFnvugw1BMLBK63Iwx',
                      'bsc7wTHRJwxKimfWStORr5AbnmVwRCa4eLzyICrGG598A')

api = tweepy.API(auth)
user = api.me()
print(user.name)
print(user.screen_name)
print(user.followers_count)


searchString = 'Ruben Plaza'
numOfTweets = 5

for tweet in tweepy.Cursor(api.search, searchString).items(numOfTweets):
    try:
        tweet.favorite()
        # tweet.retweet()
        print(f'I liked that tweet: {tweet.text}')
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
