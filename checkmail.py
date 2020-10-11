#!/usr/bin/python

from imapclient import IMAPClient
import time

import RPi.GPIO as GPIO

DEBUG = True

HOSTNAME = 'imap.gmail.com'
USERNAME = ''
PASSWORD = ''
MAILBOX = 'Inbox'

NEWMAIL_OFFSET = 0 # my unread messages never goes to zero, yours might
MAIL_CHECK_FREQ = 60 # check mail every 60 seconds

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GREEN_LED = 22
RED_LED = 19
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)

output = False

def loop():
   server = IMAPClient(HOSTNAME, use_uid=True, ssl=True)
   server.login(USERNAME, PASSWORD)

   if DEBUG:
      print('Logging in as ' + USERNAME)
      select_info = server.select_folder(MAILBOX)
      print('%d messages in INBOX' % select_info['EXISTS'])

   folder_status = server.folder_status(MAILBOX, 'UNSEEN')
   newmails = int(folder_status['UNSEEN'])


   if DEBUG:
      print "You have", newmails, "new emails!"

   if newmails > NEWMAIL_OFFSET:
      output = True
   elif newmails == NEWMAIL_OFFSET:
      output = False


   time.sleep(MAIL_CHECK_FREQ)
if __name__ == '__main__':

    try:
       print 'Press Ctrl-C to quit.'
       while True:
         loop()
    finally:
       GPIO.cleanup()
