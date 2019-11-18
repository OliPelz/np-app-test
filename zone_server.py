from flask import Flask, render_template, jsonify
import sys
import yaml

app = Flask(__name__)

server_def = None

# add static render templates
@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/check_own_zone', methods=['GET'])
def check_own_zone():
    data = {"name": "wally01", "desc": "i am mofu wolly", "rc": None} 
    return jsonify(data)

@app.route('/render_next_zone', methods=['GET'])
def check_own_zone():
    data = {"name": "wally01", "desc": "i am mofu wolly", "rc": None} 
    return jsonify(data)


if __name__ == '__main__':
   server_def = yaml.load(open('my_own_zone.yaml'))
   app.run(port=5002)
