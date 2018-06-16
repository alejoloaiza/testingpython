from flask import Flask, jsonify

app = Flask(__name__)

recommendations = [
    {
        'id': 3,
        'uuid': 'xyz123',
        'username': 'fmauricios',
        'name': u'Mauricio Serna',
    },
    {
        'id': 4,
        'uuid': 'xyz123444',
        'username': 'arpo',
        'name': u'Ana Restrepo',
    }
]

@app.route('/api/recommendations', methods=['GET'])
def get_users():
    return jsonify({'recommendations': recommendations})
