import csv
from typing import Any, Dict, List
import datetime

nation: List[List[str]] = []
sorted_nation: Dict[str, List[List[str]]] = {}
kolumny: List[str] = []

def add_to_dict(dictionary: Dict[str, List[List[str]]], new_value: List[Any]) -> Dict[str, List[List[str]]]:
    if new_value[0] in dictionary.keys():
        dictionary[new_value[0]].append(new_value)
    else:
        dictionary[new_value[0]] = [new_value]
    return dictionary

with open('./zamowienia.csv', newline='', encoding="utf8", errors="ignore") as f:
    reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
    kolumny = next(reader, None)
    for wiersz in reader:
        nation.append(wiersz)
nation = list(map(lambda wiersz: wiersz[:2] + [datetime.datetime(int(wiersz[2].split(".")[2]), int(wiersz[2].split(".")[1]),\
                                                                int(wiersz[2].split(".")[0])).strftime("%Y-%m-%d")] \
                                                + [wiersz[3]]+[wiersz[4][:-2].replace(",",".").replace(" ","")],nation))
sorted_nation = list(map(lambda x: add_to_dict(sorted_nation,x), nation))[0]
          
with open('./zamowienia_polska.csv', 'w', newline='') as csvfile, open('./zamowienia_niemcy.csv', 'w', newline='') as csvfile2:
    writer = csv.writer(csvfile,delimiter=";")
    writer2 = csv.writer(csvfile2,delimiter=";")
    writer.writerow(kolumny)
    writer2.writerow(kolumny)
    list(map(lambda x: writer.writerow(x),sorted_nation['Polska']))
    list(map(lambda x: writer2.writerow(x),sorted_nation['Niemcy']))