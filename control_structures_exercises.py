# 1) Conditional Basics

# prompt the user for a day of the week, print out whether the day is Monday or not

user_day = input('What day of the week is it? ')

# could use if user_day.starswith("Mon"):

if user_day == 'monday':
    print('Great, today is monday.')
else:
    print('Today is not monday.')

# prompt the user for a day of the week, print out whether the day is a weekday or a weekend

user_day = input('What day of the week is it? ')

# if user_day == "Saturday" or user_day == "sunday": print(f"{user_day} is a weekend day!") else: print(f"{user_day} is not a weekend.)
# if user_day.lower().startswith('s'): is another way to write the conditional.

if user_day == 'monday':
    print('This is a weekday')
elif user_day == 'tuesday':
    print('This is a weekday')
elif user_day == 'wednesday':
    print('This is a weekday')
elif user_day == 'thursday':
    print('This is a weekday')
elif user_day == 'friday':
    print('This is a weekday')
else:
    print('this is a weekend')

# create variables and make up values for
# the number of hours worked in one week
# the hourly rate
# how much the week's paycheck will be
# write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

number_of_hours_worked = input('how many hours did you work this week? ')
hourly_rate = input('what is your hourly rate? ')
weeks_paycheck = int(number_of_hours_worked) * int(hourly_rate)
overtime_paycheck = (40 * int(hourly_rate)) + ((int(number_of_hours_worked) - 40) * (int(hourly_rate) * 1.5))

if int(number_of_hours_worked) > 40:
    print(overtime_paycheck)
else:
    print(weeks_paycheck)


# Loop Basics

# While

     # Create an integer variable i with a value of 5.
     # Create a while loop that runs so long as i is less than or equal to 15
     # Each loop iteration, output the current value of i, then increment i by one.

i = 5
while i <= 15:
    print(i)
    i += 1


# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.

i = 0
while i <= 100:
    print(i)
    i += 2

# Alter your loop to count backwards by 5's from 100 to -10.

i = 100
while i >= -10:
    print(i)
    i -= 5

# Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:

i = 2
while i <= 1_000_000:
    print(i)
    i = i ** 2 # could also do i *= i which is short-hand for  i = i * i

# Write a loop that uses print to create the output shown below.

i = 100
while i >= 5:
    print(i) # print(f"i: {i}") is another way we could display it
    i -= 5


# For Loops

# Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.

user_number = int(input('please enter your favorite number. '))



for n in range(1, 11):
    print(n, "x", user_number, "=", user_number*n)

#^^^another way to do this:  print(f"{user_numer} x {n} = { user_number * n}")

# Create a for loop that uses print to create the output shown below.

for n in range(10):
    print(str((n))*n)

# print(str(n) * n)
# -------------
# break and continue

# 2) Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. 
# (Hint: use the isdigit method on strings to determine this).
 # Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.

# odd_input = input('please enter an odd number between 1 and 50. ')
#TODO: validate input is right below. when you see "while True", the intent is to create an infinite loop
# it will continuously execute until the user puts in a "true" number
while True:
    user_number = input("please enter an odd number between 1 and 50: ")
    if user_number.isdigit():
        user_number = int(user_number)
        if user_number % 2 == 0: # if it's even
            continue #skip to next loop iteration and run it again
        break
i = 1
while i <= 50:
    if i == user_number:
        print(f" Yikes! SKipping number: {i}")
        i += 2
        continue
    print(f'Here is an odd number: {i}')
    i += 2

# The input function can be used to prompt for input and use that input in your python code.
#  Prompt the user to enter a positive number and write a loop that counts from 0 to that number.
#  (Hints: first make sure that the value the user entered is a valid number, 
# also note that the input function returns a string, so you'll need to convert this to a numeric type.)

while True:
    user_number = input("please enter a positive number between 1 and 50: ")
    if user_number.isdigit():
        user_number = int(user_number)
        if user_number <= 0: # if it's even
            continue #skip to next loop iteration
        break
#- continuously
    # prompt the user for a positive number
    # check if the input is composed of digits, if so
        # convert to a numeric type
        # check if the number is negative or 0
            # if so, go back to square one
        # stop the loop (break)

for i in range(0, user_number + 1):
        print(i)
# Write a program that prompts the user for a positive integer.
#  Next write a loop that prints out the numbers from the number the user entered down to 1.
list(range(10, 1, -1)) #prints the run down from 10 to 1

while True:
    user_number = input("please enter a positive number between 1 and 50: ")
    if user_number.isdigit():
        user_number = int(user_number)
        if user_number <= 0: # if it's even
            continue #skip to next loop iteration
        break
for i in range(user_number, 0 , -1):
        print(i)



# 3) One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.

# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

for n in range(1, 101):
    if (n % 3 == 0) and (n % 5 == 0):
        print('FizzBuzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)

# 4) Display a table of powers.

# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.


# my solution below 
number_chosen = input('what number would you like to see ?  ')
print("Here is your table!")


for n in range(1, (int(number_chosen)+1)):
    print(n, n**2, n**3)

play_again = input('do you want to continue? type Y or N  ')

play_again = play_again.upper()

while play_again == 'Y':

    number_chosen = input('what number would you like to see ?  ')
    for n in range(1, (int(number_chosen)+1)):
        print(n, n**2, n**3)
    play_again = input('do you want to continue? type Y or N  ')

    play_again = play_again.upper()

print('Thank you for your time.')

# instructor solution below

user_input = int(input("Plese enter an integer: "))
print()
print("number | squared | cubed")
print("------ | ------- | -----")

for i in range(1, user_input + 1):
    print("%6d | %7d | %5d" % (i, i**2, i**3))


# 5) Convert given number grades into letter grades.

# Prompt the user for a numerical grade from 0 to 100.
# Display the corresponding letter grade.
# Prompt the user to continue.
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.
# Grade Ranges:

# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0

#instructor solution
#TODO: prompt user for this value
while True:

    numeric_grade = int(input("Please enter a number grade: "))

    # convert to letter

    if numeric_grade >= 88:
        print("A")
    elif numeric_grade >= 80:
        print("B")
    elif numeric_grade >= 67:
        print("C")
    elif numeric_grade >= 60:
        print("D")
    else:
        print("F")

    wants_to_continue = input("Do you want to continue? ")
    if not wants_to_continue.lower().startswith("y"): #could also do, if wants_to_contiue != "yes"
        break






#Bonus

# Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).


# 6 Create a list of dictionaries where each dictionary represents a book that you have read. 
# Each dictionary in the list should have the keys title, author, and genre. 
# Loop through the list and print out information about each book.

# Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.

# look at instructor notebook for #6 solution


 books = [
    {"title": "my life", "author": "Edgar Adams", "genre": "Romance"}
    {key: value, key: value, key: value}
    {key: value, key: value, key: value}
 ]

selected_genre = input("Please enter a genre")
selected_books = [book for book in books if book['genre'] == selected_genre]]


 # for singluar in plural
 # plural variable names indicate a list of things
 # the singular version is one thing from the list
# book
 for book in selected_books:
     print("---")
     print("title: {}".format(book['title'])) # curly braces denote the emtpy value which will be filled in based on user input. .format adjusts how answer looks
     print("author: {}".format(book['author']))
     print("genre: {}".format(book['genre']))
