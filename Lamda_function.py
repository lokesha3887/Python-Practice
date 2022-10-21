# lamda function/lamda expression this also called anonymous function that defined without name
from math import sqrt
def f(x):
    return 1/(sqrt(x-1)
print(f(5))

# lets create lamda function for the same task
lambda x:1/(sqrt(x-1))# this is anonymous function created using lamda
# how to use above function
print((lambda x:1/(sqrt(x-1)))(3)) # observe paranthesis

# another way of using this
a=lambda x:1/(sqrt(x-1))
print(type(a))  # which gives the functions
print(a(3))

lambda x,y:sqrt(x*x+y*y)
print((lambda x,y:sqrt(x*x+y*y))(4,5))

b=lambda x,y:sqrt(x*x+y*y)
print(b(4,5))

minmax=lambda x:(min(x),max(x)) # inside the tuple
print(minmax([2,5,6,3,15,85]))

# lambda function for conditions
ifls=lambda n:n**2 if n%2==0 else n/2
print(ifls(5))

# sorted wont change the original data  Example
list=[2,5,9,3,4,8,5]
list.sort()
print(list) # see  sort its changes in the original data
list1=[2,10,9,30,3,58,125]
sorted(list1)
print(list1) # see  sorted its won't changes in the original data
# we can apply sorted for list,tuple,set,dict,,,for keep the original data

list2=[[2,10],[9,30,3],[58,125]] # its consider the 1st element in each sublist
print(sorted(list2)) # if we mix the list and tuple it will give error

lis=['lokesha p','prajju','nithin g','prabhakar nayak'] # to sort by length of object
print(sorted(lis,key=len))

lis1=[('lokesha p',5),('prajju',10),('nithin g',2),('prabhakar nayak',6)]
print(sorted(lis1)) # based on 1st value
print(sorted(lis1,key=lambda a:a[1])) # lis1 apllied for lamda function
def second(a):
    return a[1]

print(sorted(lis1,key=second)) # lis1 gone to function
print(max(lis1,key=second))

#list contain dict
a=[{'name':'loka','age':23},
   {'name':'raj','age':33}]
print(sorted(a)) # irt will give error since its not compute which dict is < or >
print(sorted(a,key=lambda a:a['age']))
print(max(a,key=lambda a:a['age'])['name']) # for getting name of senior

# parallel sorting
a=["bsc","msc","mba",'eng']
b=(10,21,12,50)
c=['lokesha p','prajju','nithin g','prabhakar nayak']
z=zip(a,b,c)
print(z)
s=sorted(z,key= lambda x:(x[0],x[1])) # if the 1st object tied then we considering second one
print(s)

# lambda function are most commonly used in  map,filter,soted # let's see

