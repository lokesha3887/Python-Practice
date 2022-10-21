# string --value is given by " " or '' marks and its immutable and sequence data type
# we can't add or alter the string
str="Hello"
Str='Morning'
str="let's learn python"
str='let\'s learn python' # here \ is not a part of string
message='''hi good morning let's connect today , ok sure let"s tell me in what time'''

s="Hellow world"
# print(s[0]) # here 'space'  concider for counting
# print(s[-12])
# print(s[0:6])
# print(s[-12:-6])
# print(s[0:13:2])
# print(s[-12:-1:2])
# print(s[::1])
# print(s[::-1])
#or
#print(s[-1:-13:-1])

# print(len(s))
# print(s.count('o'))
# print(max(s)) # based on ascii code
# print(min(s))
# print(sorted(s)) # which gives in the form of list
#
# # operation
# a="lokesha"
# b="prajwal"
# print(a+b)
# print(a+' '+b) # for having space between them
# print(a*3)
# print('o' in s)


print(dir(str))
a="lokesha"
b='LOKESHA'
c='lokesh123'
# print(a==b.casefold()) # which converts or considers A=a
# print(a.upper())
# print(b.lower())
# print(c.isalnum()) # if string contain space  or apart from alhabet and number it will give false
# print(c.isalpha()) # gives True if string contains only alphabet
# print(c.isascii())


# n='1234'
# print(n.isdigit())
# print(n.isdecimal())
# print(n.isnumeric())
# print(n.isidentifier()) # it will give false since the value started with number
# print(a.lower())
# print(a.upper())
# print(message.isspace())
# print(message.istitle())# true if each word start with uppercase


# find the number of vovels
# message='''hi good morning let's connect today , ok sure let"s tell me in what time'''
# vcount=0
# for i in message:
#     if i.casefold() in 'aeiou':
#         vcount+=1
# print(f"vovels count is {vcount}")

# setting strong password
# import string
# first=input("Enter First name: ")
# second=input("Enter Second name")
# print('''password must include atleastone charater from (A-Z),(a-z),(0-9)
# and special character and should not include the first or lat name''')
# pwd=input("set your password")
# check1=check2=check3=check4=False
# for i in pwd:
#     if i in string.ascii_uppercase:
#         check1=True
#     elif i in string.ascii_lowercase:
#         check2=True
#     elif i in string.digits:
#         check3=True
#     elif i in string.punctuation:
#         check4=True
# if check1 and check2 and check3 and check4: # its considered as check=True
#     if first.casefold() not in pwd.casefold() or second.casefold() not in pwd.casefold():
#         print("Your password is completely setted")
#     else:
#         print("Try another")


# split
# spl='hellow word'
# split=spl.split() # which result in list ['hellow','world']
# print(split)

# a='computer:programing:python'
# print(a.split(':')) # using delimeter
#
# a.replace(':',' ') # it wont change in a so we need do define new var
# b=a.replace(':',' ')
# print(b)
#
# insr='''password must include atleastone charater
# from (A-Z),(a-z),(0-9) and special character
# and should not include the first or lat name'''
# print(insr.split()) # splits the each word if we want it by lines
# print(insr.splitlines()) # which splits line by line
#
# # count the number of char in sentence
# sentence='it wont change in a so we need do define new var'
# list1=list(sentence)# for char we use typecasting
# print(list1)
# print(f"total words in sentence is {len(list1)}")
#
# # count the number of char in sentence
# sentence='it wont change in a so we need do define new var'
# list1=sentence.split()# for word we use split()
# print(list1)
# print(f"total words in sentence is {len(list1)}")

# strip method --> used strip(any white space,\n,\t.. to be removed) the string
# a='helo  ' # to remove the space we use strip function
# b=a.strip()
# print(b+'gm') # lets check and see there is no white space

a=' \n  hello  \t'
b=a.rstrip() # which removes the white space from right side in left side but strip removes both the side
print('hi'+b+'gm') # hi in 1st line and hellogm in second line

a=' \n  hello  \t'
b=a.lstrip() # which removes the white space from right side in left side but strip removes both the side
print('gm'+b+'ok')

# task of bowling figures
# overs-maiden-runs-wickets
bowling='''raj  :  10-0-49-3
moni: 10-  1-41-3
lok:3-0-13-0
praj:6.2-0-43- 1
pav    : 10-0-49 -0'''
# here we need find name of the bowler with best economy (min runs per over
# display total maiden overs by indian team
# total overs bowles by indian team

bowlinglist=bowling.splitlines()
print(bowlinglist)  # which is in the form list
a=[record.replace(':',"-") for record in bowlinglist] # replace is aplicable since elements inside the lists are strings
print(a)
b=[spl.split('-') for spl in a] # results in lists inside the list
print(b)
# now we need to remoce spaces
c=[[rec.strip() for rec in str] for str in b] # since we consider list in comprehensin because if not consider we will get single list
print(c)
economy=[(n,int(r)/float(o)) for n,o,m,r,w in c] # we can also unpack the list
print(economy)
print(min(economy)[1])

# conversion of list to string
l=["computer","programing","is",'fun']
s=" ".join(l) # its aplicable only when list conatin only string elements " " if we give space inside this there is space b/w each element in out put
print(s)
