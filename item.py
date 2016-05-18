from itemlist import ItemList


class Item:
    def __init__(self, name="", description="", cost=0.0, availability=""):
        self.item_name = name
        self.item_description = description
        self.item_cost = cost
        self.item_availability = availability
