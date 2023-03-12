import numpy as np

text = input("Input text:").lower()
letters = np.array([*text])
letters = list(np.unique(letters)) 
letters.sort()
print(letters)