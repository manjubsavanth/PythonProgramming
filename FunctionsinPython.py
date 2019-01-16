# Functions

def fahrenheit(Temp_celsius):
    return (Temp_celsius * 9/5) +32

templist = [23.9, 34.6, 21.08, 34.67]
for t in (templist):
    print(t, ":", fahrenheit(t))


#Oprtaional parameter
def Hello(name = "Everyone"):
    """ Greets a person """
    print("Hey "+ name + "!")

Hello("Peter")
Hello()

#Docstring
print("The docstring of the function Hello: " + Hello.__doc__)

#Keyword Parameters 
def sumsub(a, b, c=0, d=0):
    return a - b + c - d 

print(sumsub(12,4))
print(sumsub(42,15,d=10))


#Return values
def no_return(x,y):
    c = x + y

res = no_return(4,5)
print(res) # None gets returned


def return_sum(x,y):
    c = x + y
    return c

res = return_sum(4,5)
print(res)







