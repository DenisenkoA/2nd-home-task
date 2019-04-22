import math
x=int(input("Введите сколько оставить знаков после запятой\n"))
print('{pi:.{x}f}'.format(x=x,pi=math.pi))
