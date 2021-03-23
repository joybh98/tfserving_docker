import base64
import requests
import numpy as np
import json

SERVER_URL='http://localhost:8501/v1/models/nlp_model:predict'
headers={"content-type":"application/json"}

test_data = np.ndarray(shape=(100,),dtype=int).tolist()

body = {
    "signature_name": "serving_default",
    "instances":{"b64":test_data}
}

# r will show the http response ex:<Response [400]>, <Response [200]> etc
try:
    r = requests.post(SERVER_URL,data=json.dumps(body),headers=headers)
    print(json.loads(r.text))
except ConnectionError:
    print('Cant connect!')