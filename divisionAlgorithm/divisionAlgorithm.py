#define input
from re import A


a = 99991
b = 2

Q = 0
R = a
while R>=b:
    R = R - b
    Q = Q + 1
    if R<b:
        print("quotient=",Q , "Remainder=", R)
    