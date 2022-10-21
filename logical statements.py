# # logical operators
# x=int(input(" enter sa number which is less than 100 : "))
# if x<100:
#     print(' well done') # depend on if statement
# else:
#     print("no its not") # depend on else statement
# print( " bye bye") # not depend on if and else
#
# x=int(input(" enter sa number which is less than 100 : "))
# if 10<x<100:
#     print(' well done') # depend on if statement
# else:
#     print("no its not") # depend on else statement
# print( " bye bye") # not depend on if and else
#
# from math import sqrt
# n1=eval(input("enter a number"))
# if n1>0:
#     n2=sqrt(n1)
#     print(f'the sqrt of {n1} is {n2}')
# else:
#     print(" you entered a number less than zero")
#
# s1,s2,s3,s4,s5=eval(input(" enter a marks"))
# avrg=(s1+s2+s3+s4+s5)/5
# if avrg>80:
#     print("ypu are good student")
# if avrg>60 and avrg <60:
#     print("average student")
# if avrg < 60:
#     print(" ok ok")



# # nested if statement
# a,b,c=eval(input("enter numbers: "))
# if a>b and a>c:
#     print("a is highest")
# else:
#     if b>a and b>c:
#         print(" b is highest")
#     else:
#         print("c is highest")
#
#
# ms=input("are u married:")
# g=input("are u male")
# a=input( " is ur age > 25")
# if ms=="yes":
#     print("eligible")
# else:
#     if g=="yes":
#         if a=="yes":
#             print("eligible")
#         else:
#             print("not eligible")
#     else:
#         print("not eligible")

# flight=input(" Is fight available")
# pia=input("Is PIA available")
# airblue=input("Is AirBlue availble")
#
# if flight=="yes":
#     if pia=="yes":
#         print("Take PIA")
#     else:
#         if airblue=="yes":
#             print("Take AirBlue")
#         else:
#             print("Take QatarAirway")
# else:
#     print(" Go by road")

 # above one using elif

# s1,s2,s3,s4,s5=eval(input(" enter a marks"))
# avrg=(s1+s2+s3+s4+s5)/5
# if avrg>80:
#     print("you are good student")
# elif avrg>60:
#     print("you are average student")
# else:
#     print("you need to study more")

# unit=eval(input("Enter a unit"))
# if unit<= 100:
#     print("the cst is {}".format(unit*13.85))
# elif unit >100 and unit <=200:
#     print(" unit cost is {}".format((100*13.85)+(unit-100)*13.85))
# else:
#     print("unit cost is {}".format((100*13.85)+(100*15.86)+(unit-200)*16.83))


# for loop -->used to repeat a statement or block of statement many times
# write down with numbering " i will comlete my task in given time" for 100 times
# print("i will comlete my task in given time\n"*100)  # which prints only the statement
#
# for i in range(100):
#     print(f"{i+1}-i will comlete my task in given time")
#or
# for i in range(100):
#     i=i+1
#     print(f"{i}  i will complete my task in given time")
# # or
# for i in range(1,101):
#     print(f"{i}-i will comlete my task in given time")
#     i=i+1
#or
# for i in range(1,101):
#     print(f"{i}-i will comlete my task in given time")
# # range(10) is 0,1,2,,,,9
# # range(1,10) is 1,2,,,,9
# for i in range(1,101):
#     print(f"{i}-i will comlete my task in given time")

# print(range(10)) # range(0,10) its not clear so
# print(list(range(10))) # now its clear
# print(list(range(10,30,3)))
# print(list(range(-10,30)))
# print(list(range(20,10,-2)))
#
# for i in range(1,11):
#     print(f"{i}-i will comlete my task in given time")
# print("Thanks") # which is free from for loop it will executed once all the iteration complets
#
# # task take a positive integer from user and display the squaere root, do this for 10 times
# # from math import sqrt
# # for i in range(10):
# #     num=int(input("enter a value"))
# #     print("square root of your number is {}".format(sqrt(num)))
#
# # write a multiplication table using for loop
# for i in range(10):
#     i=i+1
#     print(f"12x{i}={12*i}")
#
# # calculations using for loop
# list=[12,32,64,15,37,22,19,45,16,30]
# # find out the count for the numbers lies b/w 20 to 40
#
# count=0
# for i in list:
#     if 20<=i<=40:
#         count=count+1
# print(f"{count}")
#
# list1=[2,5,8,4,12,36,15,25,48,95,136,1257,168,1,2,3,5]
# #count number of even numbers and odd numbers
# count_even=0
# count_odd=0
# for i in list1:
#     if i%2==0:
#         count_even=count_even+1
#     else:
#         count_odd=count_odd+1
# print("total even number is {}".format(count_even))
# print("total odd number is {}".format(count_odd))
#
# # find the sum of numbers in list1
# sum=0
# for i in list1:
#     sum=sum+i
#     print(f"cummulative sum is {sum}")
# print("total sum is {}".format(sum))
#
# # write program to sum all even numbers and summ odd numbers seperately
# sum_even=0
# sum_odd=0
# for i in list1:
#     if i%2==0:
#         sum_even+=i
#     else:
#         sum_odd+=i
# print(f"sum of even number is {sum_even}")
# print(f"sum of odd number is {sum_odd}")
#
# # ask user to enter his/her marks in each five sub and find its mean
# sum=0
# for i in range(5):
#     mark=int(input("enter a marks"))
#     sum=sum+mark
# print("mean is {}".format(sum/5))

#flag/check variable --> when a particular thing happen flag is used to indicate that a particular thing happened
# for ex a user enter 100 or not
# list2=[12,32,64,100,37,100,19,45,16,30]
# # have to develop a logic wether list2 contain 100 or not using flag/check
#
# flag=0
# for i in list2:
#     if i==100:
#         flag=1
# if flag==1:
#     print("list2 contain 100")
# else:
#     print("list2 doesn't contain 100")
#
# flag=0
# for i in list2:
#     if i==1000:
#         flag=1
# if flag==1:
#     print("list2 contain 1000")
# else:
#     print("list2 doesn't contain 1000")
#
# # ask user to enter a value and check it by using defined function
# def iseven(n):
#     if n%2==0:
#         return True
#     else:
#         return False
#
# n1=int(input("Enter a number")) # or eval
# print(iseven(n1))

# # nested for loop
# for i in range(5):
#     for j in range(3):
#         print(f"i={i} \t j={j}") # see how iteration works
#
#
# for i in range(5): # i=0 and j=0,1,2 similarly i=1 and j=0,1,2 like this iteration will be happened
#     for j in range(3):
#         print("Hi Good morning")
# print("*"*30)
#
# for i in range(5): # i=0 and j=0,1,2 similarly i=1 and j=0,1,2 like this iteration will be happened
#     for j in range(3):
#         print("Hi Good morning")
#     print(f"{i+1} times iteration completed")
#
# # create 3x3 matrix by assigning values with var A11,A12,,, find their sum and product
# sum=0
# prod=0
# for i in range(1,4):
#     for j in range(1,4):
#         num=int(input("enter a value"))
#         print(f"A{i}{j}: {num}")
#         sum+=num
#         prod*=num
# print(f"sum is {sum}")
# print(f"product is (prod)")

# # from 1 to 10, 1st row is 1,2,,,10 2nd is multiple of 2 ,,,,,,
# for i in range(1,11):
#     for j in range(1,11):
#         print(f"{i*j}\t",end="/") # which makes the 1st iteration values in 1st row with space and / symbol
#     print() # which makes 2nd iteration values in 2nd row
#
# # write a program to get the series of the program 1+(1/2)+(1/3)+++++n terms
# n=int(input("enter 'n' value: "))
# sum=0
# for i in range(1,n+1):
#     sum+=(1/i)
# print(f"{n} series sum is {sum}")
#
# # write a program to get the series of the program 1+(1/2!)+(1/3!)+++++n terms
# n=int(input("enter 'n' value: "))
# sum=0
# for i in range(1,n+1):
#     f=1 # factorial cannot be zero
#     for j in range(1,i+1): # finding factorial
#         f*=j # if i=2  f=1x1+1x2  if i=3 f=1x1+1x2+1x3
#     sum=sum+(1/f)
# print(f"{n} series sum is {sum}")
#
# # While loop-> used to repeat a iteration of statement for multiple times
# for i in range(10):
#     print("hi")
#
# print("*"*30)
# #or
# a=1
# while a<=10:
#     print("hi")
#     a+=1

# from math import sqrt
# print("this program will solve the Quadreatic eqation")
# option='y'
# while option=='y' or option=='Y':     # infinite while loop
#     a=eval(input("enter the value of a: "))
#     while(a==0):
#         print("a cannot be zero")
#         a=eval(input("enter the other value of a: "))
#     b=eval(input("enter the value of b: "))
#     c=eval(input("enter the value of c: "))
#     disc=b**2-4*a*c
#     if disc>=0:
#         d=sqrt(disc)
#         print("d is{}".format(d))

# loop control statement  Continue,break,return

# for i in range(5):
#     if i==2:
#         continue
#     print(i) # which won't print since we continue the iteration in the above block
#
# from math import sqrt
# print("this program will solve the Quadreatic eqation")
# option='y'
# while option=='y' or option=='Y':  # infinite while loop
#     a=eval(input("enter the value of a: "))
#     if(a==0): # instead of using while we can use if and continue
#         print("a cannot be zero")
#         a=eval(input("enter the value of a: ")) # not neccessary if u put a again it will go to 307 and 308
#         continue
#     b=eval(input("enter the value of b: "))
#     c=eval(input("enter the value of c: "))
#     disc=b**2-4*a*c
#     if disc>=0:
#         d=sqrt(disc)
#         print("d is{}".format(d))

# break --> to stop the iteration
for i in range(6):
    if i==3:
        break
    print(i)

# from math import sqrt
# num=int(input("enter a number : "))
# check=True
# for i in range (2,int(sqrt(num))+1):
#     if(num%i==0):
#         check=False
#         break
# if check:
#     print(f"{num} is prime number")
# else:
#     print(f"{num} is not a prime number")


# infinite
# while True: # (while 1) which tells condition is always true that is condition never gets false
#     print("hi")

#how to break this while loop by using some condition
# s=0
# while 1:
#     mark=int(input("Enter a number: "))
#     s+=mark
#     if s>600:
#         break
#     print(s)
#
#
# s=0
# while 1:
#     mark=int(input("Enter a number: "))
#     s+=mark
#     if s>600:
#         break
#     elif mark>100:
#         break
#     else:
#         continue
#     print(s)


# else statement associated with loop
# for i in range(5):
#     print(i)
# else: # this applied when all the iteration completed if we include break statment it won't get executed
#     print("else associated with loop")
#
# for i in range(i):
#     if i==3:
#         break
#     print(i)
# else:
#     print("thanks")
#
# #continue-->which terminates the 1 iteration
# for i in range(5):
#     if i==2:
#         continue
#     print(i)
# print("thanks")
#
# # break-->which terminates the remaining iteration
# for i in range(5):
#     if i==2:
#         break
#     print(i)
# print("thanks")
#
# #exit -->which terminates the entire program
# for i in range(5):
#     if i==2:
#         exit()
#     print(i)
# print("thanks")









