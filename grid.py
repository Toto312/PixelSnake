class Grid:
    def __init__(self, dimensions, size):
        self.dimensions = dimensions
        self.size = size

        self.offset = [0,0]

        self.max = self.ret_grid(self.size)
        self.max[0] -= 1
        self.max[1] -= 1

    def resize(self, limit):
        self.offset = limit[0:2]

    def ret_coord_grid(self, coord):
        return [(coord[0]//self.dimensions[0]) * self.dimensions[0] + self.offset[0], (coord[1]//self.dimensions[1]) * self.dimensions[1] + self.offset[1]]

    def ret_grid(self,coord):
        return [(coord[0]//self.dimensions[0]) + self.offset[0], (coord[1]//self.dimensions[1]) + self.offset[1]]

    def ret_coord_world(self,coord):
        return [coord[0] * self.dimensions[0] + self.offset[0],coord[1] * self.dimensions[1] + self.offset[1]]
    
if(__name__=="__main__"):
    g = Grid([25,25],[500,500])
    g.resize([15,20,500,500])
    print(g.ret_coord_grid([25,0]))
    g.resize([100,10,500,500])
    print(g.ret_coord_grid([25,0]))
