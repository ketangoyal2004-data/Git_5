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

    def country(self,country):
        self.country = country
        print(self.country)

    def collegename(self,name):
        self.name = name
        print('collegename = ',self.name)



obj = std()
obj.name("Ketan goyal")
obj.course("BCA")
obj.city("Jaipur")
obj.branch("Full Stack")
obj.country("India")
obj.collegename('Apex university')