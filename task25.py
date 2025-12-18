a = float(input("Yoshni kiriting:"))
b = float(input("Yoshni kiriting:"))
c = float(input("Yoshni kiriting:"))
d = float(input("Yoshni kiriting:"))
e = float(input("Yoshni kiriting:"))

mini = a
maxi = a

if b < mini:
    mini = b
if c < mini:
    mini = c
if d < mini:
    mini = d
if e < mini:
    mini = e

if b > maxi:
    maxi= b
if c > maxi:
    maxi = c
if d > maxi:
    maxi = d
if e > maxi:
    max = e

average = (mini + maxi) / 2
print(float(average))
