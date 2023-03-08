lorem_ipsum = 'Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker'

litera_1 = 'Patryk'[2]
litera_2 = 'Jurczyk'[3] 
liczba_liter1 = lorem_ipsum.lower().count(litera_1.lower())
liczba_liter2 = lorem_ipsum.lower().count(litera_2.lower())
print(f'W tekście jest {liczba_liter1} liter {litera_1.lower()} oraz {liczba_liter2} liter {litera_2.lower()}')