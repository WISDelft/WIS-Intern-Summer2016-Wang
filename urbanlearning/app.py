from __init__ import *

@app.route('/urbanlearning/api/v1.0/classify/<str:id>', methods=['GET'])
def classification(id):
    
    pass

@app.route('/urbanlearning/api/v1.0/detection', methods=['GET'])
def detection():
    pass

if __name__ == '__main__':
    app.run(debug = True)
