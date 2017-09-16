import flask
from textstat.textstat import textstat
from itertools import chain
from nltk.corpus import wordnet
import nltk
import sys
from PyDictionary import PyDictionary

if __name__ == "__main__":
	if 'debug' in str(sys.argv):
		text = raw_input("Input text: ")
		print convertWordType(text)
	'''for word in text.split(' '):
		e = grabSynonyms(word)
		if e != None:
			a.append(e)
		else:
			a.append(word)
	print ' '.join(a)'''




#Cognitive services api collection

# Quote rejection
