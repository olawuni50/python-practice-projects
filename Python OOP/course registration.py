
"""1)This program allows users to type courses and grades
2) print out all the registered courses
3) print out the total grades
4)print out the number of passed and failed courses
5) calculate the total obtained
6)print out total obtainable
7)calculate the total average
"""


class School:
    def __init__(self):
        self.courses = []               #create list of courses and grades
        self.grades = []

    def calculate_grades_courses(self):
        """allows users to type in courses and grades and save in a list"""

        while True:
            print("Enter course number " + str(len(self.courses) + 1) + " press space bar to stop: ")
            course = input( )
            if course == " ":
                break
            if course in self.courses:
                print("Course already exists")
                continue

            grade = int(input("Enter Grade: " ))
            if grade == " ":
                break

            if grade >= 101:
                print("Grade is out of range")
                continue

            elif grade in range(75, 101):
                print("A1 - Excellent")
            elif grade in range(70, 75):
                print("B2 - Very Good")
            elif grade in range(65, 70):
                print("B3 - Good")
            elif grade in range(60, 65):
                print("C4 - Credit")
            elif grade in range(55, 60):
                print("C5- Credit")
            elif grade in range(50, 55):
                print("C6 - Credit")
            elif grade in range(45, 50):
                print("D7 - Pass")
            elif grade in range(40, 45):
                print("E8 - Pass")
            elif grade in range(0, 40):
                print("F9 - Fail")

            self.grades.append(grade)           #Appends grade to list
            self.courses.append(course)         #Appends course to list

        print("\nList of Courses: ")
        c = [cours for cours in self.courses]
        print(c)                                    #lists all courses entered

        print("List of Grades: ")
        g = [grad for grad in self.grades]
        print(g)                                    #lists all grades entered

        d = dict(zip(c, g))
        print(d)                                    #convert lists to dictionary

        print("\nList of Passed Courses: ")
        for key, value in d.items():
            if value >= 50:                         #list all passed courses
                print(key)

        print("\nList of Failed Courses: ")
        for key, value in d.items():
            if value < 50:                          #list all failed courses
                print(key)

    def total_obtained(self):
        """calculate total obtained"""
        sum(self.grades)
        return (sum(self.grades))

    def total_obtainable(self):
        """calculate total obtainable"""
        return len(self.courses) * 100

    def total_average(self):
        return (self.total_obtained()/self.total_obtainable()) * 100

if __name__ =="__main__":
    x = School()
    x.calculate_grades_courses()
    print(f"Total Obtained: {x.total_obtained()}")
    print(f"Total Obtainable: {x.total_obtainable()}")
    print(f"Total Average: {x.total_average()}")
