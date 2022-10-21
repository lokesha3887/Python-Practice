#setting input argument by name-->named or key argument
#positional-only and named-only argument
#setting default value of an input argument

# def showtable(table,limit):
#     for i in range(1,limit+1):
#         a=print(f'{table}x{i}\t=\t{table*i}')
#     return a
#
# showtable(8,10) # key argument
# showtable(table=8,limit=10) # setting input argument by name
# showtable(limit=10,table=8) # setting input argument by name
# showtable(8,limit=10)# positional-only and named-only argument
#showtable(table=8,10) # which gives error since position argument followed by key argument

#default value example
# a='hi'
# b='Gm'
# print(a+b,sep='') # gere default value is nothing
#
# a=[2,6,10,2,5,7]
# print(a.sort()) # here default is reverse ==false
# print(a.sort(reverse=True))
#
#
#
# def showtable(table,limit=10): # here default value is limit=10
#     for i in range(1,limit+1):
#         a=print(f'{table}x{i}\t=\t{table*i}')
#     return a
# showtable(5)
#
# def table(tab,limit=10,reverse=False): # setting default values
#     if not reverse:
#         start,stop,step=1,limit+1,1
#     if reverse:
#         start,stop,step=limit,0,-1
#     for i in range(start,stop,step):
#         a=print(f'{tab}x{i}\t=\t{tab*i}')
#     return a
#
# table(4)
# table(8,15)
# table(2,5,True)
#
# def showtable(table,/,limit=10): # before / tells arguments before the forward slash should be positional arguments not by name
#     for i in range(1,limit+1):
#         a=print(f'{table}x{i}\t=\t{table*i}')
#     return a
# #showtable(table=5) # which will give error
# showtable(5)
#
# # example in module
# import math
# help(math) # look most of inbuilt in the form of (value,/) ==> we can't give  x=10,value=5 -like this
# #math.sqrt(x=15) # it will give error
#
# def table(tab,/,*,limit=10,reverse=False): # arguments shold be given by positional before the / slash and ....given by name after * symbol
#     if not reverse:
#         start,stop,step=1,limit+1,1
#     if reverse:
#         start,stop,step=limit,0,-1
#     for i in range(start,stop,step):
#         a=print(f'{tab}x{i}\t=\t{tab*i}')
#     return a
#
# #table(8,15) # gives error
# table(8,limit=15)
#
# def table(tab,/,limit=10,*,reverse=False): # arguments shold be given by positional before the / slash and ....given by name after * symbol
#     if not reverse:    # limit can be key / positional
#         start,stop,step=1,limit+1,1
#     if reverse:
#         start,stop,step=limit,0,-1
#     for i in range(start,stop,step):
#         a=print(f'{tab}x{i}\t=\t{tab*i}')
#     return a



# variable length of input arguments
#unpacking list / tuple
# a=[2,4,6,8,10,15]
# x,y,m,z,w,r=a
# x,*y,z=a
# x,*y,z=a
# # or
# print(*a)

# how it works in functions
# def sumsr(x,y,z):
#     sumsquare=x*x+y*y+z*z
#     print(sumsquare) # we cant use return with function
# a=[2,4,6]
# sumsr(a[0],a[1],a[2])

# better by unpacking list
# sumsr(*a)
#
# b=(2,4)
# sumsr(*b,5)

# # let's cahne the above code for directly imputuing a list / tuple
# def sumsqr(list_tuple):
#     sq=0
#     for i in list_tuple:
#         sq+=(i*i)
#     return sq
#
# s=[2,3,4,5,8,9,7]
# print(sumsqr(s))
#
# # lets make different the above program lets pass the number and and make this number to packed
# def sumsqr1(*l): # this packed the given numbers list / tuple
#     sq=0
#     for i in l:
#         sq+=(i*i)
#     return sq
#
# print(sumsqr1(2,3,4,5,8,9,7))
# s=[2,3,4,5,8,9,7]
# print(sumsqr1(*s)) # here s is unpacked and in function it's get packed
#
# # lets write code for this equatuion ((x1**2+x2**2+x3**2++++++xn**2)/a)+b) when passed the input as a list or tuple
# def equatin(a,b,*x):
#     sum_x=0
#     for i in x:
#         sum_x+=i*i
#     return ((sum_x/a)+b)
#
# l=[2,4,1,2,3,4,5,6]
# print(equatin(l))

# **kwargs these are related to dictionaries
# we can merge dictionaries when we different keys
d1={'name':"loka"}
d2={'age':24}

# we can also define dict
d3=dict(name='loka',age=23)
print(d3)

d=d1|d2 # merge
print(d)

# merge these ushing **
merge={**d1,**d2} #
print(merge)

def example(arg1,arg2,*arg,**kwarg): # here * ** is not a parameter its just a operators to packing list and merge dict
    print(arg1)
    print(arg2)
    print(arg)
    print(kwarg)

print(example(1,2,10,20,30,40,a=10,b=15,c=20))
# a='loka'
# print(a.replace('l','p'))
# print(a)