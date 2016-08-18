"""
Loop through data in mongodb, tagging images
"""
from __init__ import *

if __name__ == "__main__":
    api_url = 'http://139.162.195.12:5000/urbanlearning/api/v1.0/classify/'
    with Conn(database=conf.MONGO_DB,host=conf.MONGO_IP,port=conf.MONGO_PORT, collection=conf.MONGO_COL) as col:
	cursor = col.find()
    	for idx,doc in enumerate(cursor):
	    time.sleep(2)
	    print 'processing %d' %idx
	    img_id = doc['id']
	    result=requests.get(api_url+img_id).text
	    print result
	
