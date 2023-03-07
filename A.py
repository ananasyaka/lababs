'Проверка пароля'
Password = input("Введите пароль:")


if len(Password) < 5:
   print("Пароль слишком короткий, длина пароля должна быть 5 символов и больше")


else:  Password2 = input("Повторно введите пароль:")
if Password == Password2:
     print("Пароль принят")
else: print("Пароль не принят")