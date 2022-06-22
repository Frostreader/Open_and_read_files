import os
from pprint import pprint

# Задача № 1
path = os.getcwd()
file_name = 'recipes.txt'
full_path = os.path.join(path, file_name)


def open_file(file_path, mode='rt', encoding='utf-8'):
    with open(file_path, mode) as file:
        cook_book = {}

        for line in file:
            dish_name = line.strip()
            ingredient_count = int(file.readline().strip())
            dish = []

            for item in range(ingredient_count):
                ingredient_list = file.readline().strip().split(' | ')
                d = {}
                for i in range(len(ingredient_list)):
                    d['ingredient_name'] = ingredient_list[0]
                    d['quantity'] = ingredient_list[1]
                    d['measure'] = ingredient_list[2]
                dish.append(d)

            file.readline()
            cook_book[dish_name] = dish

    return cook_book


open_file(full_path)


# Задача № 2
def get_shop_list_by_dishes(dishes, person_count):
    cook_book = open_file(full_path)
    shop_list = {}
    name_list = ['ingredient_name', 'quantity', 'measure']
    for dish in dishes:
        for j in cook_book[dish]:
            if j[name_list[0]] in shop_list.keys():
                quantity = int(shop_list[j[name_list[0]]][name_list[1]]) + int(j[name_list[1]]) * person_count
                shop_list[j[name_list[0]]] = {name_list[2]: j[name_list[2]], name_list[1]: quantity}
            else:
                quantity = int(j[name_list[1]]) * person_count
                shop_list[j[name_list[0]]] = {name_list[2]: j[name_list[2]], name_list[1]: quantity}

    pprint(shop_list)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

# Задача № 3
files = ['1.txt', '2.txt', '3.txt']
data = []
text = {}


def merge_files():
    for file in files:
        file_path = os.path.join(path, file)
        with open(file_path, 'rt', encoding='utf-8') as f:
            text.setdefault(file, f.readlines())
            sorted_file_name = sorted(text, key=text.get, reverse=True)
            sorted_text = sorted(text.values(), reverse=True)

    with open('result.txt', 'w', encoding='utf-8') as res:
        for i in range(len(sorted_text)):
            res.write('\n' + str(sorted_file_name[i]))
            res.write('\n' + str(len(sorted_text[i])))
            res.write('\n')
            for j in range(len(sorted_text[i])):
                res.write(sorted_text[i][j].strip())


merge_files()


