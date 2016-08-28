from __init__ import *

def overall_distribution():
    """Get overall distribution
    """
    distribution = []
    with Conn(database=conf.MONGO_DB,host=conf.MONGO_IP,port=conf.MONGO_PORT) as db:
	cursor = db['annotation'].find()
	for idx, annotate in enumerate(cursor):
	    print "processing %d" % idx
            annotate = annotate['result']
	    if annotate=="Resource not found":
		continue
	    [distribution.append(i['label']) for i in annotate]
    result = Counter(distribution)
    result = dict(result)
    json_writer(result, conf.DATA_PATH)

def json_writer(json_content, path):
        '''
        @usage: export dict to json and store on local storage
        @arg: path, path to store json, string eg, 'downlaods/1.json'
        @arg: json_content, the content want to export, dictionary format
        '''
        with open(path+"overall.json", 'w') as json_file:
            json.dump(json_content, json_file, ensure_ascii = True, indent = 2)
		


if __name__=="__main__":
    overall_distribution()
	    
