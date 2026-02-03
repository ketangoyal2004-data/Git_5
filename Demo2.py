class std:
    def name(self,name):
        self.name = name
        print(self.name)

    def course(self,course):
        self.course = course
        print(self.course)

    def city(self,city):
        self.city = city
        print(self.city)

    def branch(self,branch):
        self.branch = branch
        print(self.branch)

obj = std()
obj.name("Ketan goyal")
obj.course("BCA")
obj.city("Jaipur")
obj.branch("Full Stack")