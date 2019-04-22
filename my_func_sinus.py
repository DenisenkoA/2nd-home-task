from math import sin
x=float(input("Введите вещественное число\n"))
if x:
    if 0.2<=x<=0.9:
        print(sin(x))
    else:
        print(1)
else:
    print("Введите вещественное число\n")
