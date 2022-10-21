# Generators--generator expression--is a iterators
# which consume less memory
# we have not used comprehension for tuple since we do not have tuple comprehension -- generators are similar to comprehension which uses tuple
# a=[i for i in range(1000000)] # comprehension
# print(sum(a))
#
# b=(i for i in range(1000000))  # generators
# print(sum(b))

# lest compare the generators vs comprehension
# from sys import getsizeof
# print(f"size of list:{getsizeof(a)}")
# print(f"size of generators:{getsizeof(b)}")
#
# # generators are iterators
# b=(i for i in range(10))
# for i in b:
#     print(i)
# for i in b:
#     print(f"second time is: {i}") # this time output is not displayed because of iterators

# x=[2,4,6,8,10]
# xsqr=[n*n for n in x] # list class
# print(dir(xsqr))
# print(type(xsqr))

# y=[2,4,6,8,10]
# ysqr=(n*n for n in y) # generator class
# print(dir(ysqr))
# print(type(ysqr))



# next in generators # to get iteration one by one but next is not aplicable for iterable
# print(next(ysqr))
# print(next(ysqr))
# print(next(ysqr))
# print(next(ysqr))
# print(next(ysqr))
# print(next(ysqr)) # output not displayed because of generators are iterator

'''from iterable we can create iterators as many we want 1-an iterator is also an iterable 
2-we can apply min,max, len and operators in on iterators
3- we can also unpack an iterator as for i,j in x:'''

# p='pthon'
# it=iter(p)
# print(type(it))  # string iterator similary we if we convert list type will be list_iterators

# second way of creating generators
# def test(n):
#     for i in range(n):
#         return i
# print(test(5))
# print(test(15))
# print(test(55)) # all thse 3 statement gives 0 only why this is iterable and always start from the begin

# how to convert above one to genratores using yield function

# def test(n):
#     for i in range(n):
#         yield i
# a=test(5) # a and b are genertors (resumable function)
# b=test(15)
# for i in a:
#     print(i) # which gives 0,1,,9 why because geneartor are iterators
# for i in b:
#     print(i) # which gives 0,1,,14  why because geneartor are iterators and act as resumable function
# once 0 executed it moves to next and then 1,,, and so

#lets consider another example
#
def getsqr(alist):
    for i in alist:
        return i*i
a=getsqr([2,3,4,5])
print(a)
print(sum(a))

# def getsqr(alist):
#     for i in alist:
#         yield i*i
# nums=[2,3,4,5]
# a=getsqr(nums)
# print(a)
# print(sum(a)) #since we apply min,max,,,on iterators