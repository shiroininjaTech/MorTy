""" This is the module for Morty's second job, The Mailman.
    It is basically a script that checks the contents of my school email account for any new email messages and
    lights a green LED if I have new mail or a red LED if there are no new messages
"""
from imapclient import IMAPClient
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GREEN_LED = 22
RED_LED = 19
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)


# Signing in and all that jazz

def initialize_mailman():

    HOSTNAME = 'imap.gmail.com'
    USERNAME = ''
    PASSWORD = ''
    MAILBOX = 'Inbox'

    NEWMAIL_OFFSET = 0 # Sets the offset for when to display that there are new messages

    server = IMAPClient(HOSTNAME, use_uid=True, ssl=True)
    server.login(USERNAME, PASSWORD) #loggiing into GMAIL

    print('Logging in as ' + USERNAME)
    select_info = server.select_folder(MAILBOX)
    print('%d messages in INBOX' % select_info['EXISTS'])

    folder_status = server.folder_status(MAILBOX, 'UNSEEN')
    newmails = int(folder_status['UNSEEN'])

    print('You have', newmails, 'new emails, boss!')

    # Turning on the LEDs

    if newmails > NEWMAIL_OFFSET:
        GPIO.output(GREEN_LED, True)
        GPIO.output(RED_LED, False)
    else:
        GPIO.output(RED_LED, True)
        GPIO.output(GREEN_LED, False)
