import flask
from textstat.textstat import textstat

def returnComplexity(text):
	return textstat.flesch_kincaid_grade(text)

def grabSynonyms(word):
	synonyms = wordnet.synsets(word)
	return set(chain.from_iterable([word.lemma_names() for word in synonyms]))