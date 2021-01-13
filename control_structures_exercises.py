# 1) Conditional Basics

# prompt the user for a day of the week, print out whether the day is Monday or not

user_day = input('What day of the week is it? ')

if user_day == 'monday':
    print('Great, today is monday.')
else:
    print('Today is not monday.')

# prompt the user for a day of the week, print out whether the day is a weekday or a weekend

user_day = input('What day of the week is it? ')


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
while i < 1_000_000:
    print(i)
    i = i ** 2

# Write a loop that uses print to create the output shown below.

i = 100
while i >= 5:
    print(i)
    i -= 5


# For Loops

# Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.

user_number = int(input('please enter your favorite number? '))



for n in range(1, 11):
    print(n, "x", user_number, "=", user_number*n)

# Create a for loop that uses print to create the output shown below.

for n in range(10):
    print(str((n))*n)

# break and continue

# Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. 
# (Hint: use the isdigit method on strings to determine this).
 # Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.

odd_input = input('please enter an odd number between 1 and 50. ')

while number in odd_input:
    print('this is an invalid input')
    if int(number) % 2 == 0 or (int(number) > 50 or int(number) < 1):
        break

# Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.

other_odd_input = int(input('please enter an odd number between 1 and 50. '))

for n in range(0, 51):
    if n != other_odd_input and n % 2 == 0:
        continue
    print('Here is an odd number: {}'.format(n))

