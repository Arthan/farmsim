from time import sleep
from shop import Shop
from menu import Menu


PLOW = 0 # orać
SOW = 1 # siać
COLLECT = 2 # zbierać

TRACTORS = 'ciągniki'
COMBINES = 'kombajny'

class FarmSimulator():
    def __init__(self):
        self.main_menu = Menu([
            {'name': 'zaoraj pole', 'func': self.do_plow},
            {'name': 'zasiej pole', 'func': self.do_sow},
            {'name': 'zbierz plony', 'func': self.do_collect},
            {'name': 'sprzedaj plony', 'func': self.do_sell},
            {'name': 'sklep', 'func': self.do_shop},
            {'name': 'info', 'func': self.do_info},
            {'name': 'koniec', 'func': self.do_exit},
        ])
        self.reset()

    def reset(self):
        self.money = 0
        self.crops = 0
        self.next_action = COLLECT
        self.tractor = None
        self.combine_harvester = None

        self.shop = Shop()
        self.shop.load('machines.json')
        self.tractor = self.shop.categories[TRACTORS].pop(0)
        self.combine_harvester = self.shop.categories[COMBINES].pop(0)

    def do_info(self):
        print(
            '   >>>INFO<<<\n' +
            '=> na początku masz juz pole z gotowymi plonami\n' +
            '=> musisz robić wszystko po kolei\n' +
            '=> masz mały ciągnik i słaby kombajn\n' +
            '=> po zdobyciu pewnej ilości pieniedzy możesz sobie coś kupić w sklepie\n')
        input('[nacisnij enter]')

    def do_action(self, action, msg_cant, action_desc, duration, next_action):
        if not self.next_action == action:
            print(msg_cant)
            return

        # duration = int(round(duration / 10.0))
        print(f'{action_desc} zajmie ci to {duration} sekund')
        for time_left in range(duration, 0, -1):
            print(f' Czas do ukończenia: {time_left}    \r', end='')
            sleep(1)
        print('Ukończono.' + ' '*20)
        self.next_action = next_action


    def do_plow(self):
        self.do_action(PLOW, '!!!Nie masz zebranych plonów!!!', 'Oraż pole', self.tractor.wait, SOW)

    def do_sow(self):
        self.do_action(SOW, '!!!Nie masz zaoranego pola!!!', 'Siejesz pole', self.tractor.wait, COLLECT)
        
    def do_collect(self):
        self.do_action(COLLECT, '!!!Nie masz zasianego pola!!!', 'Zbierasz plony', self.combine_harvester.wait, PLOW)
        self.crops += 500

    def do_sell(self):
        if self.crops == 0:
            print('Nie masz nic co moglbys sprzedac')
            return
        income = self.crops * 2
        print(f'Sprzedajesz {self.crops} plonow za {income} $')
        self.crops = 0
        self.money += income
        
    def do_shop(self):
        category_name  = self.shop.select_category()
        category = self.shop.categories[category_name]
        item_idx = self.shop.select_item(category_name)
        if item_idx is None:
            return
        item = category[item_idx]
        if item.price > self.money:
            print('!!!nie możesz tego kupić potrzebujesz jeszcze ', item.price - self.money)
            return
        self.money -= item.price
        if category_name == TRACTORS:
            self.tractor = item
        elif category_name == COMBINES:
            self.combine_harvester = item
        category.remove(item)

    def do_exit(self):
        self.running = False

    def step(self):
        print(f'\n>>> {self.money} $<<<')
        print(f'plonow: {self.crops}\n')
        self.main_menu.run()

    def run(self):
        self.running = True
        while self.running:
            self.step()
