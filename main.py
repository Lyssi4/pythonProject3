from pprint import pprint
import os


def name_file():
    name = input('Введите имя файла: ') + '.txt'
    return name


def open_file():
    name_open_file = name_file()
    file_directory = os.path.join(os.getcwd(), name_open_file)
    keys_list = ['ingredient_name', 'quantity', 'measure']
    cook_book = {}

    with open(file_directory) as file:
        for all_data in file:
            ingr_list = []
            dish_name = all_data
            amount_ingredients = int(file.readline())
            for ingredients in range(amount_ingredients):
                parse_str = str(file.readline().strip()).split('|')
                ingr_dict = {keys_list[i]: parse_str[i] for i in range(len(keys_list))}
                ingr_list.append(ingr_dict)
            file.readline()
            cook_book[dish_name.strip()] = ingr_list
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = open_file()
    ingred_dict = {}
    for dish_name in dishes:
        if dish_name in cook_book.keys():
            for ingred in cook_book[dish_name]:
                ingredient = ingred['ingredient_name']
                quantity = int(ingred['quantity']) * person_count
                measure = ingred['measure']
                if ingredient not in ingred_dict.keys():
                    ingred_dict[ingredient] = {'quantity': quantity, 'measure': measure}
                else:
                    ingred_dict[ingredient]['quantity'] += quantity
        else:
            print(f'Блюдо {dish_name} не найдено')
    return ingred_dict


pprint(open_file(), sort_dicts=False)
pprint(get_shop_list_by_dishes(['Омлет', 'Омлет', 'Фахитос'], 2))