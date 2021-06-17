def word_count(str):
    # Create an empty dictionary
    counts = dict()
    words = str.split()
    # Loop through each line of the file
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
# Open the file in read mode
file = open("python.txt", "r")
#read content of file to string
data = file.read()
# Print the number of occurrences of word
print(word_count(data))
