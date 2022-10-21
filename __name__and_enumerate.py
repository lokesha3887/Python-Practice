#__name__=__main__ ==>standaed way to indicate the main program of our program file
def sum(list1):
    return sum(list1)

# main program starts here #this not standart way of indicating main program
a=[2,4,6,8]
print(f"Mean of the list is is: {sum(a)}")

if __name__=='__main__':  # this is the standard way of indicating main program
    a=[2,4,6,8]
    print(f"Mean of the list is is: {sum(a)}")
# this method is helpful when we use this function in another file
#if do not use this if we use this function in another file the out will be function of this one and function created in another file to avoid this we use __name__
from functions import mean
from math import sqrt
def biggermean(l1,l2):
    if mean(l1)>mean(l2):
        return l1
    else:
        return l2

if __name__=='__main__':
    x1=[3,5,7]
    x2=[1,6,12]
    print(f"list with bigger mean is: {biggermean(x1,x2)}")


#Enumerate function
course=['data science','data analysis','machine learning']
print(list(enumerate(course)))

for i,j in enumerate(course):
    print(f"course:{i}--{j}")


dictn={
    'name':'lokesha',
    'age':23,
    'address':'mysore'
}
for key,val in enumerate(dictn): # for knowing keys by giving number
    print(f"{key}--{val}")








