import requests
import time

file1 = open("../wordlists/naughty_strings.txt")
head = {
    'Cookie' : 'login-cookie=MTIzNDU2QDEyMy5jb206dXNlcg=='
}
for line in file1:
    time.sleep(0.1)
    x = requests.get('https://big-app.quoccabank.com/api/v1/bproducts?q='+ line, headers=head)
    print(line, x.text)

file1.close()