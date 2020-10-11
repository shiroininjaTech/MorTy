#!/usr/bin/python
# First off, let's import all the things!

import praw
import pdb
import re
import os
import RPi.GPIO as GPIO
from config_bot import *

# Setting up the GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GREEN_LED = 18
RED_LED = 24
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)


def rpiBot():
    
