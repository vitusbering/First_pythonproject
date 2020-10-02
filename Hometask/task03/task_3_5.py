# ax2 + bx + c = 0
a = int(input("enter variable a: "))
b = int(input("enter variable b: "))
c = int(input("enter variable c: "))
D = b * b - 4 * a * c
print(D)
if D >= 0:
    x1 = (b * -1 + (D ** (1 / 2)))/(2*a)
    print(x1)
    if D > 0:
        x2 = (b * -1 - (D ** (1 / 2)))/(2*a)
        print(x2)
else:
    print('No solution')




