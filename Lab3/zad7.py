import string 


text = input("Input text:").lower()
unique = list()
for x in text:
    try:
        x = int(x)
    except:
        None
    if x not in unique:
        unique.append(x)
letters = [x for x in unique if type(x) == str if x in [*string.ascii_lowercase]]
digits = [x for x in unique if type(x) == int]

print(f'{len(letters)} to {len(letters)/len(string.ascii_lowercase)*100:.2f}%')
print(f'{len(digits)} to {len(digits)/len(string.digits)*100:.2f}%')