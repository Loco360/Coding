import tweepy
import tkinter
from time import sleep


consumer_key = "Ah5jl7M2EtC9Byu8utbgFFzIo"
consumer_secret = "RXpBEJnPAbconEAWDQ6fLQ6d4kmqwEIIEkEgCSUyglgwQrdqFu"
access_token = "296692836-pzMtALO3JDB0U1ra24xgK7XIU8UrqnJhpJY9ofhx"
access_token_secret = "9NyOua2rTabUKoNga8YGZuegM6do3CSRCHPV7CgWLFazC"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
user = api.me()
print("Connected to the user: " + user.name)


def refollower():
    # count = 0
    for follower in tweepy.Cursor(api.followers).items():
        try:
            follower.follow()
            print("Followed someone who is following " + user.name)
        except tweepy.RateLimitError as e:
            print(e.reason)
            sleep(900)
            continue
        except StopIteration:
            break

        # count += 1


def tweetsfinder(s, counter):
    search = str(s)
    numberOfTweets = int(counter)
    print("Starting the job with " + s)
    for tweet in tweepy.Cursor(api.search, search).items(
        numberOfTweets
    ):  # lang="de" als weitere option
        try:
            print("Found tweet by: @" + tweet.user.screen_name)
            tweet.favorite()
            print("I liked the tweet!")
            sleep(2)
        except tweepy.TweepError as e:
            print(e.reason)
            sleep(10)
            continue
        except StopIteration:
            break


# tweetsfinder("#Gaming", 10)
# tweetsfinder("#Twitch", 100)
# tweetsfinder("#TwitchAffiliate", 50)
# tweetsfinder("#SupportAllstreamers", 50)
# tweetsfinder("#German", 50)
# tweetsfinder("#stream", 50)
tweetsfinder("#Supportsmallstreamers", 30)
tweetsfinder("#twitchDE", 50)
print("The job was completed successfully....")
# refollower()
