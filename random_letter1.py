s=["самовар","весна","лето"]
import random
w=random.choice(s)
n=random.randint(0,len(w)-1)

print(w[:n]+"?"+w[n+1:])

if w[n]:
    if w[n]==input("Введите верную букву\n"):
        print("Победа!")
    else:
        print("Неудача:(")
        print("Это было слово -", w)
