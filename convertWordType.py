import flask
from textstat.textstat import textstat
from itertools import chain
from nltk.corpus import wordnet
import nltk
import sys
from PyDictionary import PyDictionary



def convertWordType(text):
	converted = []
	for word in text.split(' '):
		if len(word) > 3:
			try:
				if text.split(' ').count(word) > 1:
					index = text.split(' ').count(word) - str(converted).count(word)
					e = findWordType(text, word, index)
				else:
					e = findWordType(text, word)
				if 'VB' in e[0][1]:
					e = grabSynonyms(e[0][0])
				elif 'RB' in e[0][1]:
					e = grabSynonyms(e[0][0])
				else:
					e = word
			except:
				e = word
		else:
			e = word
		converted.append(e)
	return converted
