import flask
from textstat.textstat import textstat
from itertools import chain
from nltk.corpus import wordnet
import nltk
import sys
from PyDictionary import PyDictionary



def returnComplexity(text):
	return textstat.flesch_kincaid_grade(text)
