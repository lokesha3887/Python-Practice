profit=10000
ratioAli,ratioAhmed=0.7,0.3
shareAli=ratioAli*profit
shareAhmed=ratioAhmed*profit
print(shareAli,shareAhmed)

shareAnwar=0.1*shareAli+0.15*shareAhmed
shareAli-=0.1*shareAli
shareAhmed-=0.15*shareAhmed
print(shareAli,shareAhmed,shareAnwar)