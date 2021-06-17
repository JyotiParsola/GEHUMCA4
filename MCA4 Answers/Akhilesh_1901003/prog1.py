#get file object reference to the file
file = open("input.txt", "r")
#read content of file to string
data = file.read()
#get number of occurrences of the substring in the string
occurrences = data.count("Big Data")
print('Number of occurrences of the word :', occurrences)
