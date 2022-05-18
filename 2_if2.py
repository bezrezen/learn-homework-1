"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
    first_string = input('Введите первое значение ')
    second_string = input('Введите второе значение ')
    if  first_string != second_string and second_string == 'learn':
      print(3)
    elif first_string != second_string and len(first_string) > len(second_string):
      print(2)
    elif first_string == second_string:
      print(1)
    elif type(first_string) != str and type(second_string) != str:
      print(0)
    else:
      pass
    
if __name__ == "__main__":
    main()
