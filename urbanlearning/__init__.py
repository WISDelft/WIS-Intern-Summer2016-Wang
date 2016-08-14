import os
import sys
import conf
import numpy as np
import config.model_conf as mconf
import common.util as util
from flask import Flask, jsonify, make_response
sys.path.insert(0, conf.CAFFE_ROOT + 'python')
import caffe

app = Flask(__name__)

#init caffe and transformer
caffe.set_mode_cpu()
res_net = caffe.Net(mconf.RES_MODEL_FILE, mconf.RES_PRETRAINED, caffe.TEST)
transformer = caffe.io.Transformer({'data': res_net.blobs['data'].data.shape})
transformer.set_mean('data', util.load_mean(mconf.RES_MEAN_BINARY).mean(1).mean(1))
transformer.set_transpose('data', (2,0,1))
transformer.set_channel_swap('data', (2,1,0))
transformer.set_raw_scale('data', 255.0)
