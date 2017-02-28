#Xrhsimopoih8hke python 3.6
import tweepy
consumer_key = "8vTl0EnmaV140OxxtmeZqw1JE"
consumer_secret = "atEiYbqbiPxyy25EKQJh93CEAsnwopC28BpM86SHy4iNUOoSVq"
access_key = "831677434416287746-xkrn2xYLWAPpi2ebjXxHOhwVWXtxvIx"
access_secret = "kBJCLCllO5HHl8WLjXKQhlurOHatTCiNz6ZZEn4Ocht01"

def get_last_10_tweets(screen_name):

    auth = tweepy.OAuthHandler('8vTl0EnmaV140OxxtmeZqw1JE', 'atEiYbqbiPxyy25EKQJh93CEAsnwopC28BpM86SHy4iNUOoSVq')
	auth.set_access_token('831677434416287746-xkrn2xYLWAPpi2ebjXxHOhwVWXtxvIx','kBJCLCllO5HHl8WLjXKQhlurOHatTCiNz6ZZEn4Ocht01')
	api = tweepy.API(auth)
    tenlasttweets=[]
    tenlasttweets=api.user_timeline(screen_name = screen_name,count=10)
    return tenlasttweets
onoma1=input(str("Dwse onoma 1ou xrhsth"))
onoma2=input(str("Dwse onoma 2ou xrhsth"))
