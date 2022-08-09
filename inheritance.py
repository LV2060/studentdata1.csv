class Parent:
    def __init__(self,txt):
        self.message =txt
    def printmessage(self):
            print(self.message)
class Child(Parent):
    def __int__(self, txt):
        super().__int__(txt)
x=Child("Hello,and welcome!")
x.printmessage()

