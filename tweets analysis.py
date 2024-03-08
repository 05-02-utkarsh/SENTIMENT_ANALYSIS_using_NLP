import GetOldTweets3 as got

def get_tweets():
      tweetCriteria = got.manager.TweetCriteria().setQuerySearch('corona virus')\
                                           .setSince("2020-02-01")\
                                           .setUntil("2021-02-28")\
                                           .setMaxTweets(10)
      tweets = got.manager.TweetManager.getTweets(tweetCriteria)
      print(tweets.text)

get_tweets()