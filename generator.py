import praw
import config
from praw.models import MoreComments

def login():

        '''
        Initializes a reddit instance.
        logs in by importing config.txt.

        Username, password, client_id, and client_secret are all strings.
        '''

        reddit = praw.Reddit(username = config.username,
                                 password = config.password,
                                 client_id = config.client_id,
                                 client_secret = config.client_secret,
                                             user_agent = config.user_agent)

        print ("Successfully logged into reddit" + '\n')

        return reddit #Returns a reddit instance, essentially "logs in"

def get_data():

    reddit = praw.Reddit('bot1')

    for post in reddit.subreddit('The_Donald').hot():
        for comment_forest in post.comments:
            if isinstance(comment_forest, MoreComments):
                continuecc
            print (comment_forest.body)
            comment_forest = comment_forest.body


def __main__():

    get_data()

if __name__ == '__main__': __main__()