def foo(sentence: str) -> str:
    new_sentence = ""
    for word in sentence.split(' '):
        new_sentence+=word[::-1]+" "
    return new_sentence

print(foo("Ala ma kota"))