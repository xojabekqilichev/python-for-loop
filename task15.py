n = int(input("Son kiriting: "))
r = 0

for _ in range(len(str(n))):
    r = r * 10 + (n % 10)
    n //= 10

print(r)
