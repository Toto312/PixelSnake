class Hello:
    def __init__(self):
        self.a = 1

a = Hello()

b = [a,1]

b[0].a = 4
print(a.a)