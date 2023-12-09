class LastDirections:
    def __init__(self):
        self.directions = []

    def add(self,direction):
        if(len(self.directions)<3):
            self.directions.append(direction)

        for i in range(len(self.directions)):
            if(i==0):
                continue
            self.directions[i-1] = self.directions[i]
            if(i == len(self.directions)-1):
                self.directions[i] = direction

    def last(self):
        return self.directions[-1]
    
    def delete(self):
        for i in range(len(self.directions)):
            if(i==0):
                continue
            self.directions[i-1] = self.directions[i]
            if(i == len(self.directions)-1):
                del self.directions[i]


class Direction:
    def __init__(self, direction, time=pygame.time.get_ticks()):
        self.direction = direction
        self.time = time

    def diff_time(self, time) -> int:
        return abs(self.time-time)

        
a = LastDirections()
a.add([1,2])
a.add([1,3])
a.add([1,4])
a.add([1,5])
print(a.directions)