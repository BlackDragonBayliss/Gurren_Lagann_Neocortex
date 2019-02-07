from flask import Flask, jsonify, request
from flask_cors import CORS
from Operation_Center import Operation_Center
from Perpetual_Timer import Perpetual_Timer

app = Flask(__name__)
CORS(app)


def __new__(self):
    self.operation_center = Operation_Center()


@app.route('/initSystem', methods=['POST'])
def init_system():
    operation_center = Operation_Center()
    operation_center.process_main_process_loop()
    return "initiated"

@app.route('/recordQueries', methods=['POST'])
def recordQueries():
    content = request.get_json()
    print(content)
    return "Query received"

if __name__ == '__main__':
    app.run(debug=False)