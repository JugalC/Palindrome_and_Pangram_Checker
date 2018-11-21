def pan(string):
    tempString = string
    string = string.replace(" ", "")
    string = string.lower()
    check = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False, False, False]
    for i in range(97,123):
        for j in range(len(string)):
            if string[j] == chr(i):
                check[i-97] = True

    for x in range(26):
        if not check[x]:
            print(tempString, "is not a Pangram")
            return
    print(tempString, "is a Pangram")

# ASCii Values
# A-Z 65-90
# a-z 97-122



