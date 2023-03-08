sentence = input('Zdanie z jednolitym separatorem (spacja, średnik, itd.):\n')
source_separator = input('Podaj separator z powyższego zdania:\n')
destination_separator = input('Podaj separator docelowy:\n')

split_sentence = sentence.split(source_separator)
sentence = destination_separator.join(split_sentence)
print('Twoje nowe zdanie:\n'+sentence+'\n')