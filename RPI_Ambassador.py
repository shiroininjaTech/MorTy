""" This is the module for Morty's first job, The Raspberry Pi Ambassador.
    It is basically a bot that searches /r/raspberry_pi for comments that ask for information about the
    Raspberry Pi
"""



import praw
import pdb
import re
import os
from config_bot import *
import RPi.GPIO as GPIO
import re

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
BLUE_LED = 5
""" Version 1.1 removed the use of RED_LED2"""
#RED_LED2 = 21 
GPIO.setup(BLUE_LED, GPIO.OUT)
#GPIO.setup(RED_LED2, GPIO.OUT)

# The variables for the module. For version 1.0 I've added new search phrases and messages.
user_agent = ' '
r = ' '
question = ['what is a raspberry pi', 'what is a rpi', 'where can i get info on the raspberry pi', 'where can i get info on the rpi', 'where can i find information on the raspberry pi', 'where can i find information on the rpi', 'where can i find information about the rpi', 'where can i find information about the raspberry pi', 'what is a good mini computer', 'what is a cheap mini computer',  'show me info on the raspberry pi!', 'what is a good way to learn programming', 'what is a fun way to learn progamming', 'what is a good way to learn python', 'what is a fun way to learn python', 'python learning tool', 'what is the cheapest pc', 'what is a great gift for a programmer', 'how to teach kids python', 'where can i find info on the raspberry pi?', 'raspberry pi help', 'need help finding info on the raspberry pi', 'need help finding information on the rpi', 'what is a rpi', 'inexpensive computers', 'what is a good linux computer', 'where can i get info on the raspberry pi zero', 'information on the raspberry pi zero']
count = 1
message = 'Bleep! Bloop! I am a bot. A Raspberry Pi is an amazing mini-computer that is the size of a credit card with a small price tag to boot. The Raspberry Pi is a great tool to teach others to learn how to code. It is also great for a media center/retro gaming console. I am even powered by a pi! But really, the possibilities are only limited by your imagination. For more information visit /r/raspberry_pi or [raspberrypi.org](https://www.raspberrypi.org). I can also be summoned with the phrase show me info on the raspberry pi! '
message_count = 1
bad_target = ['A Raspbery Pi is an amazing mini-computer that is as big as a credit card. The Raspberry Pi is a great tool to teach others to learn how to code. It is also great for a media center/retro gaming console. For more information visit /r/raspberry_pi or [raspberrypi.org](https://www.raspberrypi.org). ']
posts_replied_to =[]
buy_zero_message = '*bleep* *boop* I am a bot. Hello human, I am excited as you are about the release of the new Raspbery pi zero! A few places this wonderous $5 mini-computer can buy are [The Pi Hut](http://thepihut.com/products/raspberry-pi-zero) or [Pimoroni](http://pimoroni.com/zero) if you are a British humanoid. If you are of the American variety, it can be found at [Adafruit](http://www.adafruit.com/pizero) or for instore pickup at [Micro Center](http://www.microcenter.com/product/457746/Raspberry_Pi_Zero). Be aware that my intellegience reports that units are selling out very quickly. for more information, visit [raspberrypi.org](https://www.raspberrypi.org) or visit /r/raspberry_pi.'
buy_find = ['where can i purchase a rpi zero', 'where can i buy a rpi zero', 'where can i order a rpi zero', 'where can i order a raspberry pi zero', 'where can i buy a raspberry pi zero', 'where can i purchase a raspberry pi zero', 'where to buy pi zero']
project_ideas_question = ['what can i do with a rpi', 'what can i do with a raspberry pi', 'what can i make with a raspberry pi', 'what can i make with a rpi', 'what are some rpi project ideas', 'what are some raspberry pi project ideas', 'need help finding ideas for rpi projects', 'need help finding ideas for raspberry pi projects', 'what do people use raspberry pis for', 'what do people use rpis for', 'what to use a raspberry pi zero for', 'raspberry pi zero project ideas']
project_ideas_message = '*bleep* *bloop* I am a bot. Hello human! I see you need some help finding uses for that mini pc we all love, the Raspberry Pi! Some projects that others have done are: automatic plant waterers, retro gaming console, living room multimedia center with OSMC, automated and motion activated wildlife cameras, magic mirrors, airplay pandora music boxes, and arcade cabinets. Really, I can go on all day. The only limit to what you can make is your imagination! infact, I am even powered by a raspberry pi! for more project ideas, meet the makers at /r/raspberry_pi or visit [raspberrypi.org](https://www.raspberrypi.org/)'
project_ideas_question2 = ['what can i do with a rpi', 'what can i do with a raspberry pi', 'what can i make with a rth a rpi', 'what are some rpi project ideas', 'what are some raspberry pi project ideas', 'need help finding ideas for rpi projects', 'need help finding ideas for raspberry pi projects', 'what do people use raspberry pis for', 'what do people use rpis for', 'what to use a raspberry pi zero for', 'raspberry pi zero project ideas', 'what can i do with it', 'cool raspberry pi projects', 'do with this', 'what can i make', 'now what?', 'ideas for projects', 'what can i do', 'i don\t know what to do with it', 'good projects', 'project ideas']

# Punching in. Creating a Reddit instance 

def punch_in():
   global posts_replied_to
   # Checking to see if the reply log file exists
   print("checking log file....")
   if not os.path.isfile("posts_replied_to.txt"):
       posts_replied_to = []

   
   else:
       with open("posts_replied_to.txt", "r") as f:
          posts_replied_to = f.read()
          posts_replied_to = posts_replied_to.split("\n")

   global user_agent
   global r
   user_agent = ("RPI Ambassador 1.1")
   r = praw.Reddit(user_agent=user_agent)

   print("logging in...")
   r.login(REDDIT_USERNAME, REDDIT_PASS, disable_warning=True)


   return

# Next we have a function that asks the user for the items to search for.

def get_question():
    global question
    global count
    #question = input('What would you like me to search for, boss?\n')

    while count == 0:
        print(question)
        count = 1
    return 
# This is the function to promp the user to tell Morty what to say 

def get_message():
    global message
    global message_count
    #message = input("What would you like me to say?\n")

    while message_count == 0:
        print(message)
        message_count = 1
    return message
    return message_count

def get_to_work():
    print("getting subreddit comments...")
    multi_reddits = r.get_subreddit('raspberry_pi+learnpython+pcmasterrace+MiniPCs+technology+learnprogramming+RASPBERRY_PI_ZERO')
    all_comments = multi_reddits.get_comments(limit=300)
    global posts_replied_to
    for comment in all_comments:
        changeup = str(comment).lower() 
        rpi_asks = any(string in changeup for string in question)
        buy_asks = any(string in changeup for string in buy_find)
        project_asks = any(string in changeup for string in project_ideas_question) 
        if rpi_asks and comment.id not in posts_replied_to and str(comment.author) != 'RPI_Ambassador':
            print("Comment author: "+str(comment.author))
            comment_reply = message
            comment.reply(comment_reply) #Reply to the comment
            comment.upvote() #upvote the comment
            print("Replied to a comment: " +str(comment.permalink))
            posts_replied_to.append(comment.id)
            GPIO.output(BLUE_LED, True)
            #GPIO.output(RED_LED2, False)
            print("loop finished, going to sleep now\n")
            with open("posts_replied_to.txt", "w") as f:
                for comment_id in posts_replied_to:
                    f.write(comment_id + "\n")

        # If the commenter asks about raspberry pi zero

        if buy_asks and comment.id not in posts_replied_to and str(comment.author) != 'RPI_Ambassador':
            print("Comment author: "+str(comment.author))
            comment_reply = buy_zero_message
            comment.reply(comment_reply) #Reply to the comment
            comment.upvote() #upvote the comment
            print("Replied to a comment: " +str(comment.permalink))
            posts_replied_to.append(comment.id)
            GPIO.output(BLUE_LED, True)
            #GPIO.output(RED_LED2, False)
            print("loop finished, going to sleep now\n")
            with open("posts_replied_to.txt", "w") as f:
                for comment_id in posts_replied_to:
                    f.write(comment_id + "\n")
        # If the commenter asks about raspberry pi projects

        if project_asks  and comment.id not in posts_replied_to and str(comment.author) != 'RPI_Ambassador':
            print("Comment author: "+str(comment.author))
            comment_reply = project_ideas_message
            comment.reply(comment_reply) #Reply to the comment
            comment.upvote() #upvote the comment
            print("Replied to a comment: " +str(comment.permalink))
            posts_replied_to.append(comment.id)
            GPIO.output(BLUE_LED, True)
            #GPIO.output(RED_LED2, False)
            print("loop finished, going to sleep now\n")
            with open("posts_replied_to.txt", "w") as f:
                for comment_id in posts_replied_to:
                    f.write(comment_id + "\n")

        


        

        else:
            print("No targets aquired today, sir!\n")
            #GPIO.output(RED_LED2, True)
            

""" Version 1.0 of RPI_Ambassador introduces the ability of morty to also search posts and reply to them"""

def third_shift():

    print("Getting list of posts to target")
    subreddits = r.get_subreddit('raspberry_pi+RASPBERRY_PI_ZERO')        
    submissions = subreddits.get_new(limit=50)
    for submission in submissions:
        changeit= submission.selftext.lower()
        changeit2= submission.title.lower()
        asks_rpi2 = any(string in changeit2 for string in question)
        asks_buy2 = any(string in changeit2 for string in buy_find)
        asks_project2 = any(string in changeit2 for string in project_ideas_question2)
        asks_rpi = any(string in changeit for string in question)
        asks_buy = any(string in changeit for string in buy_find)
        asks_project = any(string in changeit for string in project_ideas_question2)

        if asks_rpi|asks_rpi2 and submission.id not in posts_replied_to:
            print("Replying to : "+str(submission.title))
            post_reply = message
            submission.add_comment(post_reply) #Reply to the comment
            submission.upvote() #upvote the comment
            posts_replied_to.append(submission.id)
            GPIO.output(BLUE_LED, True)
            #GPIO.output(RED_LED2, False)
            print("loop finished, going to sleep now\n")
            with open("posts_replied_to.txt", "w") as f:
                for submission_id in posts_replied_to:
                    f.write(submission_id + "\n")

        if asks_buy|asks_buy2 and submission.id not in posts_replied_to:
            print("Replying to : "+str(submission.title))
            post_reply = buy_zero_message
            submission.add_comment(post_reply) #Reply to the comment
            submission.upvote() #upvote the comment
            posts_replied_to.append(submission.id)
            GPIO.output(BLUE_LED, True)
            #GPIO.output(RED_LED2, False)
            print("loop finished, going to sleep now\n")
            with open("posts_replied_to.txt", "w") as f:
                for submission_id in posts_replied_to:
                    f.write(submission_id + "\n")

        if asks_project|asks_project2 and submission.id not in posts_replied_to:
            print("Replying to : "+str(submission.title))
            post_reply = project_ideas_message
            submission.add_comment(post_reply) #Reply to the comment
            submission.upvote() #upvote the comment
            posts_replied_to.append(submission.id)
            GPIO.output(BLUE_LED, True)
            #GPIO.output(RED_LED2, False)
            print("loop finished, going to sleep now\n")
            with open("posts_replied_to.txt", "w") as f:
                for submission_id in posts_replied_to:
                    f.write(submission_id + "\n")

        else:
           print("This job is getting boring.")
           #GPIO.output(RED_LED2, True)
