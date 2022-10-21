#sets --> is a collection not a sequence(we can't acces element by idexing),not ordered and do not have repeated values
# we use set when we don't look for order
# set is mutable
set={2,4,6,8}
print(set) # out may{8,6,2,6} ==> not ordered ==> slicing dicing is not aplicable

set={2,4,6,8,8}
print(set) # output conatin only onr 8 ==> unique valus

set={2,4,6,8,"loka"}
print(set)

set.add(10) # set is mutable
print(set)

set={2,4,6,[2,6]} #not aplicablr since set must conatin immutable data types values
set={2,4,6,(2,6)} # aplicable

# creating sets using other data types
a=set(range(10))
#b=list(a)
print(a)
print(b)

# a list contain many duplcates we need new list with unique
l=[2,2,2,5,5,5,4,4,4]
list_new=list(set(l))
print(list_new)

# set is iterable
l={2,5,6,9,8,5}
for i in l:
    print(i)

l={2,5,6,9,8,5}
m=l
m.add(10)
print(id(l),id(m)) # same since set is mutable

l={2,5,6,9,8,5}
m=l.copy() # which creats new objects to b
m.add(10) # it won't affect on the set l
print(id(l),id(m)) # different


# some operations
a={2,4,6,8,10}
b={1,2,3,4,5}
c={5,10,15,20,25,30}

intersection
c=a.intersection(b)
print(c)

d=a.intersection(b,c)
print(d)

e=a.intersection([2,4,6])
print(e)

e=a.intersection([2,4,6],(4,6,8))
print(e)

a.intersection_update([2,4,6]) # which will update to a
print(a)

union
c=a.union(b)
print(c)

d=a.union(b,c)
print(d)

e=a.union([2,4,6])
print(e)

e=a.union([2,4,6],(4,6,8))
print(e)

a.update([2,4,6]) # which will update to a
print(a)

difference
d=a.difference(b)
print(d)

a.difference_update(b)
print(a)

s=a.symmetric_difference(b) # elements of a not in b and elements of b not in a
print(s)

#subset disjoint... checking
print(a.issubset(b))
print(a.isdisjoint(b))
print(a.issuperset(b))

#sets comprehension
s=set()
for i in range(1,20):
    s.add(i**2)
print(s)

s={i**2 for i in range(1,21)}
print(s)

# dictionaries--ordered--mutable--non sequence (we can't acces the vaLUES BY INDEXION but by keys we can acces
# keys inside the dict must be unique and immutable data type
dict={'name':'lokesha',
      'age':24,
      'education':'msc',
      'rule':'data analyst'}
print(dict['age']) # we can acces objects  by keys since indexing is not aplicable
print(dict['rule'])

print(dict.get('age')) # we use get fun when we don't know wheather the key is present or not
print(dict.get('email')) # it will return None
print(dict.get('email','key not found'))

dict['email']='lokesha3887@gmail.com' # adding email to dict
dict.update({'adress':'banglore'}) # this also another method adding to dict
print(dict)
dict['age']=23.5 # changing the value wrt key
print(dict)
del dict['email'] # for deletin key and object
print(dict)
print(dict.pop('email','key is not found'))
print(len(dict))
print(sorted(dict))
#print(sorted(dict.values())) # not aplicable
print(sorted(dict.items()))

#converting list and accesing keys,values and both
k=list(dict) # or list(dict.keys()) # for getting keys
print(k)
v=list(dict.values())
print(v)
kv=list(dict.items()) # which stores the keys and values in tuples inside the list
print(kv)




# iteration in dict
dict={'name':'lokesha',
      'age':24,
      'education':'msc',
      'rule':'data analyst'}
for key in dict: # for iterating key
    print(key)

for values in dict.values(): # for iterating values
    print(values)

for keyvalues in dict.items(): # results in tuples
    print(keyvalues)

for key,values in dict.items():
    print(key,values,sep=':')
for key in dict:
    print(key,dict[key],sep='-')

# giving permission to open the aplication based on the user present in dict
login_user={'lokesha':2014,'prajwal':2413,'sunil':564}
user=input("Enter your name")
if user in login_user: # login_user.keys()
      pwd=int(input("enter your passward"))
      if pwd==login_user[user]:
            print("you are welcome")
      else:
            while True:
                  pwdr=int(input("re enter ur passward"))
                  if pwdr==login_user[user]:
                        print("you are welcome")
                        break
else:
      print("create a new account")

#Task --> countnumber of times each alpabet appeared in string
#quote='With Faith, Discipline and Selfless Devotion to duty, there is nothing worthwile that you cannot achive'
import string
quote=quote.replace(" ","") # removing spaces
for p in string.punctuation:
      quote=quote.replace(p,"") # removing punctuation
count={}
for i in quote:
      if i.lower() not in count:
            count[i.lower()]=1 # if key is not in count it will assign 1
      else:
            count[i.lower()]+=1 #if key is in count it will assign value+1
print(count)

print(sorted(count.items()))

# for shorting we need change key to values and values to key
cd=[(j,i) for i,j in count.items()] # unpacking tuples since the iteration in the form of (key,value)
print(sorted(cd,reverse=True))

#selectiong random category(keys) and values
import random
country=['pk','jp','trk','ind','engl']
sport=['crk','ftb','hok','bskbl','golf']
animal=['horse','tiger','monkey']
allwords={'country':['pk','jp','trk','ind','engl'],
          'sport':['crk','ftb','hok','bskbl','golf'],
          'animal':['horse','tiger','monkey']
          }
a=random.choice(tuple(allwords.items())) # we convertig to tuple/list bec random is not working on collrction it works on sequence
print(a)
print(f"category={a[0]}")
print(f"word={random.choice(a[1])}")

# write a program where a user buy diff items and program display the total amount of products in kgs
products={'tomato':100,
          'carrot':50,
          'beans':70,
          'onion':35,
          'brinjal':60
          }
invoice={} # product:quantity
bill=0
while True:
    p=input("enter a product and 9blank to quit: ")
    if p=="":
        break
    uprice=products.get(p)
    if uprice is None:
        print("Sorry item is not available")
        continue
    q=eval(input('Enter quantity:'))
    bill+=q*uprice
    if p not in invoice.keys():
        invoice[p]=q
    else:
        invoice[p]+=q
print(invoice)
print(bill)

#dictionary comprehension
a=[2,4,6,8,10] # output {2:4,4:16.....}
output={i:i**2 for i in a}
print(output)

s=['hello','world','computer','programming','python']
# create dict as keys in the above list and values as len of characters of those
# output={'hellow':6,'world':5.....}
output={i:len(i) for i in s}
print(output)

#create dict from other sequence value having values in pairs
a=[1,3,5,7,9]
dictn=dict(a) # its not work due to missing of key value
print(dictn)

a=[[2,4],[10,20],[100,1000]] # we must only 2 elements in sublist or subtuple
print(dict(a))

country=['pk','jp','trk','ind','engl']
sport=['crk','ftb','hok','bskbl','golf']
x=zip(country,sport)
print(dict(x))

# 2D dictionary
allstd={
      'sta111':{'name':'lokesha','age':23,'course':['data science','machine learning','mongodb']},
      'sta112':{'name':'prajwal','age':24,'course':['data science','python','django']}
}

print(allstd['sta111'])
print(allstd['sta111']['course'])
print(allstd['sta111']['course'][2])
print(allstd['sta111']['course'][2][0])

# data_structures_combined
m1={
    "Title":"12 Angry Men",
    "Year":1957,
    "Runtime":96,
    "Genre":("Crime", "Drama"),
    "Director":"Sidney Lumet",
    "Actors":["Martin Balsam", "John Fiedler", "Lee J. Cobb", "E.G. Marshall"]
}
m2={
    "Title":"Inception",
    "Year":2010,
    "Runtime":148,
    "Genre":("Action", "Adventure", "Sci-Fi", "Thriller"),
    "Director":"Christopher Nolan",
    "Actors":["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Elliot Page"," Tom Hardy"]
}
m3={
    "Title":"The Dark Knight",
    "Year":2008,
    "Runtime":152,
    "Genre":("Action", "Crime", "Drama", "Thriller"),
    "Director":"Christopher Nolan",
    "Actors":["Christian Bale", "Heath Ledger", "Aaron Eckhart", "Michael Caine"]
}
m4={
    "Title":"Lawless",
    "Year":2012,
    "Runtime":116,
    "Genre":("Crime", "Drama"),
    "Director":"John Hillcoat",
    "Actors":["Shia LaBeouf", "Tom Hardy", "Jason Clarke", "Guy Pearce"]
}
m5={
    "Title":"The Godfather",
    "Year":1972,
    "Runtime":175,
    "Genre":("Crime", "Drama"),
    "Director":"Francis Ford Coppola",
    "Actors":["Marlon Brando", "Al Pacino", "James Caan", "Richard S. Castellano"]
}
m6={
    "Title":"The Expendables 2",
    "Year":2012,
    "Runtime":103,
    "Genre":("Action", "Adventure", "Thriller"),
    "Director":"Simon West",
    "Actors":["Sylvester Stallone", "Jason Statham", "Jet Li", "Dolph Lundgren"],
}
m7={
    "Title":"Scent of a Woman",
    "Year":1992,
    "Runtime":156,
    "Genre":("Drama",),
    "Director":"Martin Brest",
    "Actors":["Al Pacino", "Chris O'Donnell", "James Rebhorn", "Gabrielle Anwar"]
}
m8={
    "Title":"The Italian Job",
    "Year":2003,
    "Runtime":111,
    "Genre":("Action", "Crime", "Thriller"),
    "Director":"F. Gary Gray",
    "Actors":["Mark Wahlberg", "Charlize Theron", "Donald Sutherland", "Jason Statham"]
}
m9={
    "Title":"Parker",
    "Year":2013,
    "Runtime":118,
    "Genre":("Action", "Crime", "Thriller"),
    "Director":"Taylor Hackford",
    "Actors":["Jason Statham", "Jennifer Lopez", "Michael Chiklis", "Wendell Pierce"]
}
m10={
    "Title":"Venom",
    "Year":2018,
    "Runtime":112,
    "Genre":("Action", "Adventure", "Sci-Fi"),
    "Director":"Ruben Fleischer",
    "Actors":["Tom Hardy", "Michelle Williams", "Riz Ahmed", "Scott Haze"]
}

myCollection=[m1,m2,m3,m4,m5,m6,m7,m8,m9,m10]
print(myCollection)

#Display First actor in the actor list of the Last movie in collection
print(myCollection[-1]['Actors'][0])

# Generate a List of All movie Titles
print([m['Title'] for m in myCollection])
## Without List Comprehension




t=[]
for m in myCollection:
    t.append(m['Title'])
print(t)

# Generate a List of movie titles with Genre Action
print([m['Title'] for m in myCollection if 'Action' in m['Genre']])
# Without List Comprehension
t=[]
for m in myCollection:
    if('Action' in m['Genre']):
        t.append(m['Title'])
print(t)

# Generate a List of all Genres in the collection
a=[j for i in myCollection for j in i['Genre']] # here repeated values are there
print(a)
genres=list(set(a))
print(genres)
#or
print(list({g for m in myCollection for g in m['Genre']}))
Without Set Comprehension
gen=set()
for m in myCollection:
    for g in m['Genre']:
        gen.add(g)
gen=list(gen)
print(gen)

# Generate a List of all Actors who have worked with Director "Christopher Nolan"
print(list({a for m in myCollection for a in m['Actors'] if m['Director']=="Christopher Nolan"}))
# Without Set Comprehension
act=set()
for m in myCollection:
    if(m['Director']=="Christopher Nolan"):
        for a in m['Actors']:
            act.add(a)
act=list(act)
print(act)

# Create a Dictionry with key as Director name and value as list of his Movie Titles
d={}
for m in myCollection:
    if(m['Director'] not in d):
        d[m['Director']]=[m['Title']]
    else:
        d[m['Director']].append(m['Title'])
print(d)

# Create a Dictionry with keys as Actor Names and value as number of movies

d={}
for m in myCollection:
    for a in m['Actors']:
        if(a not in d):
            d[a]=1
        else:
            d[a]+=1
print(d)

# Create a Ditionary with key as Genre and Value as List of Movies of that Genre
d={}
for m in myCollection:
    for g in m['Genre']:
        if(g not in d):
            d[g]=[m['Title']]
        else:
            d[g].append(m['Title'])
for k,v in d.items():
    print(f'{k}\t{v}')

# # Generate a List of Actors who have worked in both Drama and Action movies
# ## Wrong Approach
a=[]
for m in myCollection:
    for act in m['Actors']:
        if({'Action','Drama'}.issubset(m['Genre'])):
            a.append(act)
print(a)

## Correct Approach
actionActors={a for m in myCollection for a in m['Actors'] if 'Action' in m['Genre']}
dramaActors={a for m in myCollection for a in m['Actors'] if 'Drama' in m['Genre']}
print(list(actionActors.intersection(dramaActors)))

#Find total RunTime of all movies in collection
t=0
for m in myCollection:
    t+=m['Runtime']
print(t)

dict={'name':'loka',
      'age':23,
      'id':'sta111'
}
print(dict)
print(dict)
print(dict)

