import sys
import pandas as pd
import json
from textblob import TextBlob
def hw():
    print( 'Hello, world!')

def lines(fp):
    print(str(len(fp.readlines())))

def main():
    sent_file = open(sys.argv[1],'r', encoding="utf-8")  # AFINN.txt
    tweet_file = open(sys.argv[2],'r', encoding="utf-8")  # three_minutes_tweets.json
    hw()
    for line in tweet_file:
        tweetline = json.loads(line.encode("utf-8"))
        tweet_data.append(tweetline)
    for i in range(int(len(tweet_data))):
        print(tweet_data[i], f1)
    # building dataframe from list
    tweetdf = pd.DataFrame(tweet_data, columns=['text', 'lang', 'hashtags'])
    print(tweetdf[:50])
    tweetsen = []
    tweetsen = tweetdf['text'][tweetdf['lang'] == 'en']
    for line in tweetsen:
        tweettext = TextBlob(str(line))
        print(tweettext)
        print(tweettext.sentiment)
        print('polarity: {}'.format(tweettext.sentiment.polarity))
        print('subjectivity: {}'.format(tweettext.sentiment.subjectivity))
        if tweettext.sentiment[0] > 0:
            print('Positive')
        elif tweettext.sentiment[0] < 0:
            print('Negative')
        else:
            print('Neutral')

if __name__ == '__main__':
    main()
