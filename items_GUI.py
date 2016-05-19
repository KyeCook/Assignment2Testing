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
from item import Item
from itemlist import ItemList


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
        self.testing = Item()
        self.items = ItemList()
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
            temp_button = Button(text=item[0])
            temp_button.bind(on_release=self.press_entry)
            self.root.ids.itemsBox.add_widget(temp_button)

    def press_entry(self, instance):
        """
        This class function changes the text notification within the bottom status label
        :param instance: --> instance is derived from the 'create_item_buttons' function
        :return:
        """
        item_name = instance.text
        self.status_text = item_name

        # self.status_text = "{} ({}) = $ {}{}".format(item_name, self.items.items[1], self.items.items[2],
        #                                              self.items.items[3])

    def handle_add_item(self):
        """
        This opens the popup for add items
        :return:
        """
        self.root.ids.popup.open()

    # def handle_save_item(self, added_name, added_number):
    #     """
    #     Handler for pressing the save button in the add entry popup - save a new entry to memory
    #     :param added_name: name text input (from popup GUI)
    #     :param added_number: phone number text input (string)
    #     :return: None
    #     """
    #     self.phonebook[added_name] = added_number
    #     # change the number of columns based on the number of entries (no more than 5 rows of entries)
    #     self.root.ids.entriesBox.cols = len(self.phonebook) // 5 + 1
    #     # add button for new entry (same as in create_entry_buttons())
    #     temp_button = Button(text=added_name)
    #     temp_button.bind(on_release=self.press_entry)
    #     self.root.ids.entriesBox.add_widget(temp_button)
    #     close popup
    #     self.root.ids.popup.dismiss()
    #     self.clear_fields()

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
