import json
import requests
import pandas as pd

URL = ""
response = requests.get(URL)  # 문자열
arr = json.loads(response.content)  # 문자열 -> json

flowers = set()
품종 = set()

for item in arr["response"]["items"]:
    품종.add((item["pumName"], item["goodName"]))
    flowers.add((item["pumName"], item["goodName"], item["lvNm"], item["avgAmt"]))

print(len(품종))
flowers = list(flowers)
flowers.sort(key=lambda x: (x[0], x[1], x[2]))

df = pd.DataFrame(flowers)
df.columns = ["품목", "품종", "품질", "평균가"]
df.to_csv("./1106.csv", sep=",", na_rep="NaN")

품종 = list(품종)
품종.sort(key=lambda x: (x[0], x[1]))
df2 = pd.DataFrame(품종)
df2.columns = ["품목", "품종"]
df2.to_csv("./품종.csv", sep=",", na_rep="NaN")
