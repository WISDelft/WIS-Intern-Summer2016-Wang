import pymongo

class Conn(object):
    def __init__(self,database,host,port):
        """Initialize Connection"""
	self._client=pymongo.MongoClient(host,port)
	self._db=self._client[database]
	
    def __enter__(self):
	"""Get collection instance"""
	return self._db

    def __exit__(self,exc_type,exc_val,exc_tb):
	"""Shutdown connection"""
	self._client.close()
