import pymongo

class Conn(object):
    def __init__(self,database,host,port,collection):
        """Initialize Connection 
	Args:
		
	"""
	self._client=pymongo.MongoClient(host,port)
	self._db=self._client[database]
	self._col=self._db[collection]
	
    def __enter__(self):
	return self._col 

    def __exit__(self,exc_type,exc_val,exc_tb):
	"""
	"""
	self._client.close()
