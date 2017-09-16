import flask
from textstat.textstat import textstat
from itertools import chain
from nltk.corpus import wordnet
import nltk
import sys
import re
from PyDictionary import PyDictionary


def replaceQuotesWith(essayText,replacementText):
    string = re.sub(r"([\"'])(?:(?=(\\?))\2.)*?\1", replacementText, essayText)
    return string
