NOT_FOUND = 'Resource not found'

def get_response(code, task, img_id, result,img_url):
    """Generate response"""
    body = {
	'image': img_id,
	'status': code,
	'task': task,
	'result': result,
	'image_url': img_url
    }
    return body
