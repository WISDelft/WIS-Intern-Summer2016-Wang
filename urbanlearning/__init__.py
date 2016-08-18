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
res_net, transformer = util.init_caffe(mconf.RES_MODEL_FILE, mconf.RES_PRETRAINED,mconf.RES_MEAN_BINARY)
goo_net, transformer_goo = util.init_caffe(mconf.GOO_MODEL_FILE, mconf.GOO_PRETRAINED, mconf.GOO_MEAN_BINARY)
