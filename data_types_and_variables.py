# You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), 
# and Hercules (1 day, you don't know yet if they're going to like it). 
# If price for a movie per day is 3 dollars, how much will you have to pay?

movies_we_rented = {"little mermaid" : 3, "brother bear" : 5, "Hercules" : 1}

total_days = sum(movies_we_rented.values())

price_per_day = 3

total_cost = total_days * price_per_day

print(f'$ {total_cost}')



# Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. 
# Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? 
# You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

#if key is amazon, dicitonary.values * 380

hours_at_google = 6
hours_at_amazon = 4
hours_at_facebook = 10

google_pay = hours_at_google * 400
amazon_pay = hours_at_amazon * 380
facebook_pay = hours_at_facebook * 350

print(f'$ {google_pay}')



# A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.

class_not_full = False
no_schedule_conflict = True

can_be_enrolled = class_not_full and no_schedule_conflict

print(can_be_enrolled)


# A product offer can be applied only if people buys more than 2 items, and the offer has not expired. 
# Premium members do not need to buy a specific amount of products.

more_than_two_items_purchased = True
offer_not_expired = True
is_premium_member = True

can_be_applied = (more_than_two_items_purchased or is_premium_member) and offer_not_expired

print(can_be_applied)


username = 'codeup'
password = 'notastrongpassword'

# Create a variable that holds a boolean value for each of the following conditions:

# the password must be at least 5 characters
# the username must be no more than 20 characters
# the password must not be the same as the username
# bonus neither the username or password can start or end with whitespace

if len(password) >= 5 and 
   len(password) <= 20 and 
   password != username and 
   password == password.strip() and 
   username == username.strip():
    print(password)
else:
    print('fix your password and submit again')


