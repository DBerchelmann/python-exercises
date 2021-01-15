#!/usr/bin/env python
# coding: utf-8

# In[9]:


# 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

def is_two(n):
    if n == 2 or n == 'two':
        return True
    else:
        False

is_two(2)


# In[31]:


# 2 Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.


def is_vowel(letter):
    lower_vowels = ['a', 'e', 'i', 'o', 'u']
    upper_vowels = ['A', 'E', 'I', 'O', 'U']
    if letter in lower_vowels or letter in upper_vowels:
        return True
    else:
        return False

is_vowel('b')
        


# In[32]:


# 3 Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. 
# Use your is_vowel function to accomplish this.

def is_consonant(letter):
    lower_vowels = ['a', 'e', 'i', 'o', 'u']
    upper_vowels = ['A', 'E', 'I', 'O', 'U']
    if letter not in lower_vowels or letter not in upper_vowels:
        return True
    else:
        return False
    
is_consonant('f')


# In[126]:


# 4 Define a function that accepts a string that is a word. 
# The function should capitalize the first letter of the word if the word starts with a consonant.


def is_capitalized(word):
    vowels = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U' ]
    if word[0] not in vowels:
        return (word.capitalize())
    else:
        return (f"you returned a word that begins with a vowel and not a consonant")
    
is_capitalized('timber')


# In[55]:


# 5 Define a function named calculate_tip. 
# It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(meal_price, tip_percent):
    tip = meal_price * tip_percent
    total_bill = meal_price + tip
    return total_bill

calculate_tip(40, .5)
    
    


# In[59]:


# 6 Define a function named apply_discount. 
# It should accept a original price, and a discount percentage, and return the price after the discount is applied.

def apply_discount(price, discount_percent):
    discount = price * discount_percent
    discount_price = price - discount
    return discount_price

apply_discount(40, .2)


# In[64]:


# 7 Define a function named handle_commas. 
# It should accept a string that is a number that contains commas in it as input, and return a number as output.

def handle_commas(string):
    return int(string.replace(',', ''))

handle_commas('100,000,000')


# In[66]:


# 8 Define a function named get_letter_grade. 
# It should accept a number and return the letter grade associated with that number (A-F).

def get_letter_grade(value):
    if value >= 88:
        return("A")
    elif value >= 80:
        return("B")
    elif value >= 67:
        return("C")
    elif value >= 60:
        return("D")
    else:
        return("F")

get_letter_grade(75)


# In[129]:


# 9 Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowels(string):
    string = string.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in string:
        if letter in vowels:
            string = string.replace(letter, '')
    return string

remove_vowels('EATING')


# In[239]:


# 10 Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores


# A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_).
# A valid identifier cannot start with a number, or contain any spaces.

def normalize_name(string):
    
    string = "".join(letter for letter in string if letter.isalnum())   
    string = string.strip()
    string = string.lower()
    string = string.replace(' ', '_')
    
    if string.isidentifier() == True:
    
    
        return string
   
      
 
    

normalize_name('  %JeNni&**fer@ Lo*$&$(pez ')


# In[ ]:





# In[237]:


# 11 Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumulative_sum(a):
    a = [sum(a[0:x:1]) for x in range(len(a)+1)][1:]
    return a

cumulative_sum([1, 2, 3, 4])
        


# In[ ]:




