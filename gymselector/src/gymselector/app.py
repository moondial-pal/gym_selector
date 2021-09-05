"""
Random climbing gym selector
"""
import random
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, LEFT, RIGHT


def build(app):
    main_box = toga.Box()
    gym_box = toga.Box()

    gym_input = toga.TextInput(readonly=True)

    gym_label = toga.Label('Pull Down Here: ', style=Pack(text_align=LEFT))

    def random_gym(widget):
        d = [
            "Vertical Hold: San Marcos", "Vertical Hold: Old Town", "Vertical Hold: Poway", "Mesa Rim: North",
            "Mesa Rim: San Diego", "Mesa Rim: Mira Mesa", "The Wall", "Vital: Carlsbad", "Vital: Oceanside"
        ]
        select = random.choice(d)
        gym_input.value = select


    button = toga.Button('Choose Gym at Random', on_press=random_gym)

    gym_box.add(gym_label)
    gym_box.add(gym_input)

    main_box.add(gym_box)
    main_box.add(button)

    main_box.style.update(direction=COLUMN, padding_top=10)
    gym_box.style.update(direction=ROW, padding=5)

    gym_input.style.update(flex=1)
    gym_label.style.update(width=100, padding_left=10)

    button.style.update(padding=15, flex=1)

    return main_box


def main():
    return toga.App('Gym Selector', 'org.gym_selector.gs', startup=build)


if __name__ == '__main__':
    main().main_loop()