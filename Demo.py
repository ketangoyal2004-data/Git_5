class cal:
    def add(self,a,b):
        self.a = a
        self.b = b
        print("a + b = ",self.a + self.b)

    def sub(self,a,b):
        self.a = a
        self.b = b
        print("a - b = ",self.a - self.b)

obj = cal()
obj.add(101,2)
obj.sub(12,2)