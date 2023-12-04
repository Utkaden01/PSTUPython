class Manipulator:
    def __init__(self, length, angle):
        self.length = length
        self.angle = angle

    def move(self, angle):
        self.angle = angle

    def __add__(self, other):
        if isinstance(other, Manipulator):
            return Manipulator(self.length + other.length, self.angle + other.angle)
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Manipulator):
            return Manipulator(self.length - other.length, self.angle - other.angle)
        else:
            return NotImplemented

    def __mul__(self, scalar):
        return Manipulator(self.length * scalar, self.angle * scalar)

    def __truediv__(self, scalar):
        return Manipulator(self.length / scalar, self.angle / scalar)

    def __neg__(self):
        return Manipulator(-self.length, -self.angle)


class link1(Manipulator):
    def __init__(self, length, angle):
        super().__init__(length, angle)


class link2(Manipulator):
    def __init__(self, length, angle):
        super().__init__(length, angle)


class link3(Manipulator):
    def __init__(self, length, angle):
        super().__init__(length, angle)


class link4(Manipulator):
    def __init__(self, length, angle):
        super().__init__(length, angle)


class link5(Manipulator):
    def __init__(self, length, angle):
        super().__init__(length, angle)


class link6(Manipulator):
    def __init__(self, length, angle):
        super().__init__(length, angle)


link1 = link1(10, 0)
link2 = link2(8, 45)
link3 = link3(7, 60)
link4 = link4(5, 75)
link5 = link5(4, 80)
link6 = link6(3, 30)

link1.move(90)
link2.move(60)
link3.move(90)
link4.move(60)
link5.move(90)
link6.move(60)

print(link1.angle)
print(link2.angle)
print(link3.angle)
print(link4.angle)
print(link5.angle)
print(link6.angle)

link7 = link1 + link2
print(link7.length, link7.angle)

link8 = link3 - link4
print(link8.length, link8.angle)

link9 = link5 * 2
print(link9.length, link9.angle)

link10 = link6 / 2
print(link10.length, link10.angle)

link11 = -link1
print(link11.length, link11.angle)
