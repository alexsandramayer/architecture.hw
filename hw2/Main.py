import random
from hw2.CakeGenerator import CakeGenerator
from hw2.GemGenerator import GemGenerator
from hw2.GoldGenerator import GoldGenerator

if __name__ == '__main__':
    fabricList = [GoldGenerator(), GemGenerator(), CakeGenerator()]
    for i in range(20):
        rnd = random.choice(fabricList).create_item().open()