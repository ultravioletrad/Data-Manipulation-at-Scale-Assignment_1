import sys

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])     #AFINN.txt
    tweet_file = open(sys.argv[2])    #three_minutes_tweets.json
    hw()
    lines(sent_file)
    lines(tweet_file)


if __name__ == '__main__':
    main()
