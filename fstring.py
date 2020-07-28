import math
# F string
# this is bad because it creates ambuigity during debugging
#  this is simple formatting of  string
me="Dev"
a="This is %s"%me
print(a)

# another method of string formating

me="Dev"
a1=5
# a="This is %s"%me
a="this is {1}{0}"
b=a.format(me,a1)
print(b)
 # this is also is not a good idea of string formatting

 # let see another way of string formating

a=f"this is {me} {a1}  {4*3} {math.cos(65)}"

print(a)