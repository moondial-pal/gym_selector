"""
Random climbing gym selector
"""
import random
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class GymSelector(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))


        button = toga.Button(
                    'Pick a gym at random',
                    on_press=self.random_gym,
                    style=Pack(padding=5)
        )

        #gym_label = toga.Label("Pull down here: ", text="")

        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def random_gym(self, widget):
        d = [
            "Vertical Hold: San Marcos", "Vertical Hold: Old Town", "Vertical Hold: Poway", "Mesa Rim: North",
            "Mesa Rim: San Diego", "Mesa Rim: Mira Mesa", "The Wall", "Vital: Carlsbad", "Vital: Oceanside"
        ]
        select = random.choice(d)
        print(select)


def main():
    return GymSelector()


