import unidecode

def save_surnames(surnames):
    surnames_a_m = []
    surnames_n_z = []

    for surname in surnames:
        surname_ascii = unidecode.unidecode(surname)
        if surname_ascii[0].lower() in 'abcdefghijklm':
            surnames_a_m.append(surname)
        else:
            surnames_n_z.append(surname)

    with open('./A-M_nazwiska.txt', 'w') as file_a_m:
        file_a_m.write('\n'.join(surnames_a_m))

    with open('./N-Ż_nazwiska.txt', 'w') as file_n_z:
        file_n_z.write('\n'.join(surnames_n_z))

names = ['Wyżlic',"Sapkowski","Malinowski","Hohenzolern","Albrecht", "Brunow","Gruszczyński","Żuchwa"]
save_surnames(names)