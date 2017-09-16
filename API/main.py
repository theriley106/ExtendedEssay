import flask
from textstat.textstat import textstat

def returnComplexity(text):
	return textstat.flesch_kincaid_grade(text)

