from itemlist import ItemList


class Item:
    def __init__(self):
        self.items = ItemList()

        for item in self.items.items:
            self.item_name = item[0]
            self.item_description = item[1]
            self.item_cost = item[2]
            print(self.item_name, self.item_description, self.item_cost)
