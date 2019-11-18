from flask import Flask, render_template, jsonify
import sys
import yaml

app = Flask(__name__)

server_def = None
zone_name = None

# add static render templates
@app.route('/')
def index():
    return render_template('list.html', title='Home')

@app.route('/children', methods=['GET'])
def get_childs():
    data = {"name": "wally01", "desc": "i am mofu wolly", "rc": None} 
    return jsonify(data)

if __name__ == '__main__':
   server_def = yaml.load(open('setup.yaml'))
   zone_name = sys.argv[1]
   app.run(port=5002)
