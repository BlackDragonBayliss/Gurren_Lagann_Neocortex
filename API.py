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

    print(str(content))

    for key, value in content.items():
        print("hit bird intake")
        if key == 'request_type':
            if value == "bird1":
                print("hit value == bird1")
                for key, value in content.items():
                    if key == "payload":
                        print("key == payload")
                        for key, value in value.items():
                            if key == "data":
                                print("internal bird API")
                                print("bird1: " + str(value))
                                # print("bird: "+str(value.data))
                                operationCenter = OperationCenter()
                                operationCenter.goldenGooseProcess(value)
    return "Query received"

@app.route('/breachBuy', methods=['POST'])
def breachBuy():
    content = request.get_json()
    return_value = 'pass'
    print(str(content))
    for key, value in content.items():
        print("hit breachBuy intake")
        if key == 'request_type':
            if value == "breachBuy":
                print("hit value == breachBuy")
                for key, value in content.items():
                    if key == "payload":
                        print("key == payload")
                        for key, value in value.items():
                            if key == "data":
                                print("internal breachBuy API")
                                print("breachBuy: " + str(value))
                                # print("bird: "+str(value.data))
                                operationCenter = OperationCenter()
                                operationCenter.breachBuy(value)
    return "Query received"

@app.route('/test1', methods=['POST'])
def test():
    content = request.get_json()
    for key, value in content.items():
        print("hit bird intake")
        if key == 'request_type':
            if value == "test1":
                for key, value in content.items():
                    if key == "list_of_list_of_crap":
                        # print(str(value))
                        for value in value:
                            print(str(value))
                            for value in value:
                                print(value)

                        # operationCenter = OperationCenter()
                        # operationCenter.goldenGooseProcess(value)

    return "Query received"

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0', port=4440)


