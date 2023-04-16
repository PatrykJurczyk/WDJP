text = input('Wpisz zdanie: ')
split_text = text.split(" ")
print(sorted(split_text, key=len))