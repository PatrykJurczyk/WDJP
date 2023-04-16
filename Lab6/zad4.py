mieszana = [1, 2.3, 'Patryk', 5, 'Alicja', 3.0]
dictionary = dict()
for x in mieszana:
    if type(x).__name__ not in dictionary.keys():
        dictionary[type(x).__name__] = [x]
    else:
        dictionary[type(x).__name__].append(x)
print(dictionary)