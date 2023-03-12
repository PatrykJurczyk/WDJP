months = dict()
polish = ["styczeń", "luty", "marzec", "kwiecień", "maj", "czerwiec", "lipiec", "sierpień", "wrzesień", "październik", "listopad", "grudzień"]
for x in range(1,13):
    months[x]=polish[x-1]


months_pl = months.copy()
print(months_pl)
months_en = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
print(months_en)

months = dict()
months['pl'] = months_pl
months['en'] = months_en

print(months['pl'][4], months['en'][4])