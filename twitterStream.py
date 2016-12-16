import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import socket
import json
import socket
localIP = socket.gethostbyname(socket.gethostname())

consumer_key = 'GVcdBbfgALXfjNXok3qxbl7YG'
consumer_secret = 'XRupNcUhquhfl5j6t89HXwYlYNySejcqrQiSyOyW1f2D0a5i7R'
access_token = '2851500565-WAFeOr2up2y9SDIV5lMD4TVa1kirJiItAmnxq1m'
access_secret = '7AvBCaoztFVEK8InvwCx0OYmguDNhr4ZEzyzQDzHmixG9'

class TweetsListener(StreamListener):

  def __init__(self, csocket):
      self.client_socket = csocket

  def on_data(self, data):
      try:
          msg = json.loads( data )
          print( msg['text'].encode('utf-8') )
          self.client_socket.send( msg['text'].encode('utf-8') )
          return True
      except BaseException as e:
          print("Error on_data: %s" % str(e))
      return True

  def on_error(self, status):
      print(status)
      return True

def sendData(c_socket):
  auth = OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_secret)

  twitter_stream = Stream(auth, TweetsListener(c_socket))
  twitter_stream.filter(track=['trump'])

if __name__ == "__main__":
  s = socket.socket()         # Create a socket object
  host = localIP      # Get local machine name
  port = 5555                 # Reserve a port for your service.
  s.bind((host, port))        # Bind to the port

  print("Listening on port: %s" % str(port))

  s.listen(5)                 # Now wait for client connection.
  c, addr = s.accept()        # Establish connection with client.

  print( "Received request from: " + str( addr ) )

  sendData( c )
