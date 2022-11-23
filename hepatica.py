from plant import Plant


class Hepatica(Plant):

    def __init__(self, name, height, colour, month, soil, place):
        super().__init__(name, height, colour)
        self.month = month
        self.soil = soil
        self.place = place

    #def print_info(self):
        #print(f'One of the varieties of plant is {self.name}, {self.height} centimetres and with '
              #f'{self.get_colour()} flowers.')

    def blooms(self):
        print(f'{self.name} blooms in {self.month}.')

    def type_of_soil(self):
        print(f'This variety of the plant is better to grow in {self.soil}.')

    def place_to_put(self):
        print(f'It is recommended to put in {self.place}.')








