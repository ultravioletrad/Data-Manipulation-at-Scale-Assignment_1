# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 11:36:03 2019

@author: hp
"""

import sys
import re
import json

tweet_file = open(sys.argv[1],'r', encoding="utf-8")  # three_minutes_tweets.json
tweet_data = []
for line in tweet_file:
    tweet = json.loads(line.encode("utf-8"))
    tweet_data.append(tweet)
f = "C:/Users/Z.Ahmad/output.txt"
with open(f, "w+",encoding="utf-8") as f1:
    print(tweet_data[0:8298], file=f1)
print(len(tweet_data))
f2="C:/Users/Z.Ahmad/problem_1_submission.txt"
with open(f2, "w+", encoding="utf-8") as f3:
    for i in range(1, 21):
        print(tweet_data[i], file=f3)




