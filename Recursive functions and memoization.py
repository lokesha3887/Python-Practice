'''user defined functions are called recursive functions-->we know user defined function calls any another function
 when the user defined function calls itself is called recurvie and its function is called recursive function'''
# Memoization is associated with recursive function
# for finding factorial
def fact(x):  # formula is fact(x)=x*fact(x-1) so we need recursvie function here and fact(0)=fact(1)=0
    if x==0 or x==1: # base function
        return 1
    else:
        return x*fact(x-1) # recursive function

print(fact(5))

# fibbonacci series 1123581321....f(n)=f(n-1)+f(n-2) if n>1  f(0)=f(1)=1

def fbn(n):
    if n==1 or n==0:
        return 1
    else:
        return fbn(n-1)+fbn(n-2)
print(fbn(10))

# non recursive
def fbn1(n):
    a,b=1,1
    for i in range(n-1):
        a,b=b,b+a
    return b
print(fbn1(2))

#memoization is an optimization technique used primarily to speed up computer programs and overcome the complexity of functions
# mannual(memoisation)
fbdict={}
def fbnm(n):
    if n in fbdict.keys(): # for checking n is in fbdict or not
        return fbdict[n]
    if n==1 or n==0:
        ans= 1
    else:
        ans= fbn(n-1)+fbn(n-2)
    fbdict[n]=ans # storing values in fbdict
    return ans
for i in range(115):
    print(fbnm(i))

# same using inbult function (inbuilt memoization)
from functools import lru_cache
@lru_cache # decorate function before the the function
def fbmodule(n):
    if n==1 or n==0:
        return 1
    else:
        return fbn(n-1)+fbn(n-2)

for i in range(115):
    print(fbmodule(i))