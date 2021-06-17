my_dict = [ {'employee_id': 10110, 'name': 'james parker', 'Dept': 'IT'},
      {'employee_id': 10111, 'name': 'Lisa Hayden', 'Dept': 'Accounts'},
      {'employee_id': 10113, 'name': 'Brian Adam', 'Dept': 'HR'},
      {'employee_id': 10114, 'name': 'Rine Arthur', 'Dept': 'Accounts'},
      {'employee_id': 10115, 'name': 'Jeff Simpson', 'Dept': 'HR'}
     ]
def test(dictt, key, value):
    if any(sub[key] == value for sub in dictt):
        return True
    return False

ch=input(print("enter the value to find"))
key=input(print("enter the key to find"))
print(test(my_dict ,key, ch ))



