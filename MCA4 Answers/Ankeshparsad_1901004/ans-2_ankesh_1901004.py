#!/usr/bin/env python
# coding: utf-8

# In[1]:


dict = [{'employee_id': 10110, 'name': 'James Parkes', 'Dept': 'IT'},
      {'employee_id':  10111, 'name': 'Lisa Hayden', 'Dept': 'Accounts'}, 
      {'employee_id': 10113, 'name': 'Brian Adam', 'Dept': 'HR'},
      {'employee_id': 10114, 'name': 'Rine Arthur', 'Dept': 'Accounts'}, 
      {'employee_id': 10115, 'name': 'Jeff Simson', 'Dept': 'HR'}]

 


# In[4]:


def check(dictt, key, value):
    if any(sub[key]==value for sub in dictt):
        return True
    return False


# In[5]:


print(check(dict, 'name', 'james parkes'))
print(check(dict, 'name', 'ankesh parsad'))
print(check(dict, 'Dept', 'IT'))
print(check(dict, 'employee_id', '104741'))
print(check(dict, 'employee_id', '104742'))


# In[ ]:




