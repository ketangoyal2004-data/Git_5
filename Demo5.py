class vol:
    def cube(self,a):
        self.a = a
        v = self.a * self.a * self.a
        print(v)

    def cuboid(self,l,b,h):
        self.l = l
        self.b = b
        self.h = h
        cuboid = self.l * self.b * self.h
        print(cuboid)

obj = vol()
obj.cube(10)
obj.cuboid(5)