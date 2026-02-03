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

obj = maths()
obj.percentage(10)
obj.simple_interset(12,23,35)