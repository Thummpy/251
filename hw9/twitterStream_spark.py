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
('spark.master',"spark://{}:7077".format(localIP)),
]

CONF = SparkConf().setAll(SPARK_ENV) 

sc = SparkContext(conf=CONF,pyFiles=py_files)
ssc = StreamingContext(sc,1)
sqlContext = SQLContext(sc)
#ssc.checkpoint( "file:///tmp")


#socket_stream.window 
lines= ssc.socketTextStream('localhost',5555)
#lines = socket_stream.window(20)


#res = lines.flatMap( lambda text: text.split( " " ) )\
#  .filter( lambda word: word.lower().startswith("#") )\
#  .map( lambda word: ( word.lower(), 1 ) )\
#  .foreachRDD( lambda rdd: rdd.toDF().sort( desc("count") ))\
#  .limit(10).registerTempTable("tweets")


#lines.pprint(2)

res = lines.flatMap( lambda t: t.split( " " ) )
res.pprint()
#  .filter( lambda word: word.lower().startswith("#") )\
#  .map( lambda word: ( word.lower(), 1 ) )\
#  .reduceByKey( lambda a, b: a + b )\
#  .pprint(2)
#  .map( lambda rec: Tweet( rec[0], rec[1] ) )\
#  .foreachRDD( lambda rdd: rdd.toDF().sort( desc("count") ))\
#  .pprint(5)
#  .limit(10).registerTempTable("tweets")  )


ssc.start()
ssc.awaitTermination()


#top_10_tweets = sqlContext.sql( 'Select tag, count from tweets' )
#print(top_10_tweets )

