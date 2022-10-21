# random number generators
import random
help(random.random)

# Generate 10 random number (float continuous)
for i in range(10):
    print(random.random())

#Generate 10 uniform random number (integer continuous)
for i in range(10):
    print(random.uniform(5,10)) # which generates the number b/w 5 to 10

##Generate 10 uniform random number (integer discrete)
for i in range(50):
    print(random.randint(1,50))

# write program to generate random int number from 1 to 10 if random number is guess currecty stop the program(iteration)
import random
x=random.randint(1,10)
guess=int(input("Guess the random number"))
takes=1
while 1:
    takes+=1
    if guess==x:
        print("your guess is correct")
        break
    else:
        guess=int(input("Guess the random number")) # this for repeating the loop
print(f'total takes is {takes}')

# ask person to number of trials if the 50% output of dice 1 and dice 2 sum>7  a persons wins
trail=int(input(" Enter a number of trails: "))
count_7=0
for i in range(trail):
    d1=random.randint(1,6)
    d2=random.randint(1,6)
    print(f"trail{i+1}:{d1},{d2}")
    if (d1+d2)>7:
        count_7+=1
    else:  # not required
        continue
if count_7>50%trail:
    print("Person won")
else:
    print("Person loss")
