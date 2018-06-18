from flask import Flask, jsonify, request
from server import Datos
app = Flask(__name__)


@app.route('/api/recommendations', methods=['POST'])
def get_recommendation():
    if request.method == 'POST':
        req_data = request.get_json()
        print(req_data)
        return jsonify({'recommendations': req_data})
