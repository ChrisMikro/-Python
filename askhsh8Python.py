#Xrhsimopoih8hke python 3.6
import tweepy

def listesfollowers(username):
    listafollower=[]
    k=1
    for page in tweepy.Cursor(api.followers, id=username).pages():
        for UserFollower in page:
            listafollower.append(UserFollower.screen_name)
        k+=1
    return listafollower



from tweepy import OAuthHandler

consumer_key = '8vTl0EnmaV140OxxtmeZqw1JE'
consumer_secret = 'atEiYbqbiPxyy25EKQJh93CEAsnwopC28BpM86SHy4iNUOoSVq'
access_token = '831677434416287746-xkrn2xYLWAPpi2ebjXxHOhwVWXtxvIx'
access_secret = 'kBJCLCllO5HHl8WLjXKQhlurOHatTCiNz6ZZEn4Ocht01'
auth = OAuthHandler('8vTl0EnmaV140OxxtmeZqw1JE', 'atEiYbqbiPxyy25EKQJh93CEAsnwopC28BpM86SHy4iNUOoSVq')
auth.set_access_token('831677434416287746-xkrn2xYLWAPpi2ebjXxHOhwVWXtxvIx', 'kBJCLCllO5HHl8WLjXKQhlurOHatTCiNz6ZZEn4Ocht01')
api = tweepy.API(auth)

Onoma1=input(str("Dwse 1o onoma xrhsth "))
Onoma2=input(str("Dwse 2o onoma xrhsth "))

lista1=listesfollowers(Onoma1)
lista2=listesfollowers(Onoma2)
lista3=list(set(lista1).intersection(lista2))
if len(lista3)==0:
    print ("Den uparxoun koinoi followers")
else:
    i=0
    while i<len(lista3):
        print ("@"+lista3[i])
        i+=1
