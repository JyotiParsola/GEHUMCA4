dictionary = [
      {'employee_id': 10110, 'name': 'James Parkes', 'Dept': 'IT'},
      {'employee_id':  10111, 'name': 'Lisa Hayden', 'Dept': 'Accounts'}, 
      {'employee_id': 10113, 'name': 'Brian Adam', 'Dept': 'HR'},
      {'employee_id': 10114, 'name': 'Rine Arthur', 'Dept': 'Accounts'}, 
      {'employee_id': 10115, 'name': 'Jeff Simson', 'Dept': 'HR'}
]
def find(dictt, key, value):
    if any(sub[key] == value for sub in dictt):
        return True
    return False


print( find(dictionary, 'name', 'James Parkes'))
print( find(dictionary, 'name', 'vivek joshi'))
print( find(dictionary, 'Dept', 'IT'))
print( find(dictionary, 'employee_id', 10110))
print( find(dictionary, 'employee_id', 1011712))


