import pymongo

class Conn(object):
    def __init__(self,database,host,port,collection):
        """Initialize Connection"""
	self._client=pymongo.MongoClient(host,port)
	self._db=self._client[database]
	self._col=self._db[collection]
	
    def __enter__(self):
	"""Get collection instance"""
	return self._col 

    def __exit__(self,exc_type,exc_val,exc_tb):
	"""Shutdown connection"""
	self._client.close()
