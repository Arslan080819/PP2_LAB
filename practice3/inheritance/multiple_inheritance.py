class Father:
    def skills(self):
        print("Programming")

class Mother:
    def hobbies(self):
        print("Design")

class Child(Father, Mother):
    pass

child = Child()
child.skills()
child.hobbies()
