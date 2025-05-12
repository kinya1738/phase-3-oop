class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks


class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students= []

    def add_student(self, student):
        self.students.append(student)

    def course_average(self):
            count = 0
            for student in self.students:
                count += student.marks
            return count / len(self.students)

         

#creating student instances

student1 = Student("Mark", 20, 82)
student2 = Student("Fiona", 19, 45)
student3 = Student("Alex", 21, 73)   

# creating course instance
c= Course("Design")

# adding students to the course
c.add_student(student1)
c.add_student(student2)
c.add_student(student3)

# for student in c.students:
#     print(student.name)

c.course_average()   




