# # # # ls=[]
# # # # for i in range(100):
# # # #     if i%3==0:
# # # #         ls.append(i)
# # # #
# # #
# # #
# # # la=[i for i in range(100) if i%3==0]
# # # print(la)
# #   QET66I8-/*-+dict1  ={i:f"item {i}" for i in range(101) if i%10==0}
# # dict1  ={i:f"Item {i}" for i in range(5) }
# # dict2 ={value:key for key,value in dict1.items()}
# # print(dict1,"\n",dict2)
#
# dresses = {dress for dress in ["dress1","dress2","dress1","dress2"]}
#
# print(type(dresses))

# for generater comprehension we use parenthesis

evens = (i for i in range (100) if i%2==0)
print(type(evens))
print(evens.__next__())

for item in evens:
   print(item)