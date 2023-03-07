N = int(input("Введите кол-во слов:"))
s=''
p=' '
for i in range(N):
    word = str(input("Введите слово:"))
    s+=p
    s+=word
    i=i+1
print(s)