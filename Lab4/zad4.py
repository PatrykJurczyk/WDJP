import this

text = input('Wpisz tekst: ')
encode_text = ""
for x in text:
    try:
        encode_text += this.d[x]
    except:
        encode_text += x
print(encode_text)