#Function to reverse a given string

def reverse_string(strpassed):
    rstr = ''
    index = len(strpassed)
    for i in strpassed:
        rstr += strpassed[index - 1]
        index = index - 1
    print(rstr)
