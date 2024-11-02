class IOString():
    def __init__(self):
        self.st1=''
    def getString(self):
        self.st1=input('Enter String: ')
    def display(self):
        print('String is',self.st1.upper())
o1=IOString()
o1.getString()
o1.display()