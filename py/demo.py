import json
import requests

URL = ""
response = requests.get(URL)  # 문자열
arr = json.loads(response.content)  # 문자열 -> json

flowers = set()

for item in arr["response"]["items"]:
    flowers.add((item["pumName"], item["goodName"]))

print(len(flowers))
flowers = list(flowers)
flowers.sort(key=lambda x: x[0])
for f in flowers:
    print(f)
