import requests

url = 'http://127.0.0.1:5000/ocr'
files = {'front': open('img300f.png', 'rb'),'back': open('img300b.png', 'rb')}
result = requests.post(url, files=files)

print(result.json())