"""
Assignment 2
Kye Cook
started 04/05/2016

GitHub URL : https://github.com/KyeCook/Assignment2_KivyAndClasses

Program uses past assignment and converts into usable GUI using classes and kivy
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from itemlist import ItemList

LIST_MODE = 0
HIRE_MODE = 1
RETURN_MODE = 2


class ItemsGUI(App):

    # This status text is a label that changes dynamically depending on item selected. Default value is within __init__
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """
        Initializer for app class - allows for other classes to be imported and declared
        :param kwargs:
        :return:
        """
        super(ItemsGUI, self).__init__(**kwargs)
        self.items = ItemList()
        self.mode = LIST_MODE
        self.selected_items = []
        self.status_text = "Choose action from the left menu, then select items on the right"

    def build(self):
        """
        This actually builds and constructs the GUI
        :return: self.root
        """
        self.title = "Equipment Hire"
        self.root = Builder.load_file('GUI.kv')
        self.create_item_buttons()
        return self.root

    def create_item_buttons(self):
        """
        This class function dynamically builds and constructs the buttons dependant upon how many items are within the
        CSV file
        :return:
        """
        for item in self.items.items:
            temp_button = Button(text=item.name)
            temp_button.bind(on_release=self.press_entry)
            self.root.ids.itemsBox.add_widget(temp_button)
            if item.in_or_out == "out":
                temp_button.background_color = (1.0, 0.0, 0.0, 1.0)

    def press_entry(self, instance):
        """
        This class function changes the text notification within the bottom status label
        :param instance: --> instance is derived from the 'create_item_buttons' function
        :return:
        """
        item_name = instance.text

        item = self.items.get_item(item_name)
        if self.mode == LIST_MODE:
            self.status_text = "{} ({}) = ${:.2f} is {}".format(item.name, item.description, item.cost, item.in_or_out)

        elif self.mode == HIRE_MODE:
            if item.in_or_out == "in":
                if item not in self.selected_items:
                    self.selected_items.append(item)
                    instance.state = "down"

                    names = []
                    total_cost = 0

                    for item in self.selected_items:
                        total_cost += item.cost
                        names.append(item.name)

                    name_str = ",".join(names)
                    self.status_text = "Hiring : {} for ${:.2f}".format(name_str, total_cost)
                else:
                    self.selected_items.remove(item)
                    instance.state = "normal"

        elif self.mode == RETURN_MODE:
            if item.in_or_out == "out":
                if item not in self.selected_items:
                    self.selected_items.append(item)
                    instance.state = "down"

                    names = []
                    for item in self.selected_items:
                        names.append(item.name)

                    name_str = ",".join(names)
                    self.status_text = "Returning : {}".format(name_str)
                else:
                    self.selected_items.remove(item)
                    instance.state = "normal"


    def handle_list_items(self):
        self.selected_items = []
        self.status_text = "Choose action from the left menu, then select items on the right"
        self.mode = LIST_MODE
        self.root.ids.list_items_btn.state = "down"
        self.root.ids.hire_items_btn.state = "normal"
        self.root.ids.return_items_btn.state = "normal"

    def handle_hire_item(self):
        self.selected_items = []
        self.status_text = "Select available items to hire"
        self.mode = HIRE_MODE
        self.root.ids.list_items_btn.state = "normal"
        self.root.ids.hire_items_btn.state = "down"
        self.root.ids.return_items_btn.state = "normal"

    def handle_return_item(self):
        self.selected_items = []
        self.status_text = "Select available items to return"
        self.mode = RETURN_MODE
        self.root.ids.list_items_btn.state = "normal"
        self.root.ids.hire_items_btn.state = "normal"
        self.root.ids.return_items_btn.state = "down"

    def handle_confirm(self):
        self.root.ids.list_items_btn.state = "normal"
        self.root.ids.hire_items_btn.state = "normal"
        self.root.ids.return_items_btn.state = "normal"

        for item in self.selected_items:
            if self.mode == HIRE_MODE:
                item.in_or_out = "out"
            elif self.mode == RETURN_MODE:
                item.in_or_out = "in"
        self.mode = LIST_MODE

    def handle_add_item(self):
        """
        This opens the popup for add items
        :return:
        """
        self.root.ids.popup.open()

    def handle_save_item(self):
        added_name = self.root.ids.added_name.text
        added_description = self.root.ids.added_description.text
        added_price = self.root.ids.added_price.text

        self.items.add_item_from_values(added_name, added_description, added_price)
        # # change the number of columns based on the number of entries (no more than 5 rows of entries)
        # self.root.ids.entriesBox.cols = len(self.items.items) // 5 + 1
        # # add button for new entry (same as in create_entry_buttons())
        temp_button = Button(text=added_name)
        temp_button.bind(on_release=self.press_entry)
        self.root.ids.itemsBox.add_widget(temp_button)
        # closes popup
        self.root.ids.popup.dismiss()
        self.clear_fields()

    def clear_fields(self):
        """
        This clears inputted data from add group if cancel button is clicked.
        :return:
        """
        self.root.ids.added_name.text = ""
        self.root.ids.added_description.text = ""
        self.root.ids.added_price.text = ""

    def handle_cancel(self):
        """
        This handles the actions of the cancel button within the add group
        :return: none
        """
        # closes the popup window
        self.root.ids.popup.dismiss()
        self.clear_fields()


ItemsGUI().run()
