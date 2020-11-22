import requests

url = 'http://31.220.48.190:8000/ocr'
files = {'front': open('Path/To/Front/Side/Image', 'rb'),'back': open('Path/To/Back/Side/Image', 'rb')}
result = requests.post(url, files=files)

print(result.json())
