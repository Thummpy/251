from pyspark import SparkConf
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import SQLContext
from pyspark.sql.functions import desc
from collections import namedtuple
fields = ("tag","count")
Tweet = namedtuple('Tweet',fields)



import socket
localIP = socket.gethostbyname(socket.gethostname())
py_files = [
]
SPARK_ENV=[
('spark.app.name',"twitterStreamAggregation"),
('spark.master',"local[2]")#"spark://{}:7077".format(localIP)),
]

CONF = SparkConf().setAll(SPARK_ENV) 

sc = SparkContext(conf=CONF,pyFiles=py_files)
ssc = StreamingContext(sc,30)
sqlContext = SQLContext(sc)
ssc.checkpoint( "file:///tmp")


socket_stream = ssc.socketTextStream(localIP,5555)
lines = socket_stream.window(60)

"""
res = lines.flatMap( lambda text: text.split( " " ) )\
  .filter( lambda word: word.lower().startswith("#") )\
  .map( lambda word: ( word.lower(), 1 ) )\
  .reduceByKey( lambda a, b: a + b )\
  .take(2)
"""

(lines.flatMap( lambda text: text.split( " " ) )\
  .filter( lambda word: word.lower().startswith("#") )\
  .map( lambda word: ( word.lower(), 1 ) )\
  .reduceByKey( lambda a, b: a + b )\
  .map( lambda rec: Tweet( rec[0], rec[1] ) )\
  .foreachRDD( lambda rdd: rdd.toDF().sort( desc("count") ))\
  .limit(10).registerTempTable("tweets")  )


ssc.start()


top_10_tweets = sqlContext.sql( 'Select tag, count from tweets' )
print(top_10_tweets )

