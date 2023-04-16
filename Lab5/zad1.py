a = [ 1/x for x in range(1,11) ]
b = [ pow(2,x) for x in range(11) ]
c = [ x for x in b if x%4 == 0] 
print(a)
print(b)
print(c)