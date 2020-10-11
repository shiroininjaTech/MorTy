# Importing everything we need

import praw
import pdb
import re
import os
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

r.login(REDDIT_USERNAME, REDDIT_PASS, disable_warning=True)

# Checking to see if the reply log file exists

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

else:
   with open("posts_replied_to.txt", "r") as f:
      posts_replied_to = f.read()
      posts_replied_to = posts_replied_to.split("\n")
      posts_replied_to = filter(None, posts_replied_to)

# We get the last 5 entries from our subreddit

subreddit = r.get_subreddit('food')
for submission in subreddit.get_hot(limit=200):
    #print submissiont.title

    # If we haven't replied to this submission before
    if submission.id not in posts_replied_to:
       	
  
       # Do a case insenstive search
       if re.search("japanese food", submission.title, re.IGNORECASE):

           # Reply to the post
           submission.add_comment("Tonkatsu Ninja loves Tonkatsu!!")
           print("Bot replying to : ", submission.title)

       else:
           print("Can't find any targets.")

           # Store the current id into our list
           posts_replied_to.append(submission.id)

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
