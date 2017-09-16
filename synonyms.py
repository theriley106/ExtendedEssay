import flask
from textstat.textstat import textstat
from itertools import chain
from nltk.corpus import wordnet
import nltk
import sys
from PyDictionary import PyDictionary



def grabSynonyms(word, typ=None):
	if typ == None:
		synonyms = wordnet.synsets(word)
		a = set(chain.from_iterable([word.lemma_names() for word in synonyms]))
		#return a
		if len(list(a)) > 1:
			return list(a)[0]
	else:
		syns = wordnet.synsets(word)
		for i in syns:
			text = i.examples()
			a = findWordType(text, word)
			if str(typ) in str(a):
				return word
				print 'did it'
	return word
