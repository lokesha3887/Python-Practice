'''tuples --> ordered collection almost similar to tuples but slightly change is there
in tuples we cant change the elements or add  and delete the elements inside the tuples
tuples consumes less memory and less time to execute as compared to a list
 in tuples we have few inbuilt function count,index,sorty,sorted'''
print(dir(list))
print(dir(tuple))
tuples=(1,2,8,6,41,23,"python",True)
print(len(tuples))

tuples[0]='hi'
print(list) # we can,t change the elements inside the tuples but this aplicable in list
# for accessing single element in a tuples ==right entries is excluded
print(tuples[0])
print(tuples[-8])

print(tuples[6])
print(tuples[-2])

print(tuples[0:4])
print(tuples[-8:-4])

print(tuples[0:8:2])
print(tuples[-8:-1:2])

print(tuples[1:8])
print(tuples[1:-1])

print(tuples[::-1])  #==>:: which considers the all elements inside the tuples like list[0:9:-1]
print(tuples[::-1]) # which revrse the tuples

print(tuples[9:-1]) # which gives a empty tuples

print(2 in tuples) # for checking 2 in tuples or not

#tuples operations
a=(1,2,"python")
b=(10,20,'datadecode.ai')
print(a+b) # + which acts as concatination
print(a*3) # we cant perform a*b (* is aplicable for single tuples with integer value)
print(a==b) # for checking whether the tuples are equal or not
print(a>b) # which checks each elementwise and gives true or False
print(all(a)) # returns True if tuple 'a' doen't contain False
print(any(a)) # returns true if tuple 'a' contain atleat 1 True value

tuples inbult functions
tuple=(2,10,"python",45,True)
tuple1=(10,20,30,"MongoDB")
tuple.count(10) # which gives the count of 10 in the tuple, if not present in the tuple the function will give 0
a=tuple.count(10)
print(a)
i=tuple.index(True)#which gives the index of true in list
print(i)
#tuple.sort() # not supported for tuple which contain two data types
t=(2,5,9,4)
t.sort() # we can't store this in var
print(t)
t.sort(reverse=True) # descending order
print(t)
tp=["loka","ravi","suni"]  #which is not aplicable for this kind of data
print(tp.sort())
print(min(t))
print(max(t))
print(sum(t))
print(sorted(t)) # which gives shorted list instead of tuples
print(sorted(tp))  # which is aplicable for both string and int data types ,we can store this in a var
print(sorted(tp,reverse=True))

tuple.append(50) #not aplicable
tuple.insert(3,35) # not aplicable
tuple.remove("lokesha") # not aplicable
del tuple[0:3] # not aplicable
tuple.pop(2) # not aplicable
tuple.reverse() # not aplicable
tuple.extend(tuple1) # not aplicable
tuples.clear() # not aplicable


x=(10,20,30,40,50,60,"loka",False,True,100,200,300,400,500)
import random
print(random.choice(x)) # which chooses a single elemnt randomly
print(random.choices(x,k=5)) # which chooses a 5 elemnt randomly (SRSWR)
print(random.sample(x,k=5))  # which chooses a 5 elemnt randomly (SRSWOR)

random.shuffle(x) # not aplicable
print(x)

packing tuple
a=1,2,3 #even if we dont give () it takes it as tuple
print(type(a))

#unpacking tuple
x,y,z=a

x,y=a # which gives error so
x,*y=a # or *x,y but not *x,*y

x=(1,2,[2,4]) # this also unpacked
a,b,c=x
print(a)
print(b)
print(c)
############
x=1
y=(1) # even if given par it yakes as integer
print(type(x))
print(type(y))

# now let use , to get tuple
x=1,
y=(1,) # even if given par it yakes as integer
print(type(x))
print(type(y))

# we can convert tuple into a list
a=(1,2,3,4)
b=list(a)


# let write above code using tuple inside the tuple to save emory and time
def zodiac(day,month):
    signs=(
        ('capricorn',19),('aquarius',18),('pisces',20),('aries',19),
        ('taurus',20),('gemini',20),('cancer',22),('leo',22),
        ('virgo',22),('libra',22),('scorpio',21),('sigittarius',21),
        ('capicorn') # since capicorn from dec to jan
    )
    if day<= signs[month-1][1]:
        x=signs[month-1][0]
    else:
        x=signs[month][0]
    print(f"your zoidic is: {x}")

d=28
m=3
print(zodiac(d,m))

# element of periodic table
#nqme,symbul,AN,AM
e1=('hydrogen','H',1,1)
e2=('helium','He',2,4)
e3=('lithium','Li',3,7)
e4=('berylium','Be',4,9)
pertable=[e1,e2,e3,e4]  # list contins 4 tuples
# i need symbols of elememnts having the AM bet 4 and 8
for element in pertable:
    name,symbol,AN,AM=element # unpacking the tuple
    if 4<=AM<=8:
        print(symbol)

# or
for name,symbol,AN,AM in pertable:
    if 4<=AM<=8:
        print(symbol)

# i want store the student registration
# F Name, L name, Reg no, couse registered
s1=('loka','p','sta111',['data science','data analysis']) # since names,reg not changed but course can be add,del etc so we use list inside the tuple
s2=('prajju','m','sta112',['data science','machine laearning'])
s3=('shrey','s','sta113',['data analytics','aws'])
s4=('santhu','s','sta114',['python','django'])
allstudents=[s1,s2,s3,s4] #list<<tuple<<list
print(allstudents)
print(allstudents[0][3]) # for getting courses of 1st student


# here i need to access only course
for fname,lname,reg,courses in allstudents: # for 1st tuple it assign fname,,,,,
    print(courses)
# or
for stdlist in allstudents:
    fname,lname,reg,courses=stdlist
    print(courses)

# for getting st name who pursuing data science
name=[]
for fname,lname,reg,courses in allstudents: # for 1st tuple it assign fname,,,,,
    if 'data science' in courses:
        name.append(fname)
print(name)



#
