from Word import *
import generator
from textblob import TextBlob
### TESTING ###

'''
Test 1: Testing simple textblob methods to see format
'''

raw_data = get_data()
analyzed_data = comment_to_textblob(raw_data)

print(analyzed_data)
