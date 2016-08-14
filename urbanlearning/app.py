from __init__ import *

@app.route('/urbanlearning/api/v1.0/classify/<string:img_id>', methods=['GET'])
def classification(img_id):
    img_path = util.load_image(img_id)
    img = caffe.io.load_image(img_path)
    res_net.blobs['data'].data[...] = transformer.preprocess('data', img)
    out = res_net.forward()
    top_k = res_net.blobs['prob'].data[0].flatten().argsort()[-1:-6:-1]
    labels = np.loadtxt(mconf.RES_LABEL, str, delimiter='\t')
    labels = labels[top_k].tolist()
    return jsonify({'labels':labels})

if __name__ == '__main__':
    app.run(host='139.162.195.12', port=5000)
