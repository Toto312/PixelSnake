

class Grid:
    def __init__(self, size):
        self.size = size

    def ret_coord_grid(self, coord):
        return [(coord[0]//self.dimensions[0]) * self.dimensions[0], (coord[1]//self.dimensions[1]) * self.dimensions[1]]

    def ret_grid(self,coord):
        return [(coord[0]//self.dimensions[0]), (coord[1]//self.dimensions[1])]

    def ret_coord_world(self,coord):
        return [coord[0] * self.dimensions[0],coord[1] * self.dimensions[1]]