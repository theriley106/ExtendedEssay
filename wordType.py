import flask
from textstat.textstat import textstat
from itertools import chain
from nltk.corpus import wordnet
import nltk
import sys
from PyDictionary import PyDictionary


def findWordType(text, word, index=0):
	text = nltk.word_tokenize(text)
	result = nltk.pos_tag(text)
	result = [i for i in result if i[index].lower() == word]
	return result
