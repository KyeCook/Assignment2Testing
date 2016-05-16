from Assign1 import load_items


class Item:
    def __init__(self, items_id=0, name="", description="", cost=0.0, availability=""):
        self.item_id = items_id
        self.item_name = name
        self.item_description = description
        self.item_cost = cost
        self.item_availability = availability

        items = load_items()
        self.item_id = items[0]
        self.name = items[1]
        self.description = items[2]
        self.cost = items[3]
        self.availability = items[4]


    def __str__(self):
        # Formats 2 variables into one to achieve same formatting as examples
        # for number in self.name:
        #     print(number)
        #     return(number)

        string_for_formatting = "{} ({})".format(self.name[0], self.description[0],)
        # Actually applies formatting to items contents
        return ("{:<40s} = $ {:>7.2f}{}".format(string_for_formatting,self.cost[0],
                                                self.availability[0]))
