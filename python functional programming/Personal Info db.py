"""
a) Write a little program that allows the user to add a first name and last name of a person
as well as the corresponding body height and place of residence into a dictionary. Fill your
data base by at least 5 entries, and print the dictionary
b) Now ask the user for a name, and either return the body height and place of residence, or a message that it is not
in the data base.
c) Create a function that writes your data base to file, and another function that reads it into memory again.
d) Finally, ask the user for a height, and return a list of all names in your data base that are larger than
the specified height
"""

import csv
info = []
i = 0

#Creating while loop
while i < 5:
    firstName = input("Enter first name: ")
    lastName = input("Enter last name: ")
    bodyHeight = int(input("Enter body height: "))
    country = input("Enter Country: ")
    all = {"First name": firstName, "Last name": lastName, "Body Height": bodyHeight,
           "Country": country}      #Save info inside dictionary
    info.append(all)        #Append all inside info, to form list
    i += 1
print(info)

name = input("Enter your first name: ")
for i in info:
    if name == i["First name"]:
        print("Body Height: " + str(i["Body Height"]) + " Country: " + i["Country"])
        break
    else:
        print("name not in database")


def user_csv():     #creat a csv file
    keys = ["First name", "Last name", "Body Height", "Country"]
    with open('userdata.csv', 'w') as user:
        writer = csv.DictWriter(user, fieldnames=keys)
        writer.writeheader()
        writer.writerows(info)


user_csv()


def csv_convert():
    w = []
    x = []
    with open("userdata.csv") as user:
        reader = csv.reader(user)
        for row in reader:
            w.append(row)

            for i in w[1:]:
                v = {"First name": i[0], "Last name": i[1], "Body Height": int(i[2]), "Country": i[3]}
                x.append(v)
            return x



w = csv_convert()
print(w)

height = int(input("Enter height: "))
for i in w:
    if height < i["Body Height"]:
        print(str(i["Body Height"]))
