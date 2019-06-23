import tweepy
from time import sleep

consumer_key = "Ah5jl7M2EtC9Byu8utbgFFzIo"
consumer_secret = "RXpBEJnPAbconEAWDQ6fLQ6d4kmqwEIIEkEgCSUyglgwQrdqFu"
access_token = "296692836-pzMtALO3JDB0U1ra24xgK7XIU8UrqnJhpJY9ofhx"
access_token_secret = "9NyOua2rTabUKoNga8YGZuegM6do3CSRCHPV7CgWLFazC"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth.secure = True
api = tweepy.API(auth)

myBot = api.get_user(screen_name="princeboaHD")
myList = api.get_list("@" + myBot.screen_name, slug="TwitchStreamer")

print(
    "Running Bot: @"
    + myBot.screen_name
    + "\n Using list: "
    + myList.name
    + "\n Members count: "
    + str(myList.member_count)
    + " Subs count: "
    + str(myList.subscriber_count)
)

for tweet in tweepy.Cursor(api.search, q="#twitchDE", lang="de").items(10):
    try:
        if tweet.user.id == myBot.id:
            continue
        print("\n\nFound tweet by: @" + tweet.user.screen_name)
        if (tweet.retweeted == False) or (tweet.favorited == False):
            tweet.retweet()
            tweet.favorite()
            api.add_list_member(
                screen_name=tweet.user.screen_name,
                owner_screen_name=myBot.screen_name,
                list_id=myList.id,
            )
            print("Retweeted and favcorited the tweet and added the user to my List")
        if tweet.user.following == False:
            tweet.user.follow()
            print("Followed the user")
    except tweepy.TweepError as e:
        print(e)
        sleep(10)
        continue
    except StopIteration:
        break
