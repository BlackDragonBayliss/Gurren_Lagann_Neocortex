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
    return_value = 'pass'
    for key, value in content.items():
        # print("hit bird intake")
        if key == 'request_type':
            if value == "bird1":
                for key, value in content.items():
                    if key == "payload":
                        print("bird1: "+str(value))
                        operationCenter = OperationCenter()
                        operationCenter.goldenGooseProcess(value)

    return "Query received"


if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0', port=4440)


