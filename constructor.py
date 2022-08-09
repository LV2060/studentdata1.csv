  class KLU:
    def __init__(self, name, id):  # Parameterized Constructor
        self.id = id
        self.name = name

    def display(self):
        print("ID: %d \nName: %s" % (self.id, self.name))
obj1 = KLU("Vijaya", 101)
obj2 = KLU("Vardhini", 102)
obj1.display()
obj2.display()