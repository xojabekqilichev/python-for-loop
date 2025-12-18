a = float(input("1- telefon narxi:"))
b = float(input("2- telefon narxi:"))
c = float(input("3- telefon narxi:"))
d = float(input("4- telefon narxi:"))
e = float(input("5- telefon narxi:"))

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
    maxi = e

narx = (mini + maxi) / 2
print(narx)
