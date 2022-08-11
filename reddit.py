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

replays = []


def sendPM(user, subject, body):
    reddit.redditor(user).message(subject, body)


starttime = time.time()

subreddits = ["memes","dankmemes","shitposting","me_irl","animemes","goodanimemes","antimeme","UnexpectedJoJo","all"]
for y in subreddits:
    prevcomment = None
    for submission in reddit.subreddit(y).top(limit=None):
        try:
            submission : praw.models.Submission
            if(submission.over_18):
                submission.comments.replace_more(limit=None)
                for comment in submission.comments.list():
                    if prevcomment != comment.id:
                        prevcomment = comment.id
                        if "sauce" in comment.body.lower():
                            for replay in comment.replies.list():
                                #if there is a link in the replay body
                                if ("http" or "www." or ".com" or ".net" or ".org") in replay.body:
                                    replays.append("www.reddit.com" + comment.permalink + "?context=3")
        except Exception as e:
            sendPM("a_useless_communist","error",str(e))

    #write replays to file

#store the error

time.sleep(3)
with open("replays.txt", "w") as f:
    for replay in replays:
        f.write(replay + "\n")
import os
try:
    #shutdown pc
    os.system("shutdown -s -t 0")
except:
    #run the file shut.bat
    os.system("shut.bat")
sendPM("a_useless_communist","doned", "the sause is done")


