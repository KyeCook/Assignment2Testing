"""
Assignment 2

"""
from kivy.app import App
from kivy.lang import Builder


class Converter(App):
    def build(self):
        """
        This actually builds and constructs the GUI
        :return: self.root
        """
        self.title = "Equipment Hire"
        self.root = Builder.load_file('GUI.kv')
        return self.root

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

    def handle_take(self):
        mile_minus1 = float(self.root.ids.input_miles.text)
        mile_minus1 -= 1
        self.root.ids.input_miles.text = str(mile_minus1)


Converter().run()
