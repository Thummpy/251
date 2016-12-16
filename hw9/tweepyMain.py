from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="GVcdBbfgALXfjNXok3qxbl7YG"
consumer_secret="XRupNcUhquhfl5j6t89HXwYlYNySejcqrQiSyOyW1f2D0a5i7R"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="2851500565-WAFeOr2up2y9SDIV5lMD4TVa1kirJiItAmnxq1m"
access_token_secret="7AvBCaoztFVEK8InvwCx0OYmguDNhr4ZEzyzQDzHmixG9"

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['basketball'])
