from hw2.ItemFabric import ItemFabric
from hw2.CakeReward import CakeReward


class CakeGenerator(ItemFabric):

    def create_item(self):
        print("Создали сундук с тортом")
        return CakeReward()