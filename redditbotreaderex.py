import praw

user_agent = ("ShiroiNinja 0.1")

" Create a Reddit Instance "

r = praw.Reddit(user_agent = user_agent)

" Get A specific Subreddit "

subreddit = r.get_subreddit("japan")

""" Entering in data about what specific info you want.
    Also setting up what the output would look like.
"""

for submission in subreddit.get_hot(limit = 5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("-------------------------\n")
