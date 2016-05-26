

class Item:
    def __init__(self, name, description, cost, in_or_out):
        """
    Gets Item attributes and creates item objects from said attributes
        :param name:
        :param description:
        :param cost:
        :param in_or_out:
        :return:
        """
        self.name = name
        self.description = description
        self.cost = cost
        self.in_or_out = in_or_out
