# sending requests and getting outputs

import requests
import base64
import json

headers={"content-type":"application/json"}
SERVER_URL= 'http://localhost:8501/v1/models/nlp_model:predict'

loaded_text=open('example_sentence.txt','rb').read()
txt_bytes = base64.b64encode(loaded_text).decode('utf-8')

body = {
    "signature_name": "serving_default",
    "examples" : [{
        "x": { "b64": txt_bytes},  
     }]
}

r = requests.post(SERVER_URL,data=json.dumps(body),headers=headers)

print(json.loads(r.text))