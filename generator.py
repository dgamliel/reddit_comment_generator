import praw


'''
This strings is the "trigger"
that when found in a reddit comment
will prompt our script to reply to the comment
with the emojified text of the parent comment.
'''

phrase = "!emojify"

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

    for 

#--------------------------------------------------------

reddit = login()
