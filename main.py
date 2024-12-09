def main(s):
     lst = s.split()

     try:
        a = int(lst[0])
        b = int(lst[2])

     except ValueError:
        raise Exception("Одно из чисел не является целочисленным")

     if len(lst) != 3:
         raise Exception("Некорректный ввод данных")

     if a < 1 or a > 10 or b < 1 or b > 10:
        raise Exception("Oдно из чисел выходит за рамки")

     if(lst[1] == '+'):
         return str(a+b)

     elif(lst[1] == '-'):
         return str(a-b)

     elif(lst[1] == '*'):
         return str(a*b)

     elif(lst[1] == '/'):
         if b == 0:  # Проверка деления на ноль
             raise Exception("Деление на ноль невозможно")
         return str(a // b)

     else:
         raise Exception('Неверный оператор')

str1 = input("Введите выражение: ")
try:
    print(main(str1))
except Exception as e:
    print(f"Ошибка: {e}")