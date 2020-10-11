""" 
  * This is the module for Morty's first job, The Raspberry Pi Ambassador.
  * It is basically a bot that searches /r/raspberry_pi for comments that ask for information about the
  * Raspberry Pi.
"""

""" 
  * Changelog:
  * Version 1.0 introduced the ability to also search posts and reply to them.
  * Version 2.0 Involved a reworking of the entire module replacing the search lists
  * with Regular Expressions for better accuracy. Also involved the removal of the get_question() 
  * and get_message() functions.
"""
import praw
import pdb
import re
import os
from config_bot import *
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
BLUE_LED = 5
GPIO.setup(BLUE_LED, GPIO.OUT)

# The the search variables for the module
rpi_asks_regex = re.compile(r'(what|where) (is a|can i get) (info)? (.*?) (raspberry pi|rpi)(.*?)', re.I) 
rpi_asks_regex2 = re.compile(r'show me info(rmation)? (on|about) (.*?) (raspberry pi|rpi)', re.I)
rpi_asks_regex3 = re.compile(r'what (.*?) (good|fun|easy) learn (python|programming)', re.I)
buy_find_regex = re.compile(r'where (can|to) (i)? (buy|purchase|order|get) (a)? (raspberry pi|rpi) zero', re.I)
project_ideas_regex = re.compile(r'what can i (do|make|build) with a (raspberry pi|rpi) (zero)?', re.I) 
project_ideas_regex2 = re.compile(r'(need)? help finding (.*?) (raspberry pi|rpi) (zero)? project(s)? (ideas)?', re.I)  
project_post = ['what can i do with it', 'cool raspberry pi projects', 'cool rpi projects', 'now what?', 'ideas for projects', 'project ideas'] 
user_agent = ' '
r = ' '

# Message variables

project_ideas_message = '*bleep!* *bloop!* I am a bot. Hello human! I see you need some help finding uses for that mini pc we all love, the Raspberry Pi! Some projects that others have done are:\n * automatic plant waterers\n * retro gaming console\n * living room multimedia center with OSMC\n * automated and motion activated wildlife cameras\n * magic mirrors\n * airplay pandora music boxes\n * arcade cabinets\n * pi holes\n Really, I can go on all day. The only limit to what you can make is your imagination! Infact, I am even powered by a raspberry pi! for more project ideas, meet the makers at /r/raspberry_pi or visit [raspberrypi.org](https://www.raspberrypi.org/) and [instructables.com](http://www.instructables.com/tag/type-id/category-technology/channel-raspberry-pi/)'
buy_zero_message = '*bleep!* *bloop!* I am a bot. Hello human, I am excited as you are about the release of the new Raspbery pi zero! A few places this wonderous $5 mini-computer can buy are [The Pi Hut](http://thepihut.com/products/raspberry-pi-zero) or [Pimoroni](http://pimoroni.com/zero) if you are a British humanoid. If you are of the American variety, it can be found at [Adafruit](http://www.adafruit.com/pizero) or for instore pickup at [Micro Center](http://www.microcenter.com/product/457746/Raspberry_Pi_Zero). Be aware that my intellegience reports that units are selling out very quickly. for more information, visit [raspberrypi.org](https://www.raspberrypi.org) or visit /r/raspberry_pi.'
message = '*Bleep!* *Bloop!* I am a bot. A Raspbery Pi is an amazing mini-computer that is as big as a credit card. The Raspberry Pi is a great tool to teach others to learn how to code. It is also great for a media center/retro gaming console. For more information visit /r/raspberry_pi or [raspberrypi.org](https://www.raspberrypi.org). I can also be summoned with the phrase show me info on the raspberry pi! '
posts_replied_to = []
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
   user_agent = ("RPI Ambassador 2.2")
   r = praw.Reddit(user_agent=user_agent)

   print("logging in...")
   r.login(REDDIT_USERNAME, REDDIT_PASS, disable_warning=True)


   return


def get_to_work():
    print("getting subreddit comments...")
    multi_reddits = r.get_subreddit('raspberry_pi+python+learnpython+pcmasterrace+MiniPCS+technology+microcomputing+linux+technology+retropie+RASPBERRY_PI_ZERO+RASPBERRY_PI_PROJECTS')
    
    #multi_reddits = r.get_subreddit('reddit_bot_test')

    all_comments = multi_reddits.get_comments(limit=800)
    global posts_replied_to

    for comment in all_comments:
        # Setting up regix to search the comment body   
        comments = comment.body
        rpi_asks = rpi_asks_regex.search(comments)
        rpi_info = rpi_asks_regex2.search(comments)
        rpi_pro = rpi_asks_regex3.search(comments)
        project_asks = project_ideas_regex.search(comments) 
	project_asks2 = project_ideas_regex2.search(comments)
	buy_find = buy_find_regex.search(comments)

		
	# Now starts the if statements!
		
        if rpi_asks != None and comment.id not in posts_replied_to and str(comment.author) != 'RPI_Ambassador':
            print("Comment author: "+str(comment.author))
            comment_reply = message
            comment.reply(comment_reply) #Reply to the comment
            comment.upvote() #upvote the comment
            print("Replied to a comment: " +str(comment.permalink))
            posts_replied_to.append(comment.id)
            GPIO.output(BLUE_LED, True)
            print("loop finished, going to sleep now\n")
            with open("posts_replied_to.txt", "w") as f:
                for comment_id in posts_replied_to:
                    f.write(comment_id + "\n")

        if rpi_info != None and comment.id not in posts_replied_to and str(comment.author) != 'RPI_Ambassador':
            print("Comment author: "+str(comment.author))
            comment_reply = message
            comment.reply(comment_reply) #Reply to the comment
            comment.upvote() #upvote the comment
            print("Replied to a comment: " +str(comment.permalink))
            posts_replied_to.append(comment.id)
            GPIO.output(BLUE_LED, True)
            print("loop finished, going to sleep now\n")
            with open("posts_replied_to.txt", "w") as f:
                for comment_id in posts_replied_to:
                    f.write(comment_id + "\n")

        if rpi_pro != None and comment.id not in posts_replied_to and str(comment.author) != 'RPI_Ambassador':
            print("Comment author: "+str(comment.author))
            comment_reply = message
            comment.reply(comment_reply) #Reply to the comment
            comment.upvote() #upvote the comment
            print("Replied to a comment: " +str(comment.permalink))
            posts_replied_to.append(comment.id)
            GPIO.output(BLUE_LED, True)
            print("loop finished, going to sleep now\n")
            with open("posts_replied_to.txt", "w") as f:
                for comment_id in posts_replied_to:
                    f.write(comment_id + "\n")

        if project_asks != None and comment.id not in posts_replied_to and str(comment.author) != 'RPI_Ambassador':
            print("Comment author: "+str(comment.author))
            comment_reply = project_ideas_message
            comment.reply(comment_reply) #Reply to the comment
            comment.upvote() #upvote the comment
            print("Replied to a comment: " +str(comment.permalink))
            posts_replied_to.append(comment.id)
            GPIO.output(BLUE_LED, True)
            print("loop finished, going to sleep now\n")
            with open("posts_replied_to.txt", "w") as f:
                for comment_id in posts_replied_to:
                    f.write(comment_id + "\n")       
		
        if project_asks2 != None and comment.id not in posts_replied_to and str(comment.author) != 'RPI_Ambassador':
            print("Comment author: "+str(comment.author))
            comment_reply = project_ideas_message
            comment.reply(comment_reply) #Reply to the comment
            comment.upvote() #upvote the comment
            print("Replied to a comment: " +str(comment.permalink))
            posts_replied_to.append(comment.id)
            GPIO.output(BLUE_LED, True)
            print("loop finished, going to sleep now\n")
            with open("posts_replied_to.txt", "w") as f:
                for comment_id in posts_replied_to:
                    f.write(comment_id + "\n")	

        if buy_find != None and comment.id not in posts_replied_to and str(comment.author) != 'RPI_Ambassador':
            print("Comment author: "+str(comment.author))
            comment_reply = buy_zero_message
            comment.reply(comment_reply) #Reply to the comment
            comment.upvote() #upvote the comment
            print("Replied to a comment: " +str(comment.permalink))
            posts_replied_to.append(comment.id)
            GPIO.output(BLUE_LED, True)
            print("loop finished, going to sleep now\n")
            with open("posts_replied_to.txt", "w") as f:
                for comment_id in posts_replied_to:
                    f.write(comment_id + "\n")						
			
		
	else:
            print("No targets aquired today, sir!\n")

""" This is the late shift of Morty's RPI_Ambassador job, one that searches posts for RPI content """
			
def third_shift():

    print("Getting list of posts to target")
    #subreddits = r.get_subreddit('reddit_bot_test')
    subreddits = r.get_subreddit('raspberry_pi+RASPBERRY_PI_ZERO+RASPBERRY_PI_PROJECTS')        
    submissions = subreddits.get_new(limit=50)
    for submission in submissions:
        body = submission.selftext
        title = submission.title 
	changeit= submission.selftext.lower()
        changeit2= submission.title.lower()
        rpi_asks = rpi_asks_regex.search(body)
        rpi_info = rpi_asks_regex2.search(body)
        rpi_pro = rpi_asks_regex3.search(body)
        project_asks = project_ideas_regex.search(body) 
	project_asks2 = project_ideas_regex2.search(body)	
        rpi_asks2 = rpi_asks_regex.search(title)
        rpi_info2 = rpi_asks_regex2.search(title)
        rpi_pro2 = rpi_asks_regex3.search(title)
        project_asks3 = project_ideas_regex.search(title) 
	project_asks4 = project_ideas_regex2.search(title)
	buy_find = buy_find_regex.search(body)
        buy_find2 = buy_find_regex.search(title)
	post_ask = any(string in changeit for string in project_post)
	post_ask2 = any(string in changeit2 for string in project_post) 
		
        if rpi_asks != None and submission.id not in posts_replied_to:
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

        if rpi_info != None and submission.id not in posts_replied_to:
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

        if rpi_pro != None and submission.id not in posts_replied_to:
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
					
        if project_asks != None and submission.id not in posts_replied_to:
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

	if project_asks2 != None and submission.id not in posts_replied_to:
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
					
        if buy_find != None and submission.id not in posts_replied_to:
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

# The IF statements that check the submission title.					
	if rpi_asks2 != None and submission.id not in posts_replied_to:
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

        if rpi_info2 != None and submission.id not in posts_replied_to:
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

	if rpi_pro2 != None and submission.id not in posts_replied_to:
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

        if project_asks3 != None and submission.id not in posts_replied_to:
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

        if project_asks4 != None and submission.id not in posts_replied_to:
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

        if buy_find2 != None and submission.id not in posts_replied_to:
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

        if post_ask|post_ask2 and submission.id not in posts_replied_to:
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



