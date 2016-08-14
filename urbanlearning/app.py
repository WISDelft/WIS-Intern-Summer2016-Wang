from __init__ import *

@app.route('/urbanlearning/api/v1.0/classify/<string:img_id>', methods=['GET'])
def classification(img_id):
    img_path = util.load_image(img_id)
    if img_path:
        img = caffe.io.load_image(img_path)
        res_net.blobs['data'].data[...] = transformer.preprocess('data', img)
        out = res_net.forward()
        top_k = res_net.blobs['prob'].data[0]
        top_k_label = top_k.flatten().argsort()[-1:-6:-1]
        top_k_prob = top_k.flatten()[0:5]
        top_k_prob = [format(i, 'f') for i in top_k_prob]
        labels = np.loadtxt(mconf.RES_LABEL, str, delimiter='\t')
        labels = labels[top_k_label].tolist()
        result = []
        for idx, label in enumerate(labels):
            instance = {}
            instance['label'] = label
	    instance['prob'] = top_k_prob[idx]
	    result.append(instance) 
        return jsonify({'status': 200, 'result':result})
    else:
	return jsonify({'status':400, 'result': 'Resource not found'})
        

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)

if __name__ == '__main__':
    app.run(host='139.162.195.12', port=5000)
