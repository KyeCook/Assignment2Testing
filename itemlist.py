from Assign1 import load_items
from item import Item


class ItemList:
    def __init__(self):
        """
        Loads items from csv file using methods from previous assignment
        :return:
        """
        self.items = []
        items = load_items()
        for item_list in items:
            # create Item object, put in self.items
            item = Item(item_list[0], item_list[1], float(item_list[2]), item_list[3])
            self.items.append(item)

    def add_item_from_values(self, added_name, added_description, added_price):
        """
        Allows for new items added to be imported into item lists
        :param added_name:
        :param added_description:
        :param added_price:
        :return:
        """
        item = Item(added_name, added_description, float(added_price), "in")
        self.items.append(item)

    def get_item(self, name):
        """
        Allows for items to be found via name and exported to function that calls get_item
        :param name:
        :return:
        """
        for item in self.items:
            if item.name == name:
                return item

    def get_items_for_saving(self):
        """
        Constructs final lists to return to main for exporting to csv file
        :return:
        """

        items_to_save = []

        for item in self.items:
            f = (item.name, item.description, item.cost, item.in_or_out)
            items_to_save.append(f)
        return items_to_save
