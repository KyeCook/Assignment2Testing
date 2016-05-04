from kivy.app import App
from kivy.lang import Builder


class Converter(App):
    def build(self):
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('kivy_testing.kv')
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