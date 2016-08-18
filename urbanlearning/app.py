from __init__ import *

@app.route('/urbanlearning/api/v1.0/classify/<string:img_id>', methods=['GET'])
def classification(img_id):
    """Image Classification"""
    img_path = util.load_image(img_id)
    if img_path:
        img = caffe.io.load_image(img_path)
        res_net.blobs['data'].data[...] = transformer.preprocess('data', img)
        out = res_net.forward()
        result = util.get_label_prob_pairs(out, mconf.RES_LABEL)
	body = response.get_response(200,'image classification',img_id,result)
        return jsonify(body)
    else:
	body = response.get_response(404,'image classification',img_id,response.NOT_FOUND)
	return jsonify(body)
        

@app.route('/urbanlearning/api/v1.0/detect/<string:img_id>', methods=['GET'])
def detection(img_id):
    """Object Detection"""
    #msra model has the best performance on both classification & object detection
    return classification(img_id)

@app.route('/urbanlearning/api/v1.0/scene/<string:img_id>', methods=['GET'])
def scene(img_id):
    """Scene Recognition"""
    img_path = util.load_image(img_id)
    if img_path:
	out = goo_net.forward()
	result = util.get_label_prob_pairs(out, mconf.GOO_LABEL)
	body = response.get_response(200,'scene classification',img_id,result)
	return jsonify(body)
    else:
	body = response.get_response(404,'scene classification',img_id,response.NOT_FOUND)
	return jsonify(body)
    

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': response.NOT_FOUND}), 404)

if __name__ == '__main__':
    app.run(host='139.162.195.12', port=5000)
