

class Grid:
    def __init__(self, size):
        self.size = size

    def ret_coord_grid(self, coord):
        return [(coord[0]//self.size[0]) * self.size[0], (coord[1]//self.size[1]) * self.size[1]]

    def ret_grid(self,coord):
        return [(coord[0]//self.size[0]), (coord[1]//self.size[1])]

    def ret_coord_world(self,coord):
        return [coord[0] * self.size[0],coord[1] * self.size[1]]