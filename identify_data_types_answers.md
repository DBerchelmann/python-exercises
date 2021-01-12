>>> # What data type would best represent:
>>> # a term or phase typed in to search box?  string
>>> # if a user is logged in? bool
>>> # A discount amount to apply to user's shopping cart? float
>>> # Whether a coupon is valid? bool
>>> # An email address typed into a registration form? string
>>> # the price of a product? float
>>> # a matrix? list
>>> # the email addresses collected from a registration form? list
>>> # information about applicants to Codeup's data science program? dictionary

>>> '1' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> 6 % 4
2
>>> type(6 % 4)
<class 'int'>
>>> type(type(6 % 4))
<class 'type'>
>>> '3 + 4 is '
'3 + 4 is '
>>> '3 + 4 is ' + 3 + 4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> '3 + 4 is ' + (3 + 4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> x = 3 + 4
>>> '3 + 4 is {x}'
'3 + 4 is {x}'
>>> x
7
>>> y = f"3 + 4 is {x}"
>>> y
'3 + 4 is 7'
>>> 0 < 0
False
>>> 'False' == False
False
>>> True == 'True'
False
>>> 5 >= -5
True
>>> !False or False
  File "<stdin>", line 1
    !False or False
    ^
SyntaxError: invalid syntax
>>> True or "42"
True
>>> !True && !False
  File "<stdin>", line 1
    !True && !False
    ^
SyntaxError: invalid syntax
>>> 6 % 5
1
>>> 5 < 4 and 1 == 1
False
>>> 'codeup' == 'codeup' and 'codeup' == 'CODEUP'
False
>>> 4 >= 0 1 !== '1'
  File "<stdin>", line 1
    4 >= 0 1 !== '1'
           ^
SyntaxError: invalid syntax
>>> 6 % 3 == 0
True
>>> 6 % 2 == 0
True
>>> 5 % 2 != 0
True
>>> [1] = 2
  File "<stdin>", line 1
SyntaxError: cannot assign to literal
>>> [1] + [2]
[1, 2]
>>> [1] * 2
[1, 1]
>>> [1] * [2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'list'
>>> [] * [] == []
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'list'
>>> {} + {}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
>>> 


