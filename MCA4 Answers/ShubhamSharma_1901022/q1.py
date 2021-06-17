file = open('./file.txt')
string = file.read()
string = string.split(" ")
res = {}
for i in string:
    res[i] = string.count(i)

for i in res:
    print(f'{i}: {res[i]}')
