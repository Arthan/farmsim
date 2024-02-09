from time import sleep
from farm_simulator import FarmSimulator


if __name__ == '__main__':
    farm = FarmSimulator()
    farm.money = 100000
    farm.run()
