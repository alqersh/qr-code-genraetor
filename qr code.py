import requests
import json
print('''
   ____                       _                                        _        
  / __ \                     | |                                      | |       
 | |  | |_ __    ___ ___   __| | ___    __ _  ___ _ __  _ __ ___  __ _| |_ _ __ 
 | |  | | '__|  / __/ _ \ / _` |/ _ \  / _` |/ _ \ '_ \| '__/ _ \/ _` | __| '__|
 | |__| | |    | (__ (_) | (_| |  __/ | (_| |  __/ | | | | |  __/ (_| | |_| |   
  \___\_\_|     \___\___/ \__,_|\___|  \__, |\___|_| |_|_|  \___|\__,_|\__|_|   
                                        __/ |                                   
                                       |___/                py:@127.1.0.0.1                    
''')
url = input('enter your URL: ')
ur = 'https://api.qrcode-monkey.com//qr/custom'
headers = {
'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
'cache-control': 'no-cache',
'content-length': '512',
'content-type': 'text/plain;charset=UTF-8',
'origin': 'https://www.qrcode-monkey.com',
'pragma': 'no-cache',
'referer': 'https://www.qrcode-monkey.com/',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
'sec-ch-ua-mobile': '?1',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-site',
'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Mobile Safari/537.36',
}
data = {
    'data': f"{url}",
    'download': "imageUrl",
    'file': "svg",
    'size': '1000',
}
req = requests.post(url=ur,headers=headers,json=data).json()
url0="https:" + req["imageUrl"]
print(url0)
import shutil


response = requests.get(url0, stream=True)
with open('qr code py:@127.1.0.0.1.png', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
    print('done uplod qr code .png')
del response
