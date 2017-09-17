from flask import Flask, request, render_template, request, url_for, redirect, Markup, Response
import os


app = Flask(__name__)

def doStuffToEssay(essay):
	print essay
	return essay

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

@app.route("/", methods=["POST"])
def downloadFile():
	#redirect(url_for('form'))
	values = request.form.items()
	text = values[0][1]
	essay = doStuffToEssay(text)
	return str(essay)
	'''return Response(
		'test.txt',
		mimetype="text",
		headers={"Content-disposition":
				 "attachment; filename=test.txt"})'''
	#return redirect(url_for('test'))

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8888)