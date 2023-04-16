i = input('Wprowadź z klawiatury\n')
try:
    int(i)
    print(f'Rzutowalna na typ całkowity.')
except:
    print(f'Nie rzutowalna na typ całkowity.')

try:
    float(i)
    print(f'Rzutowalna na typ zmiennoprzecinkowy.')
except:
    print(f'Nie rzutowalna na typ zmiennoprzecinkowy.')