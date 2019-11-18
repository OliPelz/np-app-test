from flask import Flask, render_template, jsonify
import sys
import yaml
import requests

app = Flask(__name__)

ns_obj = None
srvs_domain = None

# add static render templates
@app.route('/')
def index():
    return render_template('list.html', title='Home')

@app.route('/check_all_neighbors', methods=['GET'])
def check_all_neighbors():
    resp_data = {"all_req_ok": False}
    all_req_ok = False
    // make a request to all other neighbor namespaces in same zone
    for proj in own_zone:
       url = "https://%s.%s" % (proj, srvs_domain)
       r = requests.get(url)
       rc = r.status_code()
    data = {"name": "wally01", "desc": "i am mofu wolly", "rc": None} 
    return jsonify(data)

if __name__ == '__main__':
   own_zone = yaml.load(open('setup.yaml'))
   ns_obj = sys.argv[1]
   srvs_domain = sys.argv[2]
   app.run(port=5002)
