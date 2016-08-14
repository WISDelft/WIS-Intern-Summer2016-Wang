import pymongo

ORIGINAL_FILE = '/root/inst_data/inst_post'
#db setting
MONGO_DB = 'instgram'
MONGO_COL = 'inst_post'
IP = '127.0.0.1'
PORT = 27017
#
_client = pymongo.MongoClient(IP,PORT)
_db = _client[MONGO_DB]
_col = _db[MONGO_COL]
#
with open(ORIGINAL_FILE) as f:
    for idx, line in enumerate(f):
	print 'processing %d' idx
	instance = {}
	try:
	    line = line.split()
	    instance['id'] = line[0]
	    instance['userid'] = line[1]
	    instance['latitude'] = line[2]
	    instance['langitude'] = line[3]
	    instance['createdat'] = line[4]
	    instance['pathid'] = line[5]
	    _col.insert(instance)
	except IndexError:
	    continue

_client.close()
