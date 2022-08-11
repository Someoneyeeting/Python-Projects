from email import message
from glob import glob
import praw
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from math import *
import time

reddit = praw.Reddit(client_id='GATkP0ZaAaKEpw',
                    client_secret='AWLst0V9gvAzB7nwl7B50ZFmGuBBcg',
                    username='UwUratingbotUwU',
                    password='mahmoud2005',
                    user_agent='UwUratingbotUwU')

me = "a_useless_communist"


def sendPM(user, subject, body):
    reddit.redditor(user).message(subject, body)

#check reseceved messages
def checkPM():
    for message in reddit.inbox.unread():
        message.mark_read()
        if message.body == "Stop":
            return True
    return False

last = None
#for comment in stream comments from r/all
for comment in reddit.subreddit('all').stream.comments():
    #check if ramadan is in comment body and if it is not the same comment as last time
    if "ramadan" in comment.body.lower() and comment.id != last:
        print("found")
        # sendPM(me,"comment","www.reddit.com" + comment.permalink + "?context=3")
        last = comment.id
    if(checkPM()):
        break

sendPM(me,"doned", "im doned")


