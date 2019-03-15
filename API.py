from flask import Flask, jsonify, request
from flask_cors import CORS
from OperationCenter import OperationCenter

app = Flask(__name__)
CORS(app)

def __new__(self):
    pass

@app.route('/initSystem', methods=['POST'])
def init_system():
    operationCenter = OperationCenter()
    # operation_center.process_main_process_loop()
    operationCenter.getNodeInformation(2)
    return "initiated"

@app.route('/recordQueries', methods=['POST'])
def recordQueries():
    content = request.get_json()
    print(content)
    return "Query received"

@app.route('/birdMessengerQuery', methods=['POST'])
def birdMessengerQuery():
    content = request.get_json()
    # print(content)

    return "birdMessengerQuery received"

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0', port=4440)


