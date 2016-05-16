from Assign1 import load_items


class Item:
    def __init__(self, items=""):
        items = items
        imported_items = load_items()
        print(imported_items[3])

