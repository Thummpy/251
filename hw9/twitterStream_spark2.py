from tweepy import Stream
from tweepy.streaming import StreamListener
import tweepy
from tweepy import OAuthHandler








consumer_key = 'GVcdBbfgALXfjNXok3qxbl7YG'
consumer_secret = 'XRupNcUhquhfl5j6t89HXwYlYNySejcqrQiSyOyW1f2D0a5i7R'
access_token = '2851500565-WAFeOr2up2y9SDIV5lMD4TVa1kirJiItAmnxq1m'
access_secret = '7AvBCaoztFVEK8InvwCx0OYmguDNhr4ZEzyzQDzHmixG9'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 







class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print('Error on_data: '.format(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['rump'])
