"""
Assignment 2

"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from item import Item
from itemlist import ItemList


class ItemsGUI(App):
    def __init__(self, **kwargs):
        super(ItemsGUI, self).__init__(**kwargs)
        self.items = ItemList()

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
        for item in self.items.items:
            temp_button = Button(text=item[0])
            # temp_button.bind(on_release=self.press_entry)
            self.root.ids.itemsBox.add_widget(temp_button)
    #
    # def press_entry(self, instance):
    #     name = instance.text
    #     # self.status_text = Item

    def handle_add_item(self):
        """
        This opens the popup for add items
        :return:
        """
        self.root.ids.popup.open()

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
