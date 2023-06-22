import math

keypad_grid_size = int(input("Grid size: 300, 150, 75: ")) / 3

while True:

    y = int(input("Y keypad grids: "))
    x = int(input("X keypad grids: "))

    class Mortar:
        def __init__(self, y, x):
            self.y = y
            self.x = x

        def calculate_distance(self):
            squared_y = self.y ** 2
            squared_x = self.x ** 2
            squared_add_total = squared_y + squared_x
            squared_root = round(math.sqrt(squared_add_total), 2)
            return round(squared_root * keypad_grid_size)


    distance = Mortar(y, x)
    print(distance.calculate_distance())
