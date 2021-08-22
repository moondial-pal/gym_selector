"""
Random climbing gym selector
"""
import random
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW



class HelloWorld(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        button = toga.Button(
                    'Pick a gym at random',
                    on_press=self.random_gym,
                    style=Pack(padding=5)
        )

        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def random_gym(self, widget):
        d = [
            "vertical_hold", "mesa_rim", "the_wall", "vital",
        ]
        select = random.choice(d)
        print(select)

def main():
    return HelloWorld()


