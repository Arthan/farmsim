import json
from tabulate import tabulate
from machine import Machine
from utils import get_int

class Shop():
    def __init__(self):
        self.categories = dict()

    def add_items(self, category_name, items):
        category = []
        if category_name in self.categories:
            category = self.categories[category_name]
        
        for item in items:
            category.append(Machine(**item))

        self.categories[category_name] = category

    def print_items_from_category(self, category):
        tab = [['nr', 'nazwa', 'silnik', 'predkosc', 'waga', 'cena']]
        for idx, item in enumerate(category):
            tab.append([
                idx + 1,
                item.name, 
                f'{item.engine}KM', 
                f'{item.speed}km/h', 
                f'{item.weight}t', 
                f'${item.price:,.0f}'.replace(',', '.')
            ])
        print()
        print(tabulate(tab, headers='firstrow', tablefmt='fancy_grid'))

    def select_category(self):
        for idx, category in enumerate(self.categories):
            print(f'({idx+1}){category}')
        category_idx = get_int('jaką chcesz sprawdzić kategorie: ', 1, len(self.categories)) - 1
        category_name = list(self.categories.keys())[category_idx]
        return category_name

    def select_item(self, category_name):
        # category_name = list(self.categories.keys())[category_idx]
        category = self.categories[category_name]
        if len(category) == 0:
            print('nic tu nie pozostalo do kupienia')
            return
        self.print_items_from_category(category)
        item_idx = get_int('który chcesz kupić pojazd: ', 1, len(category), True)
        return item_idx - 1 if not item_idx is None else None

    def load(self, filename):
        with open(filename) as file:
            data = json.load(file)
            for category in data['categories']:
                self.add_items(category['category_name'], category['machines'])