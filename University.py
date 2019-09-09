# This is a python program that builds a University activites
# I have used Obeject Oriented Programming concepts in Python to implement all of these
class University:
    def __init__(self, name, city, state, major, enrolled):
        self.name = name
        self.city = city
        self.state = state
        self.major = major
        self.enrolled = enrolled

    def fullAddress(self):
        return f"{self.city}, {self.state}"

    def totalStudent(self, year, semester):
        return f"{self.enrolled} are enrolled in {year} {semester}."
    
    def isabove18(self, age):
        if age >= 18:
            return True
        else:
            return False

    def teacherStatus(self, teacher, salary, bonus):
        totalSalary = salary + bonus
        return f"{teacher} takes ${totalSalary} per year."
        
Uni1 = University("The University of Texas at Arlington", "Arlington", "Texas", "Computer Science", 2000)

print(Uni1.fullAddress())
print(Uni1.totalStudent(2019, "Fall"))
print(Uni1.isabove18(20))
print(Uni1.isabove18(16))
print(Uni1.teacherStatus("David Petterson", 1200, 300))