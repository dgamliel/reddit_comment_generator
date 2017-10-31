import praw
from praw.models import MoreComments

word_score_dict = {}

def log_and_score(word):
    if word not in word_score_dict:
        word_score_dict[word] = 1

    else:
        word_score_dict[word] += 1

def get_data():

    reddit = praw.Reddit('bot1')

    for post in reddit.subreddit('The_Donald').top():
        print (" ### POST IS ###")
        print (post.title + '\n')
        print ("--------------------------------- AND SCORE IS : " + str(post.score))
        for comment_forest in post.comments:

            if isinstance(comment_forest, MoreComments):
                continue

            if comment_forest.body == "[deleted]" or comment_forest.body == "[removed]":
                continue

            print (comment_forest.body)
            print ("\n" + "COMMENT SCORE IS : " + str(comment_forest.score))
            comment_forest = comment_forest.body


def __main__():

    get_data()

if __name__ == '__main__': __main__()
