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






    
