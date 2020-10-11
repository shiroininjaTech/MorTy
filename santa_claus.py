""" This is the module for Morty's job for the holiday season. It basically searches reddit comments for holiday
    related phrases and blinks a pattern of LEDs if it finds the phrase.
"""


import praw
import pdb
import re
import os
from config_bot import *
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GREEN_LED = 23
RED_LED2 = 18
GREEN_LED2 = 21 
RED_LED3 = 12
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED2, GPIO.OUT)
GPIO.setup(GREEN_LED2, GPIO.OUT)
GPIO.setup(RED_LED3, GPIO.OUT)


# The variables for the module
user_agent = ' '
r = ' '
question = ['merry christmas!', 'merry christmas', 'happy holidays', 'i love christmas']


# Punching in. Creating a Reddit instance 

def put_on_santa_outfit():
   global user_agent
   global r
   user_agent = ("Santa Claus 0.1")
   r = praw.Reddit(user_agent=user_agent)

   print("Harnessing raindeer")
   r.login(REDDIT_USERNAME, REDDIT_PASS, disable_warning=True)


   return

# The blinking functions

def blink4():
    GPIO.output(GREEN_LED2, True)
    time.sleep(0.40)
    GPIO.output(GREEN_LED2, False)
    time.sleep(0.40)
    GPIO.output(GREEN_LED2, True)
    time.sleep(0.40)
    GPIO.output(GREEN_LED2, False)
    time.sleep(0.40)
    GPIO.output(RED_LED3, True)
    time.sleep(0.40)
    GPIO.output(RED_LED3, False)
    time.sleep(0.40)
    GPIO.output(GREEN_LED2, True)
    time.sleep(0.40)
    GPIO.output(GREEN_LED2, False)
    time.sleep(0.40)
    GPIO.output(GREEN_LED2, True)
    time.sleep(0.40)
    GPIO.output(GREEN_LED2, False)
    time.sleep(0.40)
    GPIO.output(RED_LED3, True)
    time.sleep(0.40)
    GPIO.output(RED_LED3, False)
    time.sleep(0.40)
    GPIO.output(GREEN_LED2, True)
    time.sleep(0.40)
    GPIO.output(GREEN_LED2, False)
    time.sleep(0.40)
    GPIO.output(RED_LED3, True)
    time.sleep(0.40)
    GPIO.output(RED_LED3, False)
    time.sleep(0.40)
    GPIO.output(GREEN_LED, True)
    time.sleep(0.40)
    GPIO.output(GREEN_LED, False)
    time.sleep(0.40)
    GPIO.output(RED_LED2, True)
    time.sleep(0.40)
    GPIO.output(RED_LED2, False)
    time.sleep(0.40)
    GPIO.output(GREEN_LED2, True)
    time.sleep(0.40)
    GPIO.output(GREEN_LED2, False)
    time.sleep(0.40)




def blink():


    GPIO.output(RED_LED2, True)
    GPIO.output(GREEN_LED, True)
    time.sleep(0.40)
    GPIO.output(RED_LED2, False)
    GPIO.output(GREEN_LED,False)
    time.sleep(0.40)
    GPIO.output(RED_LED2, True)
    GPIO.output(GREEN_LED, True)
    time.sleep(0.40)
    GPIO.output(RED_LED2, False)
    GPIO.output(GREEN_LED,False)
    time.sleep(0.40)
    GPIO.output(RED_LED2, True)
    GPIO.output(GREEN_LED, True)
    time.sleep(0.40)
    GPIO.output(RED_LED2, False)
    GPIO.output(GREEN_LED,False)
    time.sleep(0.40)

def blink2():

    GPIO.output(RED_LED3, True)
    GPIO.output(GREEN_LED2, True)
    time.sleep(0.40)
    GPIO.output(RED_LED3, False)
    GPIO.output(GREEN_LED2,False)
    time.sleep(0.40)
    GPIO.output(RED_LED3, True)
    GPIO.output(GREEN_LED2, True)
    time.sleep(0.40)
    GPIO.output(RED_LED3, False)
    GPIO.output(GREEN_LED2,False)
    time.sleep(0.40)
    GPIO.output(RED_LED3, True)
    GPIO.output(GREEN_LED2, True)
    time.sleep(0.40)
    GPIO.output(RED_LED3, False)
    GPIO.output(GREEN_LED2,False)
    time.sleep(0.40)

def blink3():

    GPIO.output(GREEN_LED2, True)
    time.sleep(0.40)
    GPIO.output(GREEN_LED2, False)
    time.sleep(0.40)
    GPIO.output(RED_LED3, True)
    time.sleep(0.40)
    GPIO.output(RED_LED3, False)
    time.sleep(0.40)
    GPIO.output(GREEN_LED2, True)
    time.sleep(0.40)
    GPIO.output(GREEN_LED2, False)
    time.sleep(0.40)
    GPIO.output(GREEN_LED, True)
    time.sleep(0.40)
    GPIO.output(GREEN_LED, False)
    time.sleep(0.40)
    GPIO.output(RED_LED2, True)
    time.sleep(0.40)
    GPIO.output(RED_LED2, False)
    time.sleep(0.40)

# The main bulk of the santa_claus module

def on_dancer_on_prancer():
    print("checking naughty list...")
    subreddit = r.get_subreddit('all')
    all_comments = subreddit.get_comments(limit=500)
    for comment in all_comments:
        changeup = str(comment).lower()
        isjolly = any(string in changeup for string in question)
        if isjolly :
            print("looks like we've found a good boy or girl!")
            blink4()
            blink4()
        else:
            print("nothing but bad children!")


