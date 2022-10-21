# function which helps us to calculate something at many times without writing the code again and again
# once the function is executed we need to call the function to use the function
# note: always input function should be not included in the function which you defined
from math import sqrt
# def areT(a,b,c):
#     s=(a+b+c)/3
#     print(f" Area of the triangle is {sqrt(s*(s-a)*(s-b)*(s-c))}")
#
# print(areT(2,5,4))
#
def areT(a,b,c):
    s=(a+b+c)/3
    Area=sqrt(s*(s-a)*(s-b)*(s-c))
    return Area

# a,b,c=eval(input("enter sides of triangle"))
# Area=areT(a,b,c) if we use same variable name which we defined for function which will give errors

# a1,a2,a3=eval(input("enter sides of triangle"))
# print(areT(a1,a2,a3))

# d,e,f=eval(input("enter sides of triangle"))
# Area=areT(d,e,f)
#
# d,e,f=eval(input("enter sides of triangle"))
# Area=areT(d,e,f)

# def biggestofthree(x,y,z):
#     if x>y and x>z:
#         print(f"{x}")
#     elif y>x and y>z:
#         print(f"{y}")
#     else:
#         print(f"{z}")
#
# print(biggestofthree(2,5,9))

# def biggestofthree(x,y,z):
#     if x>y and x>z:
#         b=x # return x
#     elif y>x and y>z:
#         b=y # return y
#     else:
#         b=z # return z
#     return b # not required
#
# print(biggestofthree(3,8,95))

# finding the distance points
# from math import sqrt
# def areT(a,b,c):
#     s=(a+b+c)/3
#     Area=sqrt(s*(s-a)*(s-b)*(s-c))
#     return Area
# def distpoints(x1,y1,x2,y2):
#     return sqrt((x2-x1)**2+(y2-y1)**2)
#
#
# a1,b1=eval(input(" Enter fist points : "))
# a2,b2=eval(input(" Enter second points : "))
# a3,b3=eval(input(" Enter third points : "))
# side1=distpoints(a1,b1,a2,b2)
# side2=distpoints(a1,b1,a3,b3)
# side3=distpoints(a2,b2,a3,b3)
# A=areT(side1,side2,side1)
# print(f"the are of0 the triangle is {A}")

# function inside a function
# def areT(a,b,c):
#     s=(a+b+c)/3
#     Area=sqrt(s*(s-a)*(s-b)*(s-c))
#     return Area
# def distpoints(x1,y1,x2,y2):
#     return sqrt((x2-x1)**2+(y2-y1)**2)
# def areofT(x1,y1,x2,y2,x3,y3):
#     a1=distpoints(x1,y1,x2,y2)
#     a2=distpoints(x1,y1,x3,y3)
#     a3=distpoints(x2,y2,x3,y3)def testfunction1():
# #     x=10
# #     print(locals())
# #     print(globals())
# #     print(f"the value of x1 is: {x}")
# #
# # def testfunction2():
# #     x=20
# #     print(locals()) #local var (inside the fun)
# #     print(globals())# main program var # both are d/f for under any function # both are same for main program
# #     print(f"the value of x2 is: {x}")
# # #main program
# # x=100
# # print(testfunction1())
# # print(testfunction2())
# # print(f"the value of x in the main program is: {x}") # now see that value of x is not affecting in all cases
# # print(locals)
# # print(globals)
#     return areT(a1,a2,a3)
#
# print(areofT(2,5,3,4,6,4))

def mean(list1):
    return sum(list1)/len(list1)
# main program
if __name__=='__main__':
    a=[2,4,6]
    print(f"mean is: {mean(a)}")