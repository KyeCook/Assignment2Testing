from Assign1 import load_items
from item import Item


class ItemList:
    def __init__(self):
        self.items = []
        items = load_items()
        for item_list in items:
            # create Item object, put in self.items
            item = Item(item_list[0], item_list[1], float(item_list[2]), item_list[3])
            self.items.append(item)

    def add_item_from_values(self, added_name, added_description, added_price):
        item = Item(added_name, added_description, float(added_price), "in")
        self.items.append(item)

    def get_item(self, name):
        for item in self.items:
            if item.name == name:
                return item
