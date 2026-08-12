class Employee:
    def __init__(self):
        self.id = 123
        self.salary = 50000
        self.designation = "SD"

#Function
    def travel(self, destination):
        print(f"Employee is now travelling to {destination}")

#Object Creation
sam = Employee()
print(sam.id)
sam.travel("Gazipur")