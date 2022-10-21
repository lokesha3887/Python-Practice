'''Mutable-->can be changed  immutable--cant be changed'''
# a=(1,2,3)
# a[0]=5 # since tuple is immutable it will give error

# a=[1,2,3]
# a[0]=5 # since list is mutable it will change 1 to 5
# print(a)
#
# a=10
# a=20
# even int is immutable but here we can cahnging ==>actuallyit it wont change both are stored in the program
# because 1st a and 2nd are different id so this above code is working

# lets consider another scenario
# def removedup(l1,l2):
#     for i in l1:
#         if i in l2:
#             l1.remove(i) # list is mutable
#     return l1
# #main program
# a=[1,2,3,4,5]
# b=[1,2,8,10]
# print(removedup(a,b))  # its not giving correct answer since list is mutable and we are using the same list for iteration and removing
#
# #to overcome above problem
# def removedup1(l1,l2):
#     l3=l1[:]  # if we use l3=l1 again we are facing above problem
#     for i in l3:
#         if i in l2:
#             l1.remove(i) # list is mutable
#     return l1
# #main program
# a=[1,2,3,4,5]
# b=[1,2,8,10]
# print(removedup1(a,b))


# to understand more about mutable and immutable
# a=10
# print(id(a))
# a=20
# print(id(a)) # id's are different hence both are different since a is representing the diff value

# a=10
# print(id(a))
# b=10
# print(id(b)) # id's are same since a and b are representing the same value
# print(a==b) # which checks the number only
# print(a is b) # which checks in memory (id wise)

# a=10
# b=a
# print(id(a),id(b))# same

# lets consider the list
# a=[2,4,6]
# print(id(a))
# a=[4,6,8]
# print(id(a)) # id's are different since list is mutable hence both are different since a is representing the diff value
#
# a=[2,4,6]
# print(id(a))
# b=[2,4,6]
# print(id(b)) # id's are different since list a and b is representing the diff id
# print(a==b)  # true elements are same
# print(a is b) # stored memory are different

# a=[2,4,6]
# b=a # same object as "a"
# print(id(a),id(b)) # same
#
# c=a[:] # different object compoared to "a"
# print(id(a),id(c)) # diff


# a=[2,4,6]
# b=a # b is called alias of a and sollow copy
# b.append(4) # which will added to list "a" also
# print(a)
# print(b)

# a=[2,4,6]
# b=a[:] # b is called deep copy of a [slicing creates na new object]
# b.append(4) # which won't added to list "a"
# print(a)
# print(b)


# deep copy-->
import copy

# a=[2,4,6]
# b=a[:] # if we add anything to b it won't affect on a # here id's of a and b are different
# print(id(a))
# print(id(b))

# or
# import copy
# a=[2,4,6]
# b=copy.deepcopy(a)
#
# #sollow copy -->
# a=[1,3,5]
# b=a # if we change something it will affect on a
# print(id(a))
# print(id(b))

# or
a=[1,3,5]
b=copy.copy(a) # which creates the new list that's object inside the b is same in a
print(id(a))
print(id(b))
