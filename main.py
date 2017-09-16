import flask
from textstat.textstat import textstat
from itertools import chain
from nltk.corpus import wordnet
import nltk
import sys
from PyDictionary import PyDictionary 


def returnComplexity(text):
	return textstat.flesch_kincaid_grade(text)

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
def findWordType(text, word, index=0):
	text = nltk.word_tokenize(text)
	result = nltk.pos_tag(text)
	result = [i for i in result if i[index].lower() == word]
	return result

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