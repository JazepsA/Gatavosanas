import csv
with open('agenti.csv', mode ='r', encoding='utf-8')as file:
    csvFile = csv.reader(file, delimiter=";")

    for lines in csvFile:
        print(lines) 
    print("-------------------")


with open('agenti.csv', mode ='r', encoding='utf-8')as file, open('name.csv', 'w', newline='', encoding="utf-8") as csvfile:
  csvFile = csv.reader(file, delimiter=";")
  writer = csv.writer(csvfile)
  for lines in csvFile:
    if lines[0] == "Izglītības iestāde" or lines[0] == "Valsts iestāde":
      writer.writerow(lines)
      print(lines) 


with open('agenti.csv', mode ='r', encoding='utf-8')as file:
  csvFile = csv.reader(file, delimiter=";")
  for lines in csvFile:
    if "Rīga," in lines[2]:
      print(lines) 

with open('agenti.csv', mode ='r', encoding='utf-8')as file,open('sorted.csv', 'w', newline='', encoding="utf-8") as csvfile:
    csvFile = csv.reader(file, delimiter=";")
    csvFile = sorted(csvFile, key= lambda row : row[1]) 
    writer = csv.writer(csvfile)
    for lines in csvFile:
        writer.writerow(lines)
        print(lines) 