from flask import Flask, request


app = Flask(__name__)

@app.route('/extendedEssay/compute', methods=['POST'])
def create_essay():
    if not request.json or not 'essay' in request.json:
       return "ERROR"
    a = str(request.json['essay'])
    return a

if __name__ == "__main__":
    app.run()