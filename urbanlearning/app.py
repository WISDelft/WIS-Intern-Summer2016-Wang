from __init__ import *

@app.route('/urbanlearning/api/v1.0/classify/<string:img_id>', methods=['GET'])
def classification(img_id):
    img_path = util.load_image(img_id)
    if img_path:
        img = caffe.io.load_image(img_path)
        res_net.blobs['data'].data[...] = transformer.preprocess('data', img)
        out = res_net.forward()
	top_k_label = util.get_labels(out,mconf.RES_LABEL)
	top_k_prob = util.get_probs(out)
        result = util.get_label_prob_pairs(top_k_label, top_k_prob)
        return jsonify({'status': 200, 'result':result})
    else:
	return jsonify({'status':400, 'result': 'Resource not found'})
        

@app.route('/urbanlearning/api/v1.0/detect/<string:img_id>', methods=['GET'])
def detection(img_id):
    img_path = util.load_image(image_id)
    if img_path:
	pass
    else:
	return jsonify({'status':400, 'result':'Resource not found'})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Page not Found'}), 404)

if __name__ == '__main__':
    app.run(host='139.162.195.12', port=5000)
