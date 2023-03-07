'Проверка места в вагоне'

Number = int(input("Введите номер места:"))
if Number>36:
  a='Боковое'
else: a='Купе'

if Number % 2 == 0:
  b='верхнее'
else: b='нижнее'

print(a,b)