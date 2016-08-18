MODEL_PATH = '/root/caffe/caffe/models/'
#Res Net
RES_MEAN_BINARY = MODEL_PATH + 'res_net/ResNet_mean.binaryproto'
RES_MODEL_FILE = MODEL_PATH + 'res_net/ResNet-152-deploy.prototxt'
RES_PRETRAINED = MODEL_PATH + 'res_net/ResNet-152-model.caffemodel'
RES_LABEL = '/root/caffe/caffe/data/ilsvrc12/synset_words.txt'
#GoogleNet
GOO_MEAN_BINARY = MODEL_PATH + 'places205_cnn/places205CNN_mean.binaryproto'
GOO_MODEL_FILE = MODEL_PATH + 'googlenet_places205/deploy_places205.protxt'
GOO_PRETRAINED = MODEL_PATH + 'googlenet_places205/googlelet_places205_train_iter_2400000.caffemodel'
GOO_LABEL = MODEL_PATH + 'places205_cnn/categoryIndex_places205.csv'
