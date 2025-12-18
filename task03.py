n = int(input('N='))

if n < 15:
    f = range(n, 15+1,)
        
else:
    f = range(n, 15-1, 1)
    
for i in f:
    print(i)
