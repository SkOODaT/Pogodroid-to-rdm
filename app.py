from flask import Flask, request
import requests, os

app = Flask(__name__, static_url_path='')

@app.route('/raw', methods=['POST'])
def raw():

    RDM_URL = "http://192.168.0.101:9001/raw"
    
    req_data = request.get_json(force=True)

    print("[POGODROIDCONNECTOR:] {}".format(req_data))

    #rename keys
    req_data['data'] = req_data.pop("payload")
    req_data['method'] = req_data.pop("type")
    
    #remove unused data
    req_data.pop('timestamp')
    req_data.pop('raw')
    
    #format data to rdm
    req_rdm = {"contents": []}
    req_rdm['contents'].append(req_data)

    headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
        }

    req = requests.post(url = RDM_URL, json=req_rdm, headers=headers)
	
    #print(req_rdm)
	
    if req.status_code != 201:
        return (("Status code: {}").format(req.status_code))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='6000', debug = False)
