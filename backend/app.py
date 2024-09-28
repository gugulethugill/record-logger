# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS

class RecordManager:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_last_record(self):
        if self.records:
            return self.records[-1]
        return None

# Create Flask App
app = Flask(__name__)
CORS(app, origins="*")
record_manager = RecordManager()

@app.route('/record', methods=['POST'])
def add_record():
    data = request.get_json()
    if 'record' not in data:
        return jsonify({"error": "Missing 'record' field"}), 400
    
    record = data['record']
    record_manager.add_record(record)
    return jsonify({"message": "Record added successfully"}), 201

@app.route('/record', methods=['GET'])
def get_record():
    last_record = record_manager.get_last_record()
    if last_record:
        return jsonify({"record": last_record}), 200
    return jsonify({"message": "No records found"}), 404

if __name__ == '__main__':
    app.run(port=5001, debug=True)