fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Exercise 1 - rewrite the above example code using list comprehension syntax. 
# Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]

uppercased_fruits = [fruit.upper() for fruit in fruits]

print(uppercased_fruits)

# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]

capitalized_fruits = [fruit.title() for fruit in fruits]
print(capitalized_fruits)

other_captial_fruits = [fruit.capitalize() for fruit in fruits]
print(other_captial_fruits)

# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.

def is_vowel(string):
    string = string.lower()
    return string in ['a', 'e', 'i', 'o', 'u']

def count_vowels(string):
    count = 0
    for letter in string:
        if is_vowel(letter):
            count += 1
    return count
print(count_vowels('guava'))

fruits_with_more_than_two_vowels= [fruit for fruit in fruits if count_vowels(fruit) > 2]

print(fruits_with_more_than_two_vowels)

[fruit for fruit in fruits if (fruit.count("a")
 + fruit.count("e")
 + fruit.count("i")
 + fruit.count("o")
 + fruit.count("u")) > 2]

# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']


fruits_with_only_two_vowels = [fruit for fruit in fruits if count_vowels(fruit) == 2]

print(fruits_with_only_two_vowels)

# Exercise 5 - make a list that contains each fruit with more than 5 characters

big_fruit = [fruit for fruit in fruits if len(fruit) > 5]

print(big_fruit)

# Exercise 6 - make a list that contains each fruit with exactly 5 characters

exact_fruit = [fruit for fruit in fruits if len(fruit) == 5]

print(exact_fruit)

# Exercise 7 - Make a list that contains fruits that have less than 5 characters

less_fruit = [fruit for fruit in fruits if len(fruit) < 5]

print(less_fruit)

# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]

counted_fruits = [len(fruit) for fruit in fruits]

print(counted_fruits)

# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"

fruits_with_letter_a = [fruit for fruit in fruits if 'a' in fruit]

print(fruits_with_letter_a)

# Exercise 10 - Make a variable named even_numbers that holds only the even numbers

even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers

odd_numbers = [number for number in numbers if number % 2 == 1]

print(odd_numbers)

# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers

positive_numbers = [number for number in numbers if number > 0]

print(positive_numbers)

# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers

negative_numbers = [number for number in numbers if number < 0]

print(negative_numbers)

# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals

two_or_more_numeral = [number for number in numbers if abs(number) >= 10]

print(two_or_more_numeral)

# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]

numbers_squared = [number ** 2 for number in numbers]

print(numbers_squared)

# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.

odd_negative_numbers = [number for number in numbers if number % 2 == 1 and number < 0]

print(odd_negative_numbers)

# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five.

numbers_plus_5 = [number + 5 for number in numbers]

print(numbers_plus_5)

# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. 
# *Hint* you may want to make or find a helper function that determines if a given number is prime or not.


def prime(number):
    if number > 1:
        for i in range(2, number//2):
            if (number % i) == 1:
                return True
            


primes = [number for number in numbers if prime(number) == True]

print(primes)