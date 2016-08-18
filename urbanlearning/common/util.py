import os
import re
import sys
import conf
import lxml
import shutil
import requests
import numpy as np
from lxml import html
from conn import Conn
sys.path.insert(0, conf.CAFFE_ROOT + 'python')
import caffe

def load_mean(file_path):
    """Load model mean binary file
    Args:
	file_path(str): mean binary file path
    Return:
	mean(ndarray): numpy array
    """
    proto_data = open(file_path, "rb").read()
    a = caffe.io.caffe_pb2.BlobProto.FromString(proto_data)
    mean  = caffe.io.blobproto_to_array(a)[0]
    return mean

def load_image(img_id):
    """Load image by id, save to temp
    Args:
	img_id(str): id of the image
    Return:
	img_path(str): image path of current image to be classify/detect)
    """
    file_path = None
    with Conn(database = conf.MONGO_DB, host=conf.MONGO_IP, port=conf.MONGO_PORT, collection=conf.MONGO_COL) as col:
	doc = col.find_one({'id':img_id})
	if doc:
	    link = doc['link']
	    try:
	    	page_source = requests.get(link)
	    	page_source = html.fromstring(page_source.text)
	    	image_path = page_source.xpath('//meta[@property="og:image"]/@content')[0]
	    	image_path = image_path.split('.jpg')[0] + '.jpg'
	    	file_path = conf.TEMP_PATH + img_id + '.jpg'
	    	save_image(image_path, file_path)
	    except IndexError:
		file_path = None
    return file_path


def save_image(url, file_name):
    """Save image to local storage
    Args:
        url(str):url of image
	file_name(str): storage path with file name
    """
    response = requests.get(url, stream = True)
    with open(file_name, 'wb') as out:
	shutil.copyfileobj(response.raw, out)
    del response

def get_labels(out, label_path):
    """Get top k label of predicted result
    """
    out_prob = out['prob'][0]
    top_k_label = out_prob.argsort()[::-1][:5]
    labels = np.loadtxt(label_path, str, delimiter='\t')
    labels = labels[top_k_label].tolist()
    return labels

def get_probs(out):
    """Get top k prob of predicted result
    """
    out_prob = out['prob'][0]
    top_k_prob = out_prob.argsort()[::-1][:5]
    probs = out_prob[top_k_prob]
    probs = [float(prob) for prob in probs]
    return probs

def get_label_prob_pairs(labels, probs):
    """Get label probability pair
    """
    res = []
    for idx, label in enumerate(labels):
	instance = {}
	instance['label'] = label
	instance['prob'] = probs[idx]
        res.append(instance)
    return res

def init_caffe(model, pretrained,binary):
    """Initialize caffe
    """
    caffe.set_mode_cpu()
    res_net = caffe.Net(model,pretrained,caffe.TEST)
    transformer = caffe.io.Transformer({'data':res_net.blobs['data'].data.shape})
    transformer.set_mean('data', load_mean(binary).mean(1).mean(1))
    transformer.set_transpose('data',(2,0,1))
    transformer.set_channel_swap('data',(2,1,0))
    transformer.set_raw_scale('data',255.0)
    return res_net, transformer


    
