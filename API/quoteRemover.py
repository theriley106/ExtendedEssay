import re


def replaceQuotesWith(essayText):
	quotes = []
	for i in range(essayText.count('"') / 2):
		quotes.append(essayText.split('"')[1] + '*')
	return essayText, quotes