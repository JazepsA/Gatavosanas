import csv
with open('Darbgramata1.csv', mode ='r', encoding='utf-8')as file, open('bbb.csv', 'w', newline='', encoding="utf-8") as csvfile:
    csvFile = csv.reader(file, delimiter=";")
    writer = csv.writer(csvfile, delimiter=";")
    
    
    for lines in csvFile:
        writer.writerow(lines) 