class Area:
    @staticmethod
    def square(a):
        print(a * a)

    @staticmethod
    def Rectangle(l,b):
        Area = l * b
        print(Area)

    @staticmethod
    def triangle(b,h):
        tri = 0.5 * b * h
        print(tri)

    @staticmethod
    def circle(r):
        pie = 22 / 7
        r = r * 2
        Area = pie * r
        print(Area)

obj = Area()
obj.Rectangle(10)
obj.square(12,3)
obj.triangle(12,3)
obj.circle(12)