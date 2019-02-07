from flask import Flask, jsonify, request
from flask_cors import CORS
from OperationCenter import OperationCenter
from Perpetual_Timer import Perpetual_Timer

app = Flask(__name__)
CORS(app)


def __new__(self):
    # self.operationCenter = OperationCenter()
    pass


@app.route('/initSystem', methods=['POST'])
def init_system():
    operationCenter = OperationCenter()
    # operation_center.process_main_process_loop()
    operationCenter.getNodeInformation()
    return "initiated"

@app.route('/recordQueries', methods=['POST'])
def recordQueries():
    content = request.get_json()
    print(content)
    return "Query received"

if __name__ == '__main__':
    app.run(debug=False)
