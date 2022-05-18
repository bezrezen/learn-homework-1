"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

def main():
    phones = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]
    i = 0
    print('Суммарное количество продаж для каждого товара:')
    for sold_sum_per_item in phones:
      print(sum(phones[i]['items_sold']))
      i += 1
    print('Среднее количество продаж для каждого товара:')
    i = 0
    for avg_sold_per_item in phones:
      print(sum(phones[i]['items_sold'])/len(phones[i]['items_sold']))
      i += 1
    i = 0
    sum_total = 0
    print('Суммарное количество продаж всех товаров:')
    for total_sum in phones:
      sum_total += sum(phones[i]['items_sold'])
      i += 1
    print(sum_total)
    i = 0
    items_sold_total = 0
    print('Среднее количество продаж всех товаров:')
    for avg_sold_total in phones:
      items_sold_total += len(phones[i]['items_sold'])
      i += 1
    print(sum_total / items_sold_total)
    
if __name__ == "__main__":
    main()
