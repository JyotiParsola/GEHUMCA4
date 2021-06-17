dictionary = [{'employee_id': 10110, 'name': 'James Parkes', 'Dept': 'IT'},
              {'employee_id':  10111, 'name': 'Lisa Hayden', 'Dept': 'Accounts'},
              {'employee_id': 10113, 'name': 'Brian Adam', 'Dept': 'HR'},
              {'employee_id': 10114, 'name': 'Rine Arthur', 'Dept': 'Accounts'},
              {'employee_id': 10115, 'name': 'Jeff Simson', 'Dept': 'HR'}]


def check(dictt, key, value):
    if any(i[key] == value for i in dictt):
        return True
    return False


print(check(dictionary, 'name', 'James Parkes'))
print(check(dictionary, 'name', 'Shubham Sharma'))
print(check(dictionary, 'Dept', 'IT'))
print(check(dictionary, 'employee_id', 10110))
print(check(dictionary, 'employee_id', 101111))
