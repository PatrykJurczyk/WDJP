words = input("Wprowadź listę wyrazów, oddzielając je przecinkami: ").split(",")
sorted_words = sorted(words, key=lambda word: len(word), reverse=True)
print(sorted_words)