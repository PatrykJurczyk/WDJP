text = 'Ala ma kota.'
generator = ( (x,[ord(y) for y in x]) for x in text.split(" "))
for x in generator:
    print(x)