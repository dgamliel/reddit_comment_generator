import praw
from praw.models import MoreComments
from textblob import TextBlob


def get_data():
    #initializes an empty array to store 
    raw_text_arr = []

    #Logs into reddit through our scraping account
    reddit = praw.Reddit('bot1')


    for post in reddit.subreddit('The_Donald').hot(limit=10):      #grabs first 10 posts from "hot" tab
        for comment in post.comments:
            if isinstance(comment,MoreComments):        #ignore comments below the "read more" threshold
                break
            
            raw_score = weighted_comment_score(comment) #determines the "score" of our comment
            str_comment = TextBlob(comment.body)        #turns raw str into textblob obj
            weighted_tuple = (raw_score, str_comment)   #creates a tuple to store the weight of the textblob and the textblob itself
            raw_text_arr.append(weighted_tuple)         #creates a list of textblob objects
            
    return raw_text_arr                                 #returns a list of tuples [(score, TextBlob),...]

def comment_to_textblob(raw_text_arr):
    #Initializes empty list to contain sublists of tagged words
    textblob_arr = []

    for raw_tuple in raw_text_arr:
        score = raw_text_arr[0][0]
        print(score)
        tags = raw_tuple[1].tags
        for tag_list in tags:
            word = tag_list[0]
            part_of_speech = tag_list[1]
            return_tuple = (score, part_of_speech, word )   
            textblob_arr.append(return_tuple)

    #Note: Each sublist contains a complete t_d comment, split into tuples that contain the word and POS
    return textblob_arr

#takes parameter praw.Reddit.comment object to create a score for the comment
def weighted_comment_score(comment_obj):
    raw_score = comment_obj.score
    raw_score = raw_score/100

    return raw_score

### Testing ###
test = get_data()
test = comment_to_textblob(test)

