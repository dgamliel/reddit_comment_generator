class Word:

#words have the word, a part of speech definition, and a score defaulted to 1
    def __init__(self, word,pos):
        self.word = word #string
        self.pos = pos #part of speech (string)
        self.score = 1

#adds 1 to score by default, can be passed parameter for more points
    def addScore(self, point = 1): 
        self.score += 1


