import random


class Line:

    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class React:

    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:

    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


elements = []
classes = [Line, React, Ellipse]
for _ in range(217):
    elements.append(random.choice(classes)(random.randint(50, 100), random.randint(50, 100), random.randint(0, 50),
                                           random.randint(0, 50)))


for object in elements:
    if type(object) is Line:
        object.sp = (0, 0)
        object.ep = (0, 0)

