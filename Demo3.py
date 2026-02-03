class cal:
    @staticmethod
    def name(name):
        print(name)

    @staticmethod
    def course(course):
        print(course)

    @staticmethod
    def branch(branch):
        print(branch)

obj = cal()
obj.branch("Full Stack")
obj.course("BCA")
obj.name("Harry")