import base64
import requests
import numpy as np
import json

SERVER_URL='http://localhost:8501/v1/models/nlp_model:predict'
headers={"content-type":"application/json"}

test_data = np.ndarray(shape=(100,)).tolist()

body = {
    "signature_name": "serving_default",
    "examples": test_data
}

r = requests.post(SERVER_URL,data=json.dumps(body),headers=headers)

print(json.loads(r.text))