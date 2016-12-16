## 251 HW 9
Build a spark cluster, consume twitter feed and aggregate tweets.

###Checklist:  
  * spark cluster (done, aws ubuntu)
  * build twitter feed (done, using tweepy. Chose to do this project in pythonas I am less familiar with scala)
  * connect stream into spark (done, using socket connect)
  * process data ( TO DO: fix errors in performing actions on ssc)
  * analytics ( TO DO)
  * output (TO DO)
  
###Struggles
  * Tried scala, but it is unkown, presented too much technical risk when coupled with unknown systems
  * Using Tweepy for python based data feed, not many issues but pickup of socket had to be worked out
  * ssc not wanting to process data, getting lots of errors ie 
    * DAGScheduler: ResultStage 2 (start at NativeMethodAccessorImpl.java:-2) failed in 3.401 s
  
  
