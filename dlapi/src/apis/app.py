#flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'label': 'cat',
        'prob': 0.97
    },
    {
        'id': 2,
        'label': 'tiger',
        'prob': 0.63
    }
]

@app.route('/apis/caffe/v0.1/classify', methods=['GET'])
def get_tasks():
    return jsonify({'classify': tasks})

if __name__ =='__main__':
    app.run(host='139.162.195.12',port=5000)
