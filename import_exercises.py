#!/usr/bin/env python
# coding: utf-8

# In[1]:


import function_exercises_updated as f


# In[2]:


f.apply_discount(40, .3)


# In[3]:



from function_exercises_updated import is_vowel


# In[4]:


is_vowel('a')


# How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
# 
#     - chain
#     - chain.from_iterable()
#   
# How many different ways can you combine two of the letters from "abcd"?
# 
#     - combinations
#     - permutations

# In[5]:


from itertools import permutations
  


# In[ ]:


perms = [x for x in itertools.permutations('abcd', 2)]
print(len(perms))


# In[6]:


print(list(permutations('abcd', 2)))


# In[7]:


from itertools import combinations


# 

# In[ ]:


combos = [x for x in itertools.combinations('abcd', 2)]
print(len(combos))


# In[8]:


print(list(combinations('abcd', 2)))


# In[ ]:





# In[9]:


import json

with open("profiles.json") as pj:
    profiles = json.load(pj)


# In[37]:


# Total number of users
len(profiles)

total_users = len(profiles)

print(total_users)


# In[11]:



profiles[0]['isActive']


# In[12]:


# Number of active users
len([profile for profile in profiles if profile['isActive']])


# In[13]:


# Number of inactive users
len([profile for profile in profiles if profile['isActive'] == False])


# In[ ]:



(


# In[14]:


print([profile['balance'].replace(',', '').strip('$') for profile in profiles])


# In[47]:


# Grand total of balances for all users

balances = map(float, [profile['balance'].strip('$').replace(',', '') for profile in profiles])

print(balances)


# In[48]:


print(sum(balances))
print(total_users)

print(sum(balances) / total_users)


# In[ ]:



    


# In[30]:


# Average balance per user -- this will be the sum - the len


number_of_users = len([profile for profile in profiles if profile['balance']])


round(balances / number_of_users, 2)


# In[ ]:


print(json.dumps(profiles, indent=4, sort_keys=True))


# In[ ]:


# User with the lowest balance


def lowest_balance(profile):

    low_balance_user = profile[0]

    for profile in profiles:

        if profile["price"] < low_balance_user["price"]:

            low_balance_user = profile

    return low_balance_user

  
 



# In[ ]:


item_minbalance = min(profiles, key=lambda x : x["balance"])
print("The id with the lowest balance is : " + item_minbalance["_id"])


# In[ ]:


# User with the highest balance

item_maxbalance = max(profiles, key=lambda x : x["balance"])
print("The id with the highest balance is : " + item_maxbalance["_id"])


# In[ ]:





# In[ ]:


import statistics
# Most common favorite fruit

statistics.mode(profile['favoriteFruit'] for profile in profiles)


# In[ ]:


# Least most common favorite fruit

min(profile['favoriteFruit'] for profile in profiles)


# In[ ]:


profiles[11]['greeting']


# In[ ]:


# Total number of unread messages for all users

unread_messages = ""

message_number = profiles[0]['greeting'].replace(" ", "")

for letter in message_number:
    if letter.isdigit():
        unread_messages += letter
        
        
print(int(unread_messages))
        






# In[49]:


for profile in profiles:
   print(profile['greeting'])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




