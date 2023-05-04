#10 to non 10
number=""
x=int(input())
base=int(input()) # base<=10
while x>0:
    digit=x%base
    x//=base
    number+=str(digit)
print(number[::-1])
