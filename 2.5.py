num = int(input())
a = num//1000
b = num//100%10
c = num%100//10
d = num%10
print(a, b, c, d, sep='\n')

if a < 5:
    print(b)
else:
    print(c,d)