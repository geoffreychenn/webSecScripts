import requests

url = 'http://haas.quoccabank.com/'

headers = {
    'Host': 'haas.quoccabank.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '678',
    'Origin': 'https://haas.quoccabank.com',
    'Referer': 'https://haas.quoccabank.com/',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Te': 'trailers',
    'Connection': 'close',
}

requestBox = {'requestBox':'POST+%2F+HTTP%2F1.1%0D%0AHost%3A+kb.quoccabank.com%0D%0ACookie%3A+session%3D.eJwlzDEKgDAMBdCrhD93aCMi5AKC4OZeBCM4GKWtKIh3V3B9w7sRd03raGoFUtKhDqPlU5NOEO8wLymXmFUNcoM-RL-Zo1BRdxixZyZfS83CDbX9gMfB9CrxXyAh-OcFp58fdQ.YqbQmw.aWeG23RR2GOYmjMzYZtUs1M26SU%0D%0AAccept%3A+text%2Fhtml%2Capplication%2Fxhtml%2Bxml%2Capplication%2Fxml%3Bq%3D0.9%2Cimage%2Favif%2Cimage%2Fwebp%2C*%2F*%3Bq%3D0.8%0D%0AAccept-Language%3A+en-US%2Cen%3Bq%3D0.5%0D%0AReferer%3A+http%3A%2F%2Fhaas.quoccabank.com%2F%0D%0AContent-Type%3A+application%2Fx-www-form-urlencoded%0D%0AContent-Length%3A+10%0D%0AOrigin%3A+http%3A%2F%2Fhaas.quoccabank.com%0D%0AConnection%3A+keep-alive%0D%0A%0D%0Aanswer%3D110%0D%0A'}

x = requests.post(url,  data=requestBox)
print(x.text)
print(x.request.headers)
print(x.request.body)