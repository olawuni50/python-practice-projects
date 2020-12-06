import csv

#Empty list
courses, grades = [], []


def courses_grades():
    """
    Allows teachers to enter courses and grades of students
    :return:
    """
    while True:
        print("Enter course number " + str(len(courses) + 1) + " press space bar to quit ")
        course = input( )
        if course == " ":
            break
        if course in courses:
            print("Course already exists")
            continue
        grade = int(input("Enter " + course + " grade: " ))
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

        grades.append(grade)
        courses.append(course)
    print("\nLists of courses: ")
    c = [cours for cours in courses]
    print(c)

    print("\nLists of grades")
    g = [grad for grad in grades]
    print(g)

    d = dict(zip(c, g))     # convert lists to dictionary
    print(d)

    print("\nList of Passed Courses: ")
    for key, value in d.items():
        if value >= 50:
            print(key.title())

    print("\nList of Failed Courses")
    for key, value in d.items():
        if value < 50:
            print(key.title())


def total_obtained():
    sum(grades)
    return (sum(grades))


def total_obtainable():
    return len(courses) * 100


def total_average():
    return round(total_obtained()/ total_obtainable() * 100, 1)


def write_csv():
     with open("C:\\Users\\olawuni ayodeji\\Desktop\\myDocs\\csvcsvcourse.csv", 'w', newline="") as write:
        fileWrite = csv.writer(write)
        fileWrite.writerow(courses)
        fileWrite.writerow(grades)

        write.close()

def read_csv():
    w = []
    with open("C:\\Users\\olawuni ayodeji\\Desktop\\myDocs\\csvcourse.csv", 'r') as read:
        fileRead = csv.reader(read)
        for file in fileRead:
            w.append(file)

        return w



if __name__ == "__main__":
    courses_grades()
    print(f"\nTotal Obtained: {total_obtained()}")
    print(f"\nTotal Obtainable: {total_obtainable()}")
    print(f"\nTotal average: {total_average()}")
    print(write_csv())
    print(read_csv())


