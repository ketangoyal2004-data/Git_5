class maths:
    def percentage(self,part,whole):
        self.part = part
        self.whole = whole
        precentage = self.part / self.whole * 100
        print(precentage)

    def simple_interset(self,profit,Rate,Time):
        self.profit = profit
        self.rate = Rate
        self.Time = Time
    
    print("This is a time was accept of month not year")
        
    SI = self.profit * self.rate * self.Time / 100
    print(SI)

    def square_number(self,a,b):
        self.a = a
        self.b = b
        a2 = self.a * 2
        b2 = self.b * 2
        two_ab = 2 * self.a * self.b
        square_a_b = a2 + two_ab + b2
        print(square_a_b)

obj = maths()
obj.percentage(10)
obj.simple_interset(12,23,35)
obj.square_number(10,20)