import pymongo
#file setting
ORIGINAL_FILE = '/root/inst_data/inst_data'
#mongodb setting
MONGO_DB = 'instgram'
MONGO_COL = 'inst_data'
IP = '127.0.0.1'
PORT = 27017
#connect mongo
_client = pymongo.MongoClient(IP,PORT)
_db = _client[MONGO_DB]
_col = _db[MONGO_COL]
#read document by line, insert into mongo
with open(ORIGINAL_FILE) as f:
    for idx,line in enumerate(f):
	print 'processing %d' % idx
	instance = {}
	try:
            line = line.split()
	    instance['id'] = line[0]
	    instance['text'] = line[1]
	    instance['type'] = line[2]
	    instance['locationid'] = line[3]
	    instance['link'] = line[4]
	    instance['hashtags'] = line[5]
	    instance['postlang'] = line[6]
	    instance['sentiment'] = line[7]
	    _col.insert(instance)
        except IndexError:
            continue

_client.close()
