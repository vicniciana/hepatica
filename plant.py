class Plant:
    def __init__(self, name='plant', height='height', colour='colour'):
        self.name = name
        self.height = height
        self.__colour = colour

    #def print_info(self):
        #print(f'One of the varieties of plant is {self.name}, {self.height} centimetres and {self.colour}.')

    def print_info(self):
        print(f'One of the varieties of plant is {self.name}, {self.height} centimetres and '
              f'{self.get_colour()}.')

    def get_colour(self):
        return self.__colour if self.__colour else None

    def set_colour(self, colour):
        self.__colour = colour



