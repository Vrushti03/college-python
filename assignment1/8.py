str = "The quick brown fox jumps over the lazy dog."
print('The first letters are:',str[0])

for x in range (0, len(str)):
    if str[x] == " ":
        letter = str[x + 1]
        print(letter)