int_bit = [1, 3]
float_ii = [3.2, 8.0]

for x in int_bit:
    if (n := bin(x).count("1")) > 1:
        print(str(x) + str(n))
for x in float_ii:
    if x.is_integer():
        print(str(x))