import os
import sys
import conf
import numpy as np
import config.model_conf
import common.util
from flask import Flask, jsonify
sys.path.insert(0, CAFFE_ROOT + 'python')
import caffe

app = Flask(__name__)

#init caffe and transformer
caffe.set_mode_cpu()
res_net = caffe.Net(RES_MODEL_FILE, RES_PRETRAINED, caffe.TEST)
transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_mean('data', loadmean(MEAN_BINARY).mean(1).mean(1))
transformer.set_transpose('data', (2,0,1))
transformer.set_channel_swap('data', (2,1,0))
transformer.set_raw_scale('data', 255.0)