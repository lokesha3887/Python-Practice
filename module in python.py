# # # for using module we use import function to get available modlue
import math
print(dir(math))# for getting function inside the module
help((math.sqrt)) # for getting help
x=input("enter a number  ")
s=math.sqrt(int(x))
print(f"square root of {x} is {s}")

from math import sqrt
x=eval(input("enter a number")) # eval fun for operations
s=sqrt(x)
print(f"square root of {x} is {s}")


print(math.sin(30))
print(math.log(100)) # lan function
print(math.log(100,10)) # log with base 10
# or
print(math.log10(100))