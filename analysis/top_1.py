from __init__ import *

def top_one():
    """Top 1 annotation analysis
    """
    distribution = []
    prob = []
    with Conn(database=conf.MONGO_DB,host=conf.MONGO_IP,port=conf.MONGO_PORT) as db:
	cursor = db['annotation'].find()
	for idx, annotate in enumerate(cursor):
	    print "processing %d" % idx
            annotate = annotate['result']
	    if annotate=="Resource not found":
		continue
	    distribution.append(annotate[0]['label'])
	    prob.append(annotate[0]['prob'])
    result = Counter(distribution)
    print result.most_common()[:20]
    result = dict(result)
    json_writer(result, conf.DATA_PATH)
    avg_prob = float(sum(prob))/len(prob)
    print "average top-1 probability is %f" % avg_prob

def json_writer(json_content, path):
        '''
        @usage: export dict to json and store on local storage
        @arg: path, path to store json, string eg, 'downlaods/1.json'
        @arg: json_content, the content want to export, dictionary format
        '''
        with open(path+"top1.json", 'w') as json_file:
            json.dump(json_content, json_file, ensure_ascii = True, indent = 2)
		


if __name__=="__main__":
    top_one()
    
