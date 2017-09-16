from flask import Flask, request, render_template, request, url_for, redirect, Markup, Response
import os


app = Flask(__name__)

def doStuffToEssay(text):
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

@app.route("/downloadFile")
def downloadFile():
    os.system('hello > test.txt')
    return Response(
        'test.txt',
        mimetype="text",
        headers={"Content-disposition":
                 "attachment; filename=test.txt"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)