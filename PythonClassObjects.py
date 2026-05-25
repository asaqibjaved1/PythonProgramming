# Python class and object 
class teacher:
    name = "Saqib"
    personnal = "0000979165"
    mobile = "0312-------"

teacher1 = teacher()
print(teacher1.name)
print(teacher1.personnal)
print(teacher1.mobile)

class teacher: 
    def __init__(self, name, number):
        self.name = name
        self.number = number
    def marks(self):
        print(self.number)
        # Static method 
    @staticmethod
    def msg():
        print("Hello Students")

t1 = teacher("Zulfi", 90)
print(t1.name)
t1.marks()
t1.msg()






