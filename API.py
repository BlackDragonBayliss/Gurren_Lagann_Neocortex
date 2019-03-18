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
    # print(content)
    return_value = 'pass'
    for key, value in content.items():
        # print("hit bird intake")
        if key == 'request_type':
            if value == "bird1":
                for key, value in content.items():
                    if key == "payload":
                        operationCenter = OperationCenter()
                        operationCenter.goldenGooseProcess(value)


                        # for key, value in value.items():
                        #     if key == "data":
                        #         # print(value)


                                # operation_center = Operation_Center()
                                # operation_center.process_async_top_stock_phase1_internal()
                                # return_value = 'res'
    return "Query received"

# @app.route('/birdMessengerQuery', methods=['POST'])
# def birdMessengerQuery():
#     # content = request.get_json()
#     # print(content)
#     content = request.get_json()
#     return_value = 'pass'
#     for key, value in content.items():
#         print("hit bird intake")
#         if key == 'request_type':
#             if value == "bird1":
#                 for key, value in content.items():
#                     if key == "payload":
#                         for key, value in value.items():
#                             if key == "data":
#                                 operation_center = Operation_Center()
#                                 operation_center.process_async_top_stock_phase1_internal()
#                                 return_value = 'res'
#
#     return "birdMessengerQuery received"

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0', port=4440)


