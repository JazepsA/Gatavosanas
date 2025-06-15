import requests
import json
url = "https://data.gov.lv/dati/lv/api/3/action/package_search?q=valsts"

response= requests.get(url)

if response.status_code == 200:
   print("Dati veiksmīgi saņemti! ")
else:
   print("Kļūda:", response.status_code)
   exit()

data = response.json()
#print(data)

if not data.get("success"):
   print("API atbilde nav veiksmīga.")
   exit()

results=data["result"]
datasets= results["results"]



for dataset in datasets:
   print("-", dataset.get("title"))

#for i in results:
#  print(f"Kopējais atrasto datu kopumu skaits: {i.get("count",0)} ")

total_count = results.get("count", 0)
print(f"\n4. Kopējais atrasto datu kopumu skaits: {total_count}")

kopa=0
summa=0

for i in datasets:
   a=i.get("num_resources",0)
   if a:
      kopa+=1
      summa=summa+a
   vid= summa/kopa

print(f"vidējo publikāciju skaitu vienā datu kopā {vid}")





