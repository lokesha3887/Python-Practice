#sequences,oredered-->List,String,Tuple
#collection,non ordered-->set,dictionary

#list
list=[1,2,8,6,41,23,"python",True]
print(len(list))
list[0]='hi'
print(list) # we can change the elements inside the list
# for accessing single element in a list ==right entries is excluded
print(list[0])
print(list[-8])

print(list[6])
print(list[-2])

print(list[0:4])
print(list[-8:-4])

print(list[0:8:2])
print(list[-8:-1:2])

print(list[1:8])
print(list[1:-1])

print(list[::-1])  #==>:: which considers the all elements inside the list like list[0:9:-1]
print(list[::-1]) # which revrse the list

print(list[9:-1]) # which gives a empty list

print(2 in list) # for checking 2 in list or not

#list operations
a=[1,2,"python"]
b=[10,20,'datadecode.ai']
print(a+b) # + which acts as concatination
print(a*3) # we cant perform a*b (* is aplicable for single list with integer value)
print(a==b) # for checking whether the list are equal or not
print(a>b) # which checks each elementwise and gives true or False

# list inbult functions
list=[2,10,"python",45,True]
list1=[10,20,30,"MongoDB"]
list.append(50) # append(object) which adds the 50 at last position in the list
list.append("lokesha")
print(list)

list.insert(3,35) # which adds the "35" in the 3(4th) position in the list
list.insert(8,'p') # insert(index,object)  since 8 here because we added 3 elements in previous steps
print(list)

list.remove("lokesha") # remove(object) which is used to remove the present object in the list
print(list)  # if we have lokesha repeated twice in a list, 1st position will be removed
# a=list.remove("lokesha") # using a=list.remove("lokesha") is not aplicable which gives none that is we cant store this as a variable
# print(a)
del list[0:3] # del function is used to delete multiple objects in a list, we cant store this in a variable
print(list)

print(all(list)) # returns True if list doen't contain False
print(any(list)) # returns true if list contain atleat 1 True value

list.pop(2) # pop(index) which removes the index 2 value #
print(list)
b=list.pop(2) # we can store this in a variable
print(b)

list.count(10) # which gives the count of 10 in the list, if not present in the list the function will give 0
a=list.count(10)
print(a)

i=list.index(True) #  index(object) which gives the index of true in list
print(i)

list.reverse() # which reverse the objects in entire list and we can't store this in a variable
print(list)

list.extend(list1) # which adds list1 objects to list ,we can't store this in a variable
print(list)

list.sort() # not supported for list which contain two data types
l=[2,5,9,4]
l.sort() # we can't store this in var
print(l)
l.sort(reverse=True) # descending order
ls=["loka","ravi","suni"]  #which is not aplicable for this kind of data
# print(ls.sort())
print(min(l))
print(max(l))
print(sum(l))
print(sorted(l))
print(sorted(ls))  # which is aplicable for both string and int data types ,we can store this in a var
print(sorted(ls,reverse=True))


list.clear() # which clears the objects in list and gives empty list
print(list)

x=[10,20,30,40,50,60,"loka",False,True,100,200,300,400,500]
import random
print(random.choice(x)) # which chooses a single elemnt randomly
print(random.choices(x,k=5)) # which chooses a 5 elemnt randomly (SRSWR)
print(random.sample(x,k=5))  # which chooses a 5 elemnt randomly (SRSWOR)

random.shuffle(x) # which shuffels the elements in the list randomly
print(x)









#write a program, which asks a users to enter month and program sgould give how many days in the that month

month=int(input("Enter a month: "))
list=[31,28,31,30,31,30,31,30,31,30,31,30] # month days
print(f'the total days in entered month is {list[month-1]}')


# create a list and write program to find out the product
list=[2,4,6,8,10]
prod=1
for i in range(5): #or len(list)
    prod*=list[i]
print(f'product is {prod}')

#0r
list=[2,4,6,8,10]
prod=1
for i in list:
    prod*=i
print(f'product is {prod}')

# similary for averages
list=[2,4,6,8,10]
sum=1
for i in list:
    sum+=i
print(f'product is {sum/len(list)}')

# create a list , if any value > 5 replace it by 10 ,if < 5 replace it by 0
list=[5,25,10,4,98,52,123,2,3,56,2,5,10]
up_list=[] # 0r list()
for i in list:
    if i>5:
        up_list.append(10)
    else:
        up_list.append(0)
print(up_list)
#or
list=[5,25,10,4,98,52,123,2,3,56,2,5,10]
for i in range(len(list)):
    if list[i]>5:
        list[i]=10
    else:
        list[i]=0
print(list)

# write a program to entered number is palindrome or not using list
num=121
l=list(str(num)) # since we can't convert number to list but we can convert string to a list
l.reverse() # now l var stored in the revrse order
l1=list(str(num)) # l1 variable in verginal format
if l==l1:
    print("Entered number is palindrome")
else:
    print("Entered number is not a palindrome")

#or
num=input("Enter a number: ") # which stores the number in string
l=list(num)
l1=l[::-1] # which gives the reverse of the list
if l==l1:
    print("Entered number is palindrome")
else:
    print("Entered number is not a palindrome")


# # some scenario
list=[]
for i in range(10):
    mark=int(input("Enter a marks: "))
    list.append(mark)
print(list)

#List
def a(b):
    return b*3
x=6
print(a(x))

list=[2,5,4,6,1,True]
print(a(list))

# square the entries in the list and store their sum with var A
list=[2,5,3,4,2,1]
sum=0
for i in list:
    sqr=i**2
    sum+=sqr
print("sum is {}".format(sum))

# or by defining function
def fun(x):
    sum=0
    for i in x:
        sum+=i**2
    return sum
list=[2,5,3,4,2,1]
print(f"by function the squrd list sum is {sum}")

#write program to get the square of elements in the list
def fun(x):
    b=[]
    for i in x:
        sqr=i**2
        b.append(sqr)
    return b
    print(f"by function the squrd list  is {b}")

list=[2,5,3,4,2,1]
print(fun(list))


# list as a function of arguments (input/output)

def sqrsum(list):
    s=0
    for i in list:
        s=s+(i**2)
    return s
# main program
l=[2,4,6,1,2]
print(sqrsum(l))


def sqrlist(list):
    sl=[]
    for i in list:
        sl.append(i**2)
    return sl
# main program
l=[2,4,6,1,2]
print(sqrlist(l))

# write a function program which creates a list of >avrg list, < avrglist and = avrglist
def avrglist(list):
    avrg=sum(list)/len(list)
    l=[]
    m=[]
    g=[]
    for i in list:
        if i<avrg:
            l.append(i)
        elif i==avrg:
            m.append(i)
        else:
            g.append(i)
    print(f"l:{l}\nm:{m}\ng:{g}")
#main function
avlist=[2,4,4,8,4,2,12,300]
print(avrglist(avlist))

print((24+50+30+26+23+60+20+52+75+71+35+44+50)/60)


list inside the list
a=[2,3.4,True,[2,4,6]]
print(len(a))
print(a[3])
print(a[3][1]) # accessing a elements  from the sublist

# zodiac sign
m=eval(input("Enter month number: "))
d=eval(input("Enter day: "))
if m==1:
    if d<=19:
        x='capricon'
    else:
        x='aquarius'
elif m==2:
    if d<=18:
        x='aquarius'
    else:
        x='pisces'
elif m==3:
    if d<=20:
        x='pisces'
    else:
        x='aries'
elif m==4:
    if d<=19:
        x='aries'
    else:
        x='taurus'
elif m==5:
    if d<=20:
        x='taurus'
    else:
        x='gemini'
elif m==6:
    if d<=20:
        x='gemini'
    else:
        x='cancer'
elif m==7:
    if d<=22:
        x='cancer'
    else:
        x='leo'
elif m==8:
    if d<=22:
        x='leo'
    else:
        x='virgo'
elif m==9:
    if d<=22:
        x='virgo'
    else:
        x='libra'
elif m==10:
    if d<=22:
        x='libra'
    else:
        x='scorpio'
elif m==11:
    if d<=22:
        x='scorpio'
    else:
        x='sagittarius'
else:
    if d<=21:
        x='sagittarius'
    else:
        x='capicorn'
print(f"your Zodiac sign is {x}")

# let write above code using list inside the list
def zodiac(day,month):
    signs=[
        ['capricorn',19],['aquarius',18],['pisces',20],['aries',19],
        ['taurus',20],['gemini',20],['cancer',22],['leo',22],
        ['virgo',22],['libra',22],['scorpio',21],['sigittarius',21],
        ['capicorn'] # since capicorn from dec to jan
    ]
    if day<= signs[month-1][1]:
        x=signs[month-1][0]
    else:
        x=signs[month][0]
    print(f"your zoidic is: {x}")

d=28
m=3
print(zodiac(d,m))

# if we have list inside the list we need convert this into a single list only using for loop
a=[[2,3,4],[7,-2,4,6,7],['computer',100,'python']]
single_list=[]
for i in a:
    for j in i:  # this will be fine if we have only the lists inside the list
        single_list.append(j)
print(f'the single list is: {single_list}')

# what if we have the list contain list,objects etc

a=[[2,3,4],[7,-2,4,6,7],['computer',100,'python'],500,1000]
single_list=[]
for i in a:
    if type(i)==list:
        for j in i:
            single_list.append(j)
    else:
        single_list.append(i)
print(f'the final single list is: {single_list}')


# need identified the which sublist has the highest sum
a=[[2,4,6],[1,2,3],[10,20,30,40],[12,5]]
sum1=[]
for i in a:
    sum1.append((sum(i)))
i=sum1.index(max(sum1))
print(f'{i+1} has max sum ')

# or by function
def maxsumind(list):
    sum1=[]
    for i in a:
        sum1.append((sum(i)))
    i=sum1.index(max(sum1))
    print(f'{i+1} has max sum ')

# slipt the list each list contain 3 elements
def splitlist(list,n):
    A=[]
    sublist=[]
    for i in range(0,len(list),n):
        sublist=list[i:i+n]
        A.append(sublist)
    return A

# main program
l=a=[2,4,6,1,2,3,10,20,30,40,12,5]
print(splitlist(l,3))


# merge given two list
a=[[2,4,6],[1,2,3],[10,20,30,40],[12,5]]
b=[[2,4,6],[1,2,3],[10,20,30,40],[12,5]]
A=[]
for i in range(len(a)): # or len(b)
    A.append(a[i]+b[i])
print(A)



# list comprehension
num=[2,4,6,8]
sqr=[]
for i in num:
    sqr.append(i**2)
print(sqr)

# let's do it using comprehension
num=[2,4,6,8]
sqr=[i**2 for i in num] # i**2 which is append to sqr in each iteration
print(sqr)

# list comprehension with filtering(some conditions is applied to filter tha data)
n=int(input("Enter a number: "))
factors=[]
for i in range(1,n+1):
    if n%i==0:
        factors.append(i)
print(factors)

#lets write using comprehension with filtering
n=int(input("Enter a number: "))
factors=[i for i in range(1,n+1) if n%i==0] # here the i value is appended to factors if its satisfies the if condition
print(factors)

#write a comprehension program to get only the sqr of even numbers
a=[1,2,3,4,5,6,7,8,9]
sqr_even=[i**2 for i in a if i%2==0]
print(sqr_even)

# generate the sum of the inner sub list
a=[[1,2,3],[4,5,6,7],[8,9],[10,11,12,13],[14,15]]
sumsublist=[sum(i) for i in a]
print(sumsublist)

# genreate a single valued tuples by using list
a=[1,2,3,4,5,6,7,8,9]
tup=[(i,) for i in a]
print(tup)

# if else condition in list comprehension
'''for the given list generate new list if the in the given list is even the corresponding value in the new list is sqr of that 
value if is odd 3 times this the new list value'''
list=[1,2,3,4,5,6,7,8,9]
new_list=[i**2 if i%2==0 else i**3 for i in list]
print(new_list)

# if we have the string
list=[1,2,3,4,5,6,7,8,9,"hello"]
new_list=[i**2 if i%2==0 else i**3 for i in list if type(i)==int]
print(new_list)

# working with multiple iterables
# generate a list of tuples (x,y)
x=[1,-1,5,0,3]
y=[2,-1,7,4,10]
tuple=[(x[i],y[i]) for i in range(len(x))]
print(tuple)

# usinf zip function
x=[1,-1,5,0,3]
y=[2,-1,7,4,10]
z=zip(x,y) # which in zip mode so we need to convert into list/tuple,,,
z=list(z) # zip function is preferable when the length of the x and y are different
print(z) # now we get the tuples





