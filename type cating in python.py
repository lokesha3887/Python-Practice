# x=20
# y=float(x)
# print(type(x))
# print(type(y))
#
# list=[2,5,7,8]
# dict=tuple(list)
# print(type(list))
# print(type(dict))
#
# x=str(10)
# print(x + 'hello')
#
# # task
# n1=int(input('enter a num'))
# n2=int(input('enter a num'))
#
# print("{} is {}% of {}".format(n1,n1%n2,n2))

# n1=float(input('enter a num'))
# n2=int(n1)
# print("integer part is {}".format(n2))
# print("fractinal part is {}".format(n1-n2))
#print(f"fractinal part is {n1-n2})

x=eval(str(input("enter 3 digits")))

sum=0
for i in x:
    sum=sum+i
    print(sum)
print("Summ is",sum)
