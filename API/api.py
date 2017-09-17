#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, request, url_for, redirect, Markup, Response
import os
import time
import inflect
import random
import contractions
from states import *
import enchant
import re
import requests
from quoteRemover import *

app = Flask(__name__)

def doStuffToEssay(essay, punc=None, acr=None, spel=None, verb=None, proc=None):
	essay, quotes = replaceQuotesWith(essay)
	essay = convertAllNum(essay)
	essay = contractions.fix(essay)
	essay = convertStates(essay)
	Accuracy = spellCheck(essay)
	for q in quotes:
		essay.partition('*')[0] + str(q) + essay.partition('*')[2]
	a = str(random.randint(1000000000, 9999999999)) + '.txt'
	filez = "{}/static/{}".format(os.getcwd(), a)
	os.system('touch {}'.format(filez))
	file = open(filez, "w")
	file.write(essay)
	file.close()
	return essay

def get_num(x):
    return int(''.join(ele for ele in x if ele.isdigit()))

def bloombergVar(stock="AAPL"):
	a = requests.Session()
	a.get("https://www.bloomberg.com/quote/{}:US".format(stock), headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
	return get_num(str(a.get('https://www.bloomberg.com/markets/api/bulk-time-series/price/AAPL%3AUS?timeFrame=1_MONTH').json()))

def pnyMellon():
	url = 'https://web.bnymellonwealthmanagement.com/login/forms/login.fcc?id=1'
	a = requests.Session()
	a.get(url, headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
	return get_num(str(a.cookies))

def itgDev():
	url = 'https://itg-library.bluematrix.com/client/login.jsp'
	a = requests.Session()
	a.get(url, headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
	return get_num(str(a.cookies))

def chaseGet():
	#Runs regex on Cookie from auth screen
	url = 'https://chaseonline.chase.com/Public/ReIdentify/ReidentifyFilterView.aspx?COLLogon'
	a = requests.Session()
	a.get(url, headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
	return get_num(str(a.cookies))

def dattoGet():
	#Getting cookie from login screen
	url = 'https://auth.datto.com/login'
	a = requests.Session()
	a.get(url, headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
	return get_num(str(a.cookies))

def capOne():
	#From university login screen regex out numerical value
	url = 'https://verified.capitalone.com/enrollment-api/orchlayer/enrollment/content?lang=en_US'
	a = requests.Session()
	a.get(url, headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac O X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
	return get_num(str(a.cookies))

def mathWorks():
	url = 'https://www.mathworks.com/search/site_search.html?c%5B%5D=entire_site'
	a = requests.Session()
	a.get(url, headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac O X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
	return get_num(str(a.cookies))

def twoSigma():
	# Grabbed from data vendors cookie - regexed out the numerical values
	url = 'https://www.twosigma.com/contact/data-vendors'
	a = requests.Session()
	a.get(url, headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac O X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
	return get_num(str(a.cookies))

def myLutron():
	# Lutron authenication page
	url = 'https://umslogin.lutron.com/Account/Login?ReturnUrl=%2F%3Fwa%3Dwsignin1.0%26wtrealm%3Dhttps%253a%252f%252fwww.lutron.com%252f_trust%252fdefault.aspx%26wctx%3Dhttp%253a%252f%252fwww.lutron.com%252fen-US%252f_layouts%252fauthenticate.aspx%253fSource%253d%252fen-US%252f_layouts%252fmyLutron%252fForms%252fHomePageRedirect.aspx'
	a = requests.Session()
	a.get(url, headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac O X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
	return get_num(str(a.cookies))

def oracle():
	# regex numerical digits in cookie from oracle
	url = 'https://login.oracle.com/mysso/signon.jsp'
	a = requests.Session()
	a.post(url, headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac O X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
	return get_num(str(a.cookies))

def getTech():
	url = 'http://get.tech/assets/utm-ss.js'
	a = requests.Session()
	a.post(url, headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac O X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
	return get_num(str(a.cookies))

def soylent():
	url = 'https://www.soylent.com/'
	a = requests.Session()
	a.post(url, headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac O X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
	return get_num(str(a.cookies))

def wayFair():
	e = []
	for i in range(10):
		e.append(random.choice([chr(i) for i in range(ord('a'),ord('z')+1)]))
	url = 'https://www.wayfair.com/keyword.php?keyword={}&command=dosearch&new_keyword_search=true'.format(''.join(e))
	a = requests.Session()
	a.post(url, headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac O X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
	return get_num(str(a.cookies))

def deshaw():
	url = 'https://www.deshaw.com/irweb/css/reset.css?appStartTime='
	a = requests.Session()
	a.post(url, headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac O X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
	return get_num(str(a.cookies))

def makeSchool():
	url = 'https://www.makeschool.com/apply'
	a = requests.Session()
	a.post(url, headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac O X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
	return get_num(str(a.cookies))

def qualtrics():
	# Quantifying the x-host id on the qualtrics templates page
	url = 'https://www.qualtrics.com/support/wp-content/themes/qualtrics/templates/main.html?v=1.2'
	a = requests.Session()
	a = a.get(url, headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac O X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
	return get_num(str(a.text))


#def genRandomVal(numval, numapi):



def convertPunctuation(text):
	puntuation = ["?", "!", "."]
	for p in puntuation:
		text = text.replace(p, '{} '.format(p))
	return text

def convertStates(text):
	a = []
	for stri in text.split(' '):
		try:
			e = states[stri.upper()]
			a.append(e)
		except Exception as exp:
			a.append(stri)
	return ' '.join(a)

def spellCheck(text):
	inwords = []
	d = enchant.Dict("en_US")
	for word in text.split(' '):
		try:
			if d.check(word) == False:
				inwords.append(word)
		except:
			pass
	return (float(len(inwords)) / float(len(text.split(' ')))) * 100


def convertAllNum(text):
	a = []
	for stri in text.split(' '):
		strc = stri.replace(',', '')
		try:
			e = int(strc)
			e = numToWord(e)
		except Exception as exp:
			e = str(stri)
		a.append(e)
	return ' '.join(a)

def countNumberOf(text, char):
	return test.count(char)

def numToWord(num):
	p = inflect.engine()
	return p.number_to_words(num)

def returnRandomValues(startval, endval, amount):
	if (endval - startval) > amount:
		return None
	a = []
	while a < amount:
		value = random.randint(startval, endval)
		if value not in a:
			a.append(value)
	return a

@app.route('/')
def form():
	return render_template('index.html')

@app.route('/extendedEssay/compute', methods=['POST'])
def create_essay():
	if not request.json or not 'essay' in request.json:
	   return None
	text = str(request.json['essay']).replace("hello", "goodbye")
	return doStuffToEssay(text)



@app.route('/test')
def test():
	return "Test"


@app.route('/fileDownloading/<filet>')
def fileDownloading(filet, download=False):
	#this returns the file as a text
	try:
		file = "{}/static/{}.txt".format(os.getcwd(), filet)
		f = open(file,'r')
		if download == False:
			return f
		else:
			return Response(
			file,
			mimetype="text",
			headers={"Content-disposition":
					 "attachment; filename={}".format(filename)})
	except:
		return None

@app.route("/", methods=["POST"])
def downloadFile():
	#redirect(url_for('form'))
	values = request.form.items()
	text = values[0][1]
	essay = doStuffToEssay(text)
	time.sleep(2.8)
	return str(essay)
	'''return Response(
		'test.txt',
		mimetype="text",
		headers={"Content-disposition":
				 "attachment; filename=test.txt"})'''
	#return redirect(url_for('test'))

if __name__ == "__main__":
	'''print bloombergVar()
	print pnyMellon()
	print capOne()
	print mathWorks()
	print twoSigma()
	print myLutron()
	print oracle()'''
	#print wayFair()
	#print deshaw()
	#print makeSchool()
	#print qualtrics()
	#print soylent()
	print getTech()
	app.run(host='0.0.0.0', port=8888)