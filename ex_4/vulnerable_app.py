from flask import Flask, request, jsonify
import os

app = Flask(__name__)

def execute(command):
    result = os.popen(command).read()
    return result

@app.route('/checkfile', methods=['GET'])
def check_file():
    filename = request.args.get('filename')
    command_result = execute(f"ls -l {filename} 2>/dev/null")
    return jsonify({'command_result': command_result})

if __name__ == '__main__':
    app.run(debug=False)
