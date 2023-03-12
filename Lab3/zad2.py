numbers = [1,2,3,4,5,6,7,8,9,10]
numbers_new = numbers[5:]
numbers = numbers[:5]

numbers_concat = (numbers + numbers_new)
numbers_concat.insert(0,0)
numbers_concat.sort(reverse=True)

print(numbers_concat)