def pal(string):
    tempString = string
    string = string.replace(" ", "")
    string = string.lower()
    if string == string[::-1]:
        print(tempString, "is a Palindrome")
    else:
        print(tempString, "isn't a Palindrome")