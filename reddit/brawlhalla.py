import praw,random,time,keyboard


reddit = praw.Reddit(
    client_id="h97j_D1DObYQLAgrO5uAjQ",
    client_secret="_ODdH7xacolI0w6w913Kfr0bhSuDmQ",
    username="JapanToTentacles",
    password="mahmoud2005",
    user_agent="japan",
)

keyboard.wait("h")
dire = ""
moves = {
    "up": "up",
    "down": "down",
    "light": "c",
    "heavy": "x",
    "dodge": "shift",
    "throw": "v",
    "dance": "f",
    "jump": "space"
}

for i in reddit.subreddit('all').stream.comments():
    for move in list(moves.keys()):
        if(move in i.body.lower()):
            keyboard.press_and_release(moves[move])
        if("right" in i.body.lower()):
            keyboard.press("right")
            keyboard.release("left")
        elif("left" in i.body.lower()):
            keyboard.press("left")
            keyboard.release("right")
        elif("stop" in i.body.lower()):
            keyboard.release("right")
            keyboard.release("left")
        
        