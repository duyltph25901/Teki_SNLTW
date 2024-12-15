class Student:
    def __init__(self, id, studentName, age, address, avgPoint):
        self.id = id
        self.studentName = studentName
        self.age = age
        self.address = address
        self.avgPoint = avgPoint

    def toString(self): 
        return f"{self.id} | {self.studentName} | {self.age} | {self.address} | {self.avgPoint}"