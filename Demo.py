class cal:
    def add(self,a,b):
        self.a = a
        self.b = b
        print("a + b = ",self.a + self.b)

    def sub(self,a,b):
        self.a = a
        self.b = b
        print("a - b = ",self.a - self.b)

    def mul(self,a,b):
        self.a = a
        self.b = b
        print("a * b = ",self.a * self.b)

    def div(self,a,b):
        self.a = a
        self.b = b
        print("a / b = ",self.a / self.b)

    def exp(self,a):
        self.a = a
        return a ** 2
    
    def pow(self,a):
        self.a = a
        return self.a % 2

obj = cal()
obj.add(101,2)
obj.sub(12,2)
obj.mul(102,2)
obj.div(12,3)
obj.exp(12)
obj.pow(12)