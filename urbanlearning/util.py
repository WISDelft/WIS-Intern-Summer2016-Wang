import os
import re
import sys
import conf
import lxml
import urllib
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
	id(str): id of the image
    """
    file_path = None
    with Conn(database = conf.MONGO_DB, host=conf.MONGO_IP, port=conf.MONGO_PORT, collection=conf.MONGO_COL) as col:
	doc = col.find_one({'id':img_id})
	if doc:
	    link = doc['link']
	    page_source = requests.get(link)
	    page_source = html.fromstring(page_source.text)
	    image_path = page_source.xpath('//meta[@property="og:image"]/@content')[0]
	    image_path = image_path.split('.jpg')[0] + '.jpg'
	    file_path = conf.TEMP_PATH + img_id + '.jpg'
	    save_image(image_path, file_path)
    return file_path


def save_image(url, file_name):
    """Save image to local storage
    Args:
        url(str):url of image
    """
    u = urllib.urlopen(url)
    data = u.read()
    f = open(file_name, 'wb')
    f.close()




    
