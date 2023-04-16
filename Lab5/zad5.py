from random import  randint

def foo(n: int) -> list():
    dice = dict.fromkeys([x for x in range(1,7)],0)
    for x in range(n):
        throw = randint(1,6)
        dice[throw]+=1
    return [(f'oczka: {x}', f'rzutów: {dice[x]}') for x in range(6, 0, -1)]
    

n = int(input('Podaj liczbę: '))
print(foo(n))


