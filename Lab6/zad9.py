import random

with open('./hasla.txt', 'r') as f:
    hasla = f.read().splitlines()

haslo = random.choice(hasla)
litery_hasla = [' ' if c == ' ' else '_' for c in haslo]
print('Odgadnij hasło: ' + ' '.join(litery_hasla))

while '_' in litery_hasla:
    litera = input('Podaj literę lub wpisz "hasło", aby odgadnąć całe hasło: ').lower()
    
    if litera == 'hasło':
        odp = input('Podaj hasło: ').lower()
        if odp == haslo.lower():
            print('Brawo, odgadłeś hasło!')
            break
        else:
            print('Niepoprawne hasło.')
    elif len(litera) != 1 or not litera.isalpha():
        print('Podaj pojedynczą literę.')
    elif litera in haslo.lower():
        for i, c in enumerate(haslo):
            if c.lower() == litera:
                litery_hasla[i] = haslo[i]
        print(' '.join(litery_hasla))
    else:
        print('Nie ma takiej litery w haśle.')
else:
    print('Brawo, odgadłeś hasło!')   