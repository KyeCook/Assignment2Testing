"""
Assignment 2 Testing work

Need to find out :
    > How to centre align widgets
"""
from kivy.app import App
from kivy.lang import Builder


class Converter(App):
    def build(self):
        self.title = "Equipment Hire"
        self.root = Builder.load_file('gui_addItems.kv')
        # self.root = Builder.load_file('gui_mainMenu.kv')
        return self.root

    def handle_convert(self):
        miles = float(self.root.ids.input_miles.text)
        kilometers = miles/0.62137
        if kilometers > 1:
            is_plural = "s"
        else:
            is_plural = ""
        self.root.ids.output_label.text = "{:.2f}km{}".format(kilometers, is_plural)

    def handle_add(self):
        mile_plus1 = float(self.root.ids.input_miles.text)
        mile_plus1 +=1
        self.root.ids.input_miles.text = str(mile_plus1)

    def handle_take(self):
        mile_minus1 = float(self.root.ids.input_miles.text)
        mile_minus1 -=1
        self.root.ids.input_miles.text = str(mile_minus1)


Converter().run()
