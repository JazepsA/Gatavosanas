import re
saraksts = {}
# parbauda vai vards ir derīgs
# tikai japartaisa lai butu bez regex, jo vins nelauj Ā Č utt...
def derigs(str):
    if(not str[0].isupper()):
        return False
    pattern = r'^[A-Za-z]+$'
    x = re.findall(pattern, str)
    if x:
        return True
    else:
        return False

# ļauj ievadīt vienu vārdu
def ievadit():
    while True:
        vards = input("Ievadiet vārdu😊
        if(derigs(vards)):
            return vards
        print("Nepareizi ievadits vards!")

burti = "ABC"
for i in burti:
    saraksts[i] = ""

# parbaudit vai saraksta vajag elementu
def parbaudit():
    for i in burti:
        if saraksts[i] == "":
            return False
    return True

while True:
    if(parbaudit()):
        break
    vards = ievadit()
    saraksts[vards[0]] = vards

print(saraksts) 