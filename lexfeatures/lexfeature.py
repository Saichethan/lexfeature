


"""
author: Saichethan M. Reddy
date: 02/06/2020
"""

class encoder:
	def __init__(self, sentence):
		self.sentence = sentence
	def encode(self):
		low = self.sentence.split(" ") #list of words
		now = len(low) #no of words
		output = []

		wordlen = [len(w) for w in low]
		maxlen = max(wordlen)
		minlen = min(wordlen)

		for i in range(now):
			word = []

			#first word?
			if i is 0:
				word.append(1)
			else:
				word.append(0)

			#last word?
			if i is now-1:
				word.append(1)
			else:
				word.append(0)

			#is lower cased?
			if low[i].islower():
				word.append(1)
			else:
				word.append(0)

			#is upper cased?	
			if low[i].isupper():
				word.append(1)
			else:
				word.append(0)

			#is title cased?
			if low[i].istitle():
				word.append(1)
			else:
				word.append(0)

			#any digit present?
			if any(x.isdigit() for x in str(low[i])):
				word.append(1)
			else:
				word.append(0)

			#all alpha numeric?
			if low[i].isalnum():
				word.append(1)
			else:
				word.append(0)

			#word len is max?
			if len(low[i]) is maxlen:
				word.append(1)
			else:
				word.append(0)

			#word len is min?
			if len(low[i]) is minlen:
				word.append(1)
			else:
				word.append(0)

			output.append(word)

		return output


