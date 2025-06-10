import requests

pieprasijums=requests.get("https://data.gov.lv/dati/lv/api/3/action/datastore_search?resource_id=92ac6e57-c5a5-444e-aaca-ae90c120cc3d")
if (pieprasijums.status_code >= 400):
    print("Serveris neatbild")
else:
    teksts=pieprasijums.json()
    if len(teksts) == 0:
        print("nav teksta")
    print(teksts)

    vietas=[]
    record= teksts["result"]["records"]
    for i in range(len(record)):
        if record [i] ["8 : Baterijas un akumulatori"] == "x":
            print(record[i]["adrese"])
        if record [i] ["8 : Baterijas un akumulatori"] == "x":
            print(record[i]["pilsetanovads"])
        if record [i] ["10 : Nolietotās riepas"] == "x":
            print(record[i]["adrese"])
        if record [i] ["10 : Nolietotās riepas"] == "x":
            print(record[i]["pilsetanovads"])
        if record [i] ["3 : Metāls"] == "x":
            print(record[i]["adrese"])
        if record [i] ["3 : Metāls"] == "x":
            print(record[i]["pilsetanovads"])
        



