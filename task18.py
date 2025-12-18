N = input("Sonni kiriting:")
r = 0

for i in range(1, int(N)+1):
    if i % 2 != 0:
       r += i 
print(r)
