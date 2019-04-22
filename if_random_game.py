import random
x=int(input("Введите число [0;4]\n"))
y=random.randint(0,4)
if x:
    if x==y:
        print("Вы выиграли")
    else:
        print("Вы проиграли")
if x:
    if x>y:
        print("Ваше число было больше")
    else:
        print("Ваше число было меньше")
        
