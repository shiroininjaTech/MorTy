from __future__ import unicode_literals

""" This is the Module for Morty's stellar job, an Astronaut! What this module provides are functions for the 
    scraping of data from the websites of various space agencies for information in regards to spaceflight 
    launches. Morty will notify me via LED flashes when there is a space launch schedule today.  
"""

""" Version 1.0
    Modified: 04/07/16
"""

import re
import requests, bs4
import time, os
from datetime import date
import calendar
from dateutil import parser
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

my_date = date.today()

# The function to blink the LEDs

def blinky():

    GPIO.output(27, True)
    time.sleep(0.50)
    GPIO.output(27, False)
    time.sleep(0.40)
    GPIO.output(22, True) 
    time.sleep(0.50)
    GPIO.output(22, False)
    time.sleep(0.50)
    GPIO.output(27, True) 
    time.sleep(0.50)
    GPIO.output(27, False)
    time.sleep(0.50)
    GPIO.output(22, True)
    time.sleep(0.50)
    GPIO.output(22, False)
    time.sleep(0.50)
    GPIO.output(27, True)
    time.sleep(0.50)
    GPIO.output(27, False)
    time.sleep(0.50)
    GPIO.output(22, True)
    time.sleep(0.50)
    GPIO.output(22, False)
    time.sleep(0.50)
    GPIO.output(27, True)
    time.sleep(0.50)
    GPIO.output(27, False)
    time.sleep(0.50)
    GPIO.output(22, True)
    time.sleep(0.50)
    GPIO.output(22, False)
    time.sleep(0.50)



# The function to search NASA's launch times.

def armStrong():

    print('Are we going to space today boss? Lets see...')
    spaceFlight = requests.get('https://spaceflightnow.com/launch-schedule/')
    spaceFlight.raise_for_status()
    
    # Now that we have the website loaded, let's parse it with Beautiful Soup (Why can't it be ugly soup?) 

    flyingSoup = bs4.BeautifulSoup(spaceFlight.text)
    flyDates = flyingSoup.select('span[class="launchdate"]')
    flyDates2 = flyDates[0].getText()
    
    # We've scraped the date from the website, now let's convert it to computer speak.

    dateChange = parser.parse(flyDates2)

    # Changing the date objects to strings because computers are stupid.   
    changedateStr = str(dateChange)
    changedSlice = changedateStr[0:10]
    todaydateStr = str(my_date)

    # Does the launch date match today's date?
    if todaydateStr == changedSlice:
       print('To infinity and Beyond!')
       blinky()
       # TO-DO: scrap mission description and display/email it to me

    elif todaydateStr != changedSlice:
       print('Keeping our feet on the ground today, boss!')
       # TO-DO: scrap mission description and display/email it to me

    else:
        print('Somethings broken!')



