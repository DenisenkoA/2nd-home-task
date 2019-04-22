s="У лукоморья 123 дуб зеленый 456"

#1
if s:
    if s.count("я")!=0:
        print(s.index('я'))
    else:
        print("буква ""я"" не была представлена")

#2
print(s.count("y"))

#3
if  s:
    if s.isupper ==True:
        print(s.isupper())
    else:
        print(s.upper())

#4
print(len(s))

if s:
    if len(s)>4:
        print(s.lower())
        
#5
print('О'+s[1:])
