data =  [{'employee_id': 10110, 'name': 'James Parkes', 'Dept': 'IT'},
      {'employee_id':  10111, 'name': 'Lisa Hayden', 'Dept': 'Accounts'}, 
      {'employee_id': 10113, 'name': 'Brian Adam', 'Dept': 'HR'},
      {'employee_id': 10114, 'name': 'Rine Arthur', 'Dept': 'Accounts'}, 
      {'employee_id': 10115, 'name': 'Jeff Simson', 'Dept': 'HR'}]

def test(key, value):
   if any(single_data[key] == value for single_data in data):
       return True
   return False

print(test('employee_id', 10110))
print(test('name', 'Lisa Hayden'))
print(test('name', 'Abhinav Garg'))
print(test('Dept', 'Mca'))
