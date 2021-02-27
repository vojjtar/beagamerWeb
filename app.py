from flask import Flask, render_template, url_for, jsonify, request

import json

from API.getData import serverInfo


#python 3.8.6


app = Flask(__name__, template_folder='BeaGamer/templates', static_folder='BeaGamer/static')


@app.route('/')
def beagamerHub():
    return render_template('index.html')

@app.route('/rust')
def rustHub():
    return render_template('Rust.html')


@app.route('/test', methods=['GET'])
def testfn():
    if request.method == 'GET':
        serverInfo()
        with open('API/server_data.json') as f:
            data = json.load(f)
        return jsonify(data)





if __name__ == '__main__':
    app.run()
