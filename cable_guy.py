""" This is the Module for Morty's 3rd full time job. He only works at this job 3 times a week. This script
    searches for my favourite youtube channel, gets the list of videos uploaded, and only downloads the newest
    submission.
"""


# Importing the things needed for the job

from __future__ import unicode_literals
import youtube_dl
import time
import os
from datetime import date
import calendar
import morty

# Setting up work schedule
my_date = date.today()
day_week = calendar.day_name[my_date.weekday()]
gimmeABreakMan = ['Wednesday']
breakDay  = any(string in day_week for string in gimmeABreakMan)
linux_day = ['Friday']
sabbath = any(string in day_week for string in linux_day)
piggles_day = ['Tuesday']
piggles = any(string in day_week for string in piggles_day)
flake_day = ['Monday']
flakeman = any(string in day_week for string in flake_day)
german_day = ['Sunday']
german = any(string in day_week for string in german_day)

def larry():

    if flakeman:

        print("------------------------------------------------------")
        print("Is it that time already? Going to get your favourite shows, boss!")
        print("------------------------------------------------------")
        YDLOptions={
            # Provide any options to YDL you want here, see
            # https://github.com/rg3/youtube-dl/blob/master/youtube_dl/YoutubeDL.py#L117-L265
            #for options
            'playlist_items':'1,2,3,4,5'
}

        with youtube_dl.YoutubeDL(YDLOptions) as ydl:
            ydl.download(['https://www.youtube.com/user/Gimmeaflakeman/videos'])




    if german:

        print("------------------------------------------------------")
        print("Is it that time already? Going to get your favourite shows, boss!")
        print("------------------------------------------------------")
        YDLOptions={
            # Provide any options to YDL you want here, see
            # https://github.com/rg3/youtube-dl/blob/master/youtube_dl/YoutubeDL.py#L117-L265
            #for options
            'playlist_items':'1,2,3,4,5'
 }

        with youtube_dl.YoutubeDL(YDLOptions) as ydl:
            ydl.download(['https://www.youtube.com/channel/UCNnv7-2ypvF6z8zJuR-3clg/videos?flow=grid&view=0&sort=dd'])


    if breakDay:

        print("------------------------------------------------------")
        print("Is it that time already? Going to get your favourite shows, boss!")
        print("------------------------------------------------------")
        YDLOptions={
            # Provide any options to YDL you want here, see
            # https://github.com/rg3/youtube-dl/blob/master/youtube_dl/YoutubeDL.py#L117-L265
            #for options
            'playlist_items':'1,2,3,4,5'

}

        with youtube_dl.YoutubeDL(YDLOptions) as ydl:
            ydl.download(['https://www.youtube.com/user/Gimmeabreakman/videos?sort=dd&view=0&flow=grid'])


    if sabbath:

        print("------------------------------------------------------")
        print("Is it that time already? Going to get your favourite shows, boss!")
        print("------------------------------------------------------")
        YDLOptions={
            # Provide any options to YDL you want here, see
            # https://github.com/rg3/youtube-dl/blob/master/youtube_dl/YoutubeDL.py#L117-L265
            #for options
            'playlist_items':'1,2,3,4,5,6,7'

}

        with youtube_dl.YoutubeDL(YDLOptions) as ydl:
            ydl.download(['https://www.youtube.com/user/LinusTechTips/videos'])


  
    else:
        print("\nNot working as a cable guy today!\n")
    
    return
