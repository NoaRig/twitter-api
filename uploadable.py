# tweepy is the library being sed to access the twitter API
# followed the streaming example located in their api documentation
import tweepy

# override tweepy.StreamListener to add Logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

if __name__ == '__main__':

    # the parameters for the following function call are supplied once you register your
    # application with twitter.

    file_object = open("tweet-example.txt", "w+")

    key = "your key here"

    secret = "your secret here"

    auth = tweepy.OAuthHandler(key, secret)

    api = tweepy.API(auth)
    i = 0
    for tweet in tweepy.Cursor(api.search, q=('covid-19 OR #covid19 OR #china-virus'),
                               since='2020-03-01', until='2020-9-25',
                               lang="en").items():
        i += 1
        file_object.write(f'Tweet [{i}]: ' + tweet.text)
