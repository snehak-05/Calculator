from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
import math

Window.clearcolor = (0.9, 0.9, 1, 1)
Window.size = (360, 400)

class MyCalculatorApp(App):
    def build(self):
        self.icon="calculator2.jpg"
        self.expression = ""  # Store user input
        layout = GridLayout(cols=4, rows=6)
        layout2 = BoxLayout(orientation="vertical", padding=10)

        # Button texts and colors
        buttons = [
            ["%", "x³", "C", "del"], ["1/x", "x²", "√x", "/"], 
            ["7", "8", "9", "*"], ["4", "5", "6", "-"], 
            ["1", "2", "3", "+"], ["+/-", "0", ".", "="]
        ]
        colors = {"/": (1, 1, 1, 0.5), "*": (1, 1, 1, 0.5), "-": (1, 1, 1, 0.5), "+": (1, 1, 1, 0.5),
                  "=": (1, 0, 0, 1), "default": (0, 0, 1, 0.5)}

        # Text input (display screen)
        self.scn = TextInput(text="0", size_hint=(1, 0.3), readonly=True, background_normal="", 
                             background_color=(1, 1, 1, 1), foreground_color=(0, 0, 0, 1), font_size=32)
        layout2.add_widget(self.scn)

        # Add buttons dynamically
        for row in buttons:
            for text in row:
                btn_color = colors.get(text, colors["default"])
                btn = Button(text=text, background_color=btn_color, font_size=24)
                btn.bind(on_press=self.on_button_press)
                layout.add_widget(btn)

        layout2.add_widget(layout)
        return layout2

    def on_button_press(self, instance):
        text = instance.text

        if text == "C":  # Clear screen
            self.expression = ""
        elif text == "x³":
            try:
                self.expression = str(float(self.expression) ** 3)
            except:
                self.expression = "Error"
        elif text == "del":  # Delete last character
            self.expression = self.expression[:-1]
        elif text == "=":  # Evaluate expression
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "Error"
        elif text == "x²":  # Square
            try:
                self.expression = str(float(self.expression) ** 2)
            except:
                self.expression = "Error"
        elif text == "√x":  # Square root
            try:
                self.expression = str(math.sqrt(float(self.expression)))
            except:
                self.expression = "Error"
        elif text == "1/x":  # Reciprocal
            try:
                self.expression = str(1 / float(self.expression))
            except:
                self.expression = "Error"
        elif text == "%":  # Percentage
            try:
                self.expression = str(float(self.expression) / 100)
            except:
                self.expression = "Error"
        elif text == "+/-":  # Change sign
            try:
                self.expression = str(-1 * float(self.expression))
            except:
                self.expression = "Error"
        else:
            self.expression += text

        self.scn.text = self.expression if self.expression else "0"

MyCalculatorApp().run()
