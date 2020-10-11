# Importing everything we need

import praw
import pdb
import re
import os
import time
from datetime import datetime, date, timedelta
from config_bot import *

# Checking if the config file exists

if not os.path.isfile("config_bot.py"):
    print("You must creat a config file with your username and password.")
    print("Please see config_skel.py")
    exit(1)

# Create a Reddit instance

user_agent = ("tonkatsuninja 0.1")
r = praw.Reddit(user_agent=user_agent)

# Logging in 
print("logging in...")
r.login(REDDIT_USERNAME, REDDIT_PASS, disable_warning=True)

# Checking to see if the reply log file exists
print("checking log file....")
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

else:
   with open("posts_replied_to.txt", "r") as f:
      posts_replied_to = f.read()
      posts_replied_to = posts_replied_to.split("\n")
  


# Create a list of keywords for the bot to search for.

keywords = ['tonkatsu', 'japanese food', 'what is your favorite japanese food?', 'i love tonkatsu', 'japanese bar food']

# Declaring the bot as a function

def first_bot():
    # Grabbing subreddits and comments
    print("getting subreddit comments...")
    subreddit = r.get_subreddit('japan')
    all_comments = subreddit.get_comments(limit=25)



    for comment in all_comments:
        changeup = comment.body.lower() #make the comment lower case
        talks_about_tonkatsu = any(string in changeup for string in keywords) #boolean for deciding if comment meets criteria
        #if the comment talks about tonkatsu and hasn't been commented on before, respond with the correct string
        if talks_about_tonkatsu and comment.id not in posts_replied_to and comment.author != "shiroininja":
           print("Comment author: "+str(comment.author))
           comment_reply = "Tonkatsu Ninja loves tonkatsu! You should too!"
           comment.reply(comment_reply) #reply to the comment
           comment.upvote() #upvote the comment
           print("Replied to a comment: " +str(comment.permalink))
           # Store the current id into our list
           posts_replied_to.append(comment.id)
           print("loop finished, going to sleep now")
           # Write our updated list back to the file
           with open("posts_replied_to.txt", "w") as f:
                for post_id in posts_replied_to:
                    f.write(post_id + "\n")
        else:
            print("No tonkatsu today!")
            print("\n going to bed hungry :(")
                        
     
while True:
    first_bot()
    time.sleep(30)      
