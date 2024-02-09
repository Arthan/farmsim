from utils import get_int


class Menu():
    def __init__(self, options):
        self.options = options

    def run(self):
        for idx, option in enumerate(self.options):
            print(f'{idx+1}. {option["name"]}')
        option_nr = get_int('\nco chcesz zrobić: ', 1, len(self.options))
        print()
        self.options[option_nr-1]["func"]()