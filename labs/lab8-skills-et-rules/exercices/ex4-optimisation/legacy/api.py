from flask import Flask, request, jsonify
import data_processor

app = Flask(__name__)

users = []

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    users.append(data)
    return jsonify(data), 201

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    if user_id < len(users):
        return jsonify(users[user_id])
    return jsonify({'error': 'Not found'}), 404

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id < len(users):
        data = request.get_json()
        users[user_id] = data
        return jsonify(data)
    return jsonify({'error': 'Not found'}), 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id < len(users):
        users.pop(user_id)
        return '', 204
    return jsonify({'error': 'Not found'}), 404

@app.route('/export', methods=['GET'])
def export_data():
    format = request.args.get('format', 'json')
    data = {'users': users, 'count': len(users)}
    result = data_processor.process_data(data, format)
    return result

if __name__ == '__main__':
    app.run(debug=True, port=5000)

# Made with Bob
