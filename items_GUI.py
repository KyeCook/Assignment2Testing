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
CONFIRM_MODE = 3
ADD_ITEM_MODE = 4


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

    def press_entry(self, instance):
        """
        This class function changes the text notification within the bottom status label
        :param instance: --> instance is derived from the 'create_item_buttons' function
        :return:
        """
        item_name = instance.text

        selected_item = None

        # TODO change to method of itemlist getitem(name)
        for item in self.items.items:
            if item.name == item_name:
                selected_item = item

        if self.mode == LIST_MODE:
            self.status_text = "{} ({}) = ${:.2f} is {}".format(selected_item.name, selected_item.description,
                                                                selected_item.cost, selected_item.in_or_out)

        if self.mode == HIRE_MODE:
            if selected_item.in_or_out == "in":
                if selected_item not in self.selected_items:
                    self.selected_items.append(selected_item)

                    names = []
                    total = 0
                    for item in self.selected_items:
                        total += item.cost
                        names.append(item.name)

                    # self.root.ids.list_items_btn.state = "down"
                    # print(total)
                    name_str = ",".join(names)
                    self.status_text = "Hiring : {} for ${:.2f}".format(name_str, total)
                else:
                    self.selected_items.remove(selected_item)
            # print(self.mode, self.status_text)

    def handle_list_items(self):
        self.mode = LIST_MODE
        self.root.ids.list_items_btn.state = "down"
        self.root.ids.hire_items_btn.state = "normal"
        self.root.ids.return_items_btn.state = "normal"
        self.root.ids.confirm_btn.state = "normal"
        self.root.ids.add_item_btn.state = "normal"

    def handle_hire_item(self):
        self.mode = HIRE_MODE
        self.root.ids.list_items_btn.state = "normal"
        self.root.ids.hire_items_btn.state = "down"
        self.root.ids.return_items_btn.state = "normal"

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
