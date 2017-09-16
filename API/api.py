from flask import Flask, request


app = Flask(__name__)

@app.route('/extendedEssay/compute', methods=['POST'])
def create_essay():
    if not request.json or not 'title' in request.json:
        abort(400)
    '''task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)'''
    print request.json
    return request.json

if __name__ == "__main__":
    app.run()