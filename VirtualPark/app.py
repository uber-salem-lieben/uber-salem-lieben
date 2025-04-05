
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

posts = []

@app.route('/api/posts', methods=['GET'])
def get_posts():
    return jsonify(posts)

@app.route('/api/post', methods=['POST'])
def add_post():
    data = request.json
    if not data or 'author' not in data or 'entity' not in data or 'message' not in data:
        return jsonify({'error': 'Invalid data'}), 400
    post = {
        'author': data['author'],
        'entity': data['entity'],
        'message': data['message'],
        'timestamp': data.get('timestamp')
    }
    posts.insert(0, post)
    return jsonify({'success': True, 'post': post}), 201

if __name__ == '__main__':
    app.run(debug=True)
