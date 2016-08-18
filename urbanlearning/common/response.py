NOT_FOUND = 'Resource not found'

def get_response(code, task, img_id, result):
    """Generate response"""
    body = {
	'image': img_id,
	'status': code,
	'task': task,
	'result': result
    }
    return body
