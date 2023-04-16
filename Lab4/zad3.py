import sys

print('Wpisz liczbę całkowitą: ', end="")

number = int(sys.stdin.readline())
multiplier = pow(10,(len(str(number))-1))
ratio = f"Podaną liczbę można zapisać jako: "
print(number, multiplier)
while number > 0:
    temp = int(number//multiplier)
    ratio+=f'{multiplier} * {temp}'
    if(multiplier > 1):
        ratio+=f' + '
    number = number - (temp*multiplier)
    multiplier= int(multiplier/10)
sys.stdout.write(ratio)
