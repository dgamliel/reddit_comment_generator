import praw
from praw.models import MoreComments

word_dict = {}

def strip_words(in_word):

    for word in word_list:
        word = ''
        for char in word:
            if char < 'A' or char > 'z':
                continue
            else:
                char = str.lower(char)
                word += char
                log_and_score(word, text_score)

    return word

def log_and_score(word, score):

    if word not in word_dict:
        word_dict[word] = score

    else:
        word_dict[word] += score

    print(word_dict)

def split_body(text_body, text_score):
    word_list = text_body.split()


def get_data():

    reddit = praw.Reddit('bot1')

    for post in reddit.subreddit('The_Donald').hot():
        print (" ### POST IS ###")
        print (post.title + '\n')
        print ("--------------------------------- AND SCORE IS : " + str(post.score))
        for comment_forest in post.comments:

            if isinstance(comment_forest, MoreComments):
                continue

            text_body = comment_forest.body
            comment_score = comment_forest.score

            if text_body == "[deleted]" or text_body == "[removed]":
                continue

            print (text_body)
            print ("\n" + "COMMENT SCORE IS : " + str(comment_score))
            split_body(text_body, comment_score)


def __main__():

    get_data()

if __name__ == '__main__': __main__()
