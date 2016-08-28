from __init__ import *

def top_one():
    """Top 1 annotation analysis
    """
    distribution = []
    prob = []
    with Conn(database=conf.MONGO_DB,host=conf.MONGO_IP,port=conf.MONGO_PORT) as db:
	cursor = db['annotation'].find({"result.0.prob":{"$gt":0.9}})
	for idx, annotate in enumerate(cursor):
	    print "processing %d" % idx
            annotate = annotate['result']
	    if annotate=="Resource not found":
		continue
	    distribution.append(annotate[0]['label'])
	    prob.append(annotate[0]['prob'])
    result = Counter(distribution)
    result = dict(result)
    proportion = {}
    topone = json_reader(conf.DATA_PATH+"top1.json")
    for k,v in result.iteritems():
	proportion[k]=v/float(topone[k])
    proportion = sorted(proportion.items(), key=operator.itemgetter(1), reverse=True)
    print proportion[0:20]
	

	



def json_writer(json_content, path):
        '''
        @usage: export dict to json and store on local storage
        @arg: path, path to store json, string eg, 'downlaods/1.json'
        @arg: json_content, the content want to export, dictionary format
        '''
        with open(path+"top1_high.json", 'w') as json_file:
            json.dump(json_content, json_file, ensure_ascii = True, indent = 2)
		
def json_reader(doc):
        """Read json
        Args:
            doc(str): json path and name
        Returns:
            content(dict): file content
        """
        with open(doc, 'r') as f:
            content = json.load(f)
        return content


if __name__=="__main__":
    top_one()
    
