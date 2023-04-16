import csv
import datetime

polska = []
niemcy = []
kolumny = []

with open('./zamowienia.csv', newline='', encoding="utf8",errors="ignore") as f:
    reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
    kolumny = next(reader, None)
    for wiersz in reader:
        wiersz[4] = wiersz[4][:-2].replace(",",".").replace(" ","")
        date = wiersz[2].split(".")
        wiersz[2] = datetime.datetime(int(date[2]), int(date[1]), int(date[0])).strftime("%Y-%m-%d")
        if wiersz[0]=="Polska" :
            polska.append(wiersz)
        else:
            niemcy.append(wiersz)
          
with open('./zamowienia_polska.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile,delimiter=";")
    writer.writerow(kolumny)
    for wiersz in polska:
        writer.writerow(wiersz)
        
with open('./zamowienia_niemcy.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile,delimiter=";")
    writer.writerow(kolumny)
    for wiersz in niemcy:
        writer.writerow(wiersz)