import praw
from praw.models import MoreComments

def log_and_score(word, score):
    word_score_dict = {}

    if word not in word_score_dict:
        word_score_dict[word] = score

    else:
        word_score_dict[word] += score

    print(word_score_dict)

def split_body(text_body, text_score):
    word_list = text_body.split()

    for word in word_list:
        word = ''
        for char in word:
            if char < 'A' or char > 'z':
                continue
            else:
                char = str.lower(char)
                word += char
                log_and_score(word, text_score)



def get_data():

    reddit = praw.Reddit('bot1')

    for post in reddit.subreddit('The_Donald').hot():
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
            split_body(comment_forest.body, comment_forest.score)


def __main__():

    get_data()

if __name__ == '__main__': __main__()
