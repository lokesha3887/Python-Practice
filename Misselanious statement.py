# here i need make not visual 1st print statement -- os
#display 1st print function only 3 sec

import os
import time
print("Hi GM")
time.sleep(3)
os.system("cls")
print("Bye GN")


# making watch
# hh=mm=ss=0
# while 1:
#     os.system('cls')
#     ss+=1
#     print(f"{hh:0>2}:{mm:0>2}:{ss:0>2}")
#     time.sleep(1)
#     if ss==60:
#         ss=0
#         mm+=1
#     if mm==60:
#         mm=0
#         hh+=1

# #making watch asking user to stop or not by using msvcrt
# import os,time,msvcrt
# hh=mm=ss=0
# while 1:
#     os.system('cls')
#     ss+=1
#     print(f"{hh:0>2}:{mm:0>2}:{ss:0>2}")
#     time.sleep(1)
#     if ss==60:
#         ss=0
#         mm+=1
#     if mm==60:
#         mm=0
#         hh+=1
#     if(msvcrt.kbhit()): # if any key press the loop will be ended
#         key=msvcrt.getwch()
#         if key==k:
#             break


#survey beverages: ask person to enter number b/w 0 to 4 ....
print("Survey beverages 1:coffe 2:tea 3:coke 4:juice")
# p=1 # since when person enters zero that is not counted so that i am choosin 1 instead of 0
# c=t=k=j=0
# while 1: # if we use p+=1 in next line we should give p=0
#     option=int(input("enter a number bwtween 0 to 4"))
#     if option==0 or option>4:
#         break
#     elif option==1:
#         c+=1
#     elif option==2:
#         t+=1
#     elif option==3:
#         k+=1
#     else:
#         j+=1
#     p+=1
#
# print(f"Total number of people participated in survey is {p} out of {p} people {c} are choosen coffe, {t} are choosen tea, {k} are choosen coke and {j} are choosen juice")
#

# to check whether the entered numbered is palindrome or not
# x=45682
# y=x
# rev=0
# while x!=0:
#     a=x%10 #answer is last digit that is 2
#     x=x//10 # first n-1 numbers that is 4568
#     rev=rev*10+a
#     print(a,x,rev)
#
# if y==rev:
#     print("x is a palindrome")
# else:
#     print("x is not a polindrome")


# find the palindrome numbers between 1 to 1000
for x in range(1000):
    y=x
    rev=0
    while x!=0:
        a=x%10 #answer is last digit that is 2
        x=x//10 # first n-1 numbers that is 4568 and taking x=x//10 to continue the iteration
        rev=rev*10+a
        print(a,x,rev)

    if y==rev:
        print(f"{y}x is a palindrome")
    else:
        print(f"{y} is not a polindrome")





