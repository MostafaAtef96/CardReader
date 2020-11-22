import requests

url = 'http://31.220.48.190:8000/ocr'
files = {'front': open('img300f.png', 'rb'),'back': open('img300b.png', 'rb')}
result = requests.post(url, files=files)

print(result.json())
