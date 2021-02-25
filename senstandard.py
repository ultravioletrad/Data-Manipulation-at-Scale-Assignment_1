import collections
from collections import defaultdict
import json
import nltk
import re
import matplotlib.pyplot as plt
import advertools as adv
from textblob import TextBlob
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
tweet_data = []
tweeten = []
hashtags =[]
tweetfile = open(sys.argv[1],'r', encoding="utf-8")  # three_minutes_tweets.json

#file_path = "C:/Users/three_minutes_tweets.json"
#tweetfile = open(file_path, 'r', encoding="utf-8")
for line in tweetfile:
    tweetline = json.loads(line.encode("utf-8"))
    tweet_data.append(tweetline)
    if tweetline.get('lang') == 'en':
        texten = tweetline.get('text')
        tweeten.append(texten)
hashtag_summary = adv.extract_hashtags(tweeten)
print("___________hashtags summary___________")
print(hashtag_summary['hashtags'])
print("_______top ten hashtags________")
print(hashtag_summary['top_hashtags'][:10])
print("_______hashtag frequency________")
hashtag_summary['hashtag_freq'][:10]
n = int(len(tweeten))
print(n)
processed_tweets = []
for tweet in tweeten:
    # Removing 'http'
    processed_tweet = re.sub(r"http\S+", "", str(tweet))

    # Remove all the special characters
    processed_tweet = re.sub(r'\W', ' ', processed_tweet)

    # remove all single characters
    processed_tweet = re.sub(r'\s+[a-zA-Z]\s+', ' ', processed_tweet)

    # Remove single characters from the start
    processed_tweet = re.sub(r'\^[a-zA-Z]\s+', ' ', processed_tweet)

    # Substituting multiple spaces with single space
    processed_tweet = re.sub(r'\s+', ' ', processed_tweet, flags=re.I)

    # Converting to Lowercase
    processed_tweet = processed_tweet.lower()

    processed_tweets.append(processed_tweet)
print("______sentiment of tweets__________")
for line in processed_tweets:
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

#list of words
wordslist = []
for text in processed_tweets:
    for word in text.split():
        wordslist.append(word)
print(wordslist)
# Given a list of words, return a dictionary of
# word-frequency pairs.
word_freq = defaultdict(int)
for word in wordslist:
    word_freq[word] += 1
print(pd.DataFrame.from_dict(word_freq, orient='index'))
# Create a list of word
text = ["Pakistan,Punjab,Sindh,Baluchistan,Khybar Pakhtunkhwa,Gilgit Baltistan,Kashmir"]
wordcloud = WordCloud(width=480, height=480, background_color="green",colormap="Blues").generate(str(text))

plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()

#if__name__ == '__main__':
 #main()
