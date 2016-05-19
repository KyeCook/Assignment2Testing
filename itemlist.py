from Assign1 import load_items


class ItemList:
    def __init__(self):
        self.items = load_items()
        # print(self.items)

    def __str__(self):
        # Formats 2 variables into one to achieve same formatting as examples
        # for number in self.name:
        #     print(number)
        #     return(number)

        string_for_formatting = "{} ({})".format(self.name[0], self.description[0],)
        # Actually applies formatting to items contents
        return ("{:<40s} = $ {:>7.2f}{}".format(string_for_formatting,self.cost[0],
                                                self.availability[0]))