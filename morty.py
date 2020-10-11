#!/usr/bin/python3

""" This is the Source script for the  MorTy Personal Assistant Bot Version 2.0. Version 2.0 introduced Interaction and activation of 
    Modules via tactile switch and introduced a Backlighting function. Version 3.0 introduced Motion Detection!
    Version 3.5 brought light detection via a light sensor and a move to MorTy's new home.
    Version 3.6 brought the a minor change to how MorTy recieves the date from the OS to prevent the need for reboot.

"""

""" Version 3.6
    Modified 07/31/17
    Written By: Thomas Mullins
"""
# Import all the things!

import praw
import pdb
import re
import os
import time
from config_bot import *
import RPi.GPIO as GPIO
import traceback
# Setting up all the GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# For the Light sensor

GPIO.setup(4, GPIO.IN) 

# For the Motion sensor

PIR_PIN=26
GPIO.setup(PIR_PIN, GPIO.IN)


# Checking for Morty's paperwork for his first job

if not os.path.isfile("/home/pi/Documents/PythonFiles/MorTy/config_bot.py"):
    print("Boss did you fill out the proper paperwork?\n")
    exit(1)




if __name__ == '__main__':

    try:
        print('Press Ctrl-C to quit.')

        while True:

            # Finishing Set up for the switches
            input_state = GPIO.input(18)
            input_state2 = GPIO.input(21)
            input_state3 = GPIO.input(25)
            input_state4 = GPIO.input(23)

            # With v3.5 came sound detection, if clapping is detected, then run cable guy
            if input_state3 == False :
                print('Initializing Cable Guy Job!')
                GPIO.output(27, True)
                import cable_guy
                cable_guy.larry()
                time.sleep(0.2)
                GPIO.output(27, False)
                time.sleep(0.2)

            # If Motion is detected, Astronaut is run
            #if GPIO.input(PIR_PIN):
                #print('Astronaut Initialized!')
                #GPIO.output(22, True)
                #import astronaut
                #astronaut.armStrong()
                #time.sleep(0.2)
                #GPIO.output(22, False)
                #time.sleep(0.2)
            
            # If Button 2 is pressed, MorTy is rebooted
            if input_state2 == False:
                os.system('sudo shutdown -r now')

            # If Light isn't detected, turn on the ambient lights 
            if GPIO.input(4) == GPIO.HIGH:
                print('Ambient Light on!')
                GPIO.output(13, True)
                GPIO.output(19, True)
                time.sleep(0.2)
                

                # If Light is detected, turn ambient lights off.
            if GPIO.input(4) == GPIO.LOW:
                GPIO.output(13, False)
                GPIO.output(19, False)
                time.sleep(0.2)





    except:
         errorFile = open('MortysHealth.txt', 'w')
         errorFile.write(traceback.format_exc())
         errorFile.close()
         print('The traceback info was written to MortysHealth.txt')
    finally:
        GPIO.cleanup()

