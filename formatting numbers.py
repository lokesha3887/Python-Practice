# default number system is decimal
a=10000000
print(f"value is : {a}") # it's quite difficult to read
print(f' value is {a:,}')
print(f' value is {a:_}')

b=-15
print(f' value is positive or negative {b:+}') # for checking the value whether positive or negative

c=2.5689
print(f' foramtting decimal value to 2 is  {c:.2f}')

print(f' {0.95:%}')
print(f' {0.95:.2%}') # for 2 decimal

print(f'{57965.1258:+,.3f}') # 3 formatters

print(f'{251894:E}') # scientific formatter

print(f'{23}')
print(f'{23:0d}') # decimal
print(f'{23:0b}') # binary
print(f'{23:0o}')  # octa


print(f'{23:>30}') # for printing 23 in right side  that after 28 space # total length is 30
print(f'{23:*>30}') # * may be anything similar

print(f'{23:^30}') # for alligning middle we use ^ symbol


roll_num=int(input("roll number"))
print(f' your R no is 2021-uom-{roll_num:0>2}')

print(round(2.025684,3))


sec=int(input(" Enter seconds : "))
min=sec//60
sec=sec%60
print(f'{min}:{sec}')
