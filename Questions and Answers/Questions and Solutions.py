                                    #1
""""Write a Python code of a program that adds all numbers that are multiples of both 7 and 9 up to
600 (including 600)"""

y = [seven for seven in range(0, 601) if seven % 7==0]
x = [nine for nine in range (0, 601) if nine % 9 == 0]

def intersect(*args):
    res = []
    for x in args[0]:
        for others in args[1:]:
            if x not in others: break
            else:
                res.append(x)
    return res
a = intersect(y, x)
print(sum(a))
                                        #2
"""Write a Python code of a program that adds all numbers that are multiples of **either 7 or 9** up to 
600(including 600).Ensure that numbers like 63 are added only once in the sum."""

def union(*arg):
    res = []
    for seq in arg:
        for x in seq:
            if x not in res:
                res.append(x)
    return res

a = union(y, x)
print(sum(a))
                                        #3
"""Write a Python code to displays all the **odd numbers** between 10 and 50"""
x = [odd for odd in range(10, 51) if odd % 2 == 1]
print(x)

                                        #4
"""Write a Python code of a program that asks the user to enter ten numbers then display the total and the average of
**ONLY** the **odd numbers** among those ten numbers"""
numbers = []
while True:
    print("Enter number " + str(len(numbers) + 1) + " press zero to quit ")
    number = int(input("Enter number: "))
    if number == 0:
        break

    numbers.append(number)

x = [numb for numb in numbers if numb % 2 == 1]
print(x)
print(f"Total numbers: {sum(x)}")
n = len(x)
average = sum(x)/n
print(f"Average is : {average}")


                                            #5
"""Write a Python code for the following:,
* Ask the user to enter a Number, 
* Display the summation of multiples of 7 up to that number (**from 1 to N inclusive**)"""

numbers = int(input("Enter number: "))
x = [numb for numb in range(0, numbers) if numb % 7 == 0]
print(sum(x))


                                            #6
"""Write a Python code to displays all the **odd numbers** between 10 and 50"""

y = [x for x in range(10, 51) if x % 2 == 1]
print(y)


                                            #7
""" Write codes to:
1.	Ask Users to choose what kind of products do they have. Please write what kind of products do you have - fruits(f)
or vegetables(v)?
2.	Depends on what they have - suggest them to chose from your list one specific product.
 For example: for vegetables (Carrots, Lettuce, Mushrooms, Potatoes, Garlic, Cabbages),
  for fruits:(Cucumber, Melons, Tomatoes, Eggplant).
3.	Then show some information about this product (Cooking methods, how to prepare, Availability, Recipes).
Bonus
If user enters a value that is not f or v (fruits(f) or vegetables(v)),
then program should ask to choose the kind of product again until User picks right one.

Depends of plural/singular form of the products - write -Here is information how to prepare it/them

After Users choose what kind of product they interested in, suggest them to chose what kind of information do they want
to know: What to look for/ Cooking methods/ Store / How to prepare / Ways to eat
"""

print("Please what kind of product do you have??")
while True:
    print("Type 'f' for fruits and 'v' for vegetables: ")
    print("\nf - fruits\nv - vegetables")
    product = input("Enter products:  ")
    if product == 'v':
        print("\n Press any number for details on how to produce it ")
        print("We have \n1. Carrots, \n2. Lettuce, \n3. Mushrooms, \n4. Potatoes, "
              "\n5. Garlic, \n6. CabbagesCarrots, \n7. Lettuce, \n8. Mushrooms, \n9. Potatoes, \n10. Garlic, "
              "\n11. Cabbages")
        number = int(input("Enter number: "))
        if number == 3:
            print("\n You chose mushroom, Here is information on how to prepare them: "
                  "\nCultivated mushrooms don't need peeling  \njust wipe both the cap and stalk with a paper towel. "
                  "\nDo not wash. Field mushrooms sometimes need peeling.")

            statement = input("Do you which to continue? ")
            if statement == 'y':
                continue
            elif statement == 'n':
                    break
    if product == 'f':
        print("\n Press any number for details on how to produce the product you choose")
        print("\n We have \n1. Cucumber \n2. Melons \n3. Tomatoes \n4. Eggplant")
        number = int(input("Enter number: "))
        if number == 1:
            print("Here is information how to prepeare it: \n Young cucumbers have a mild and tender skin and,\n"
                  "\nit is unnecessary to peel them. Telegraph, Lebanese and cocktail cucumbers never need to be peeled. "
                  "\nEuropean recipe books may advocate peeling and removing the seeds, but this is not normally necessary")

            statement = input("Do you which to continue? ")
            if statement == 'y':
                continue
            elif statement == 'n':
                break


                                                    #8
"""
Write python program, which prints the following sequences of values in loops
a)24, 18, 12, 6, 0, -6
b)-10, -5, 0, 5, 10, 15, 20
c)18, 27, 36, 45, 54, 63
"""
i = 24
while i >= -6:
    print(i, end=" ")
    i = i - 6

print()
a = -10
while a <= 20:
    print(a, end=",")
    a = a + 5

print()
b = 18
while b <= 63:
    print(b, end=",")
    b = b + 9

print()
c = 18
while c >= -63:
    print(c, end=" ")

                                                    #9
"""
"Write a Python program that asks the user for one number and tells if it is a prime number or not
"""
number = int(input("Enter number: "))
if number % 2 == 1:
    print("It is a prime number")
else:
    print("It is not a prime number")


                                                    #10
""" write a program that check whether your friend's name appear in the list if yes, print his/her age
if no add new friends name and age
"""

friends = {"Tyler": 32, "Jones": 23, "Paul": 37}
while True:
    name = input("Enter friends name: ")
    if name in friends:
        print(f"My friends name is {name} and his age is {friends[name]}")
        print("Do you wish to continue? Y/N")
        reply = input("Enter Y/N: ")
        if reply == "N":
            break
        elif reply == "Y":
            continue
    else:
        print("\nYou are not my friend, so i dont know your age")
        print("Enter your age so i can add you to the list of my friends: ")
        age = int(input("Enter your age: "))
        friends[name] = age
        print("Name and Age added to database")




