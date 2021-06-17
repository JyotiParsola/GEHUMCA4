data = [{'employee_id': 10110, 'name': 'James Parkes', 'Dept': 'IT'},
        {'employee_id':  10111, 'name': 'Lisa Hayden', 'Dept': 'Accounts'},
        {'employee_id': 10113, 'name': 'Brian Adam', 'Dept': 'HR'},
        {'employee_id': 10114, 'name': 'Rine Arthur', 'Dept': 'Accounts'},
        {'employee_id': 10115, 'name': 'Jeff Simson', 'Dept': 'HR'}]

key = input("enter the key : ")
value = input("enter the value : ")

for single_data in data:
    if key in single_data.keys():
        if key == 'employee_id':
            value = int(value)
        if single_data[key] == value:
            print('true')
        else:
            print('false')
    else:
        print('false')
