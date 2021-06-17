def test(dictt, key, value):
   if any(sub[key] == value for sub in dictt):
       return True
   return False

dictt =  [{'employee_id': 10110, 'name': 'James Parkes', 'Dept': 'IT'},
      {'employee_id':  10111, 'name': 'Lisa Hayden', 'Dept': 'Accounts'}, 
      {'employee_id': 10113, 'name': 'Brian Adam', 'Dept': 'HR'},
      {'employee_id': 10114, 'name': 'Rine Arthur', 'Dept': 'Accounts'}, 
      {'employee_id': 10115, 'name': 'Jeff Simson', 'Dept': 'HR'}]
print("\nOriginal dictionary:")
print(dictt)
print("\nCheck if a specific Key and a value exist in the said dictionary:")
print(test(dictt,'employee_id', 10110))
print(test(dictt,'name', 'James Parkes'))
print(test(dictt,'Dept', 'Accounts'))
print(test(dictt,'Dept', 'CS'))
print(test(dictt,'name', 'Neeraj Bhatt'))
print(test(dictt,'employee_id', 11111))
