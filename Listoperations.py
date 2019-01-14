import time

# List operations

lststr = ["easy", "simple", "cheap", "free"]

#Access the last element
print(lststr[-1])

# pop - Removes one element,  append - add one element, extend - add many elements
lst = [3, 5, 7, 45, 2, 8, 19, 46, 23]

lst.pop #removes last element
print(lst)

lst.pop(2) #removes third elemnt from the list
print(lst)

lst.append(90)
print(lst)

lst.extend(lststr)  #Add multiple elements to an existing list
print(lst)

str1 = ["a", "b", "c"]
programming_language = "Python"
str1.extend(programming_language)
print(str1)

t = ("C#", "Jython", "Python", "IronPython")
str1.extend(t)
print(str1)


# Append method is the quickest among append,+ and += while adding elements to the list
n= 10000

start_time = time.time()
l = []
for i in range(n):
    l = l + [i * 2]
print(time.time() - start_time)

start_time = time.time()
l = []
for i in range(n):
    l += [i * 2]
print(time.time() - start_time)

start_time = time.time()
l = []
for i in range(n):
    l.append(i * 2)
print(time.time() - start_time)   


#Removing the elements from list

colours = ["red", "green", "blue", "green", "yellow"]

colours.remove("blue")

try:
    colours = ["red", "green", "green", "yellow"]
    colours.remove("blue")
except Exception:
    print("The selected color is not in the list")
finally:
    print("Executing finally...")


#Find the index of an element
colours = ["red", "green", "blue", "green", "yellow"]
print(colours.index("green"))

#Insert operation
lst = ["German is spoken", "in Germany,", "Austria", "Switzerland"]
lst.insert(3, "and")
print(lst)