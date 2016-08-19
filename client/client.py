"""
Loop through data in mongodb, tagging images
"""
from __init__ import *
import ast

def build_checkpoint():
    """Build checkpoint db"""
    with Conn(database=conf.MONGO_DB,host=conf.MONGO_IP,port=conf.MONGO_PORT) as db:
        if "checkpoint" in db.collection_names():
	    return True
	else:
	    print "Building checkpoint database"
	    cursor_instdata = db['inst_data'].find()
	    for idx, doc in enumerate(cursor_instdata):
		print "processing %d" % idx
		instance={}
		instance['id'] = doc['id']
		db['checkpoint'].insert_one(instance)
	
def tag(api_url):
    """Tagging image"""
    with Conn(database=conf.MONGO_DB,host=conf.MONGO_IP,port=conf.MONGO_PORT) as db:
	checkpoints = db['checkpoint'].find({}, {"_id":0,"id":1})
	for checkpoint in checkpoints:
	    result={}
	    img_url = api_url + checkpoint['id']
	    print 'processing %s' % checkpoint['id']
	    result=requests.get(img_url).text
	    try:
	    	result=ast.literal_eval(result)
		db['annotation'].insert_one(result)
	    except SyntaxError:
		db['checkpoint'].delete_one({'id':checkpoint['id']})
		continue
	    #remove current id from checkpoint
	    db['checkpoint'].delete_one({'id':checkpoint['id']})


if __name__ == "__main__":
    api_url = 'http://139.162.195.12:5000/urbanlearning/api/v1.0/classify/'
    tag(api_url)
	
