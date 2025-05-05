# """for i in range(10):
#     print(i)"""
# from distutils.command.install import value
#
#
# # The n is different
# def fibonacci(n):
#      if n==1:
#          return 1
#      elif n==2:
#          return 1
#      elif n>2:
#          return fibonacci(n-1)+fibonacci(n-2)
#
# for i in range (1,5):
#     print(i,":",fibonacci(i))
#A dictionary holds a key and value
# cache={}
#
# value=0
#
# def fibonacci2(n):
#     if n in cache:
#         return  cache[n]
#
#     if n==1 or n==2:
#         value=1
#     elif n>2 :
#         value=fibonacci2(n-1)+fibonacci2(n-2)
#
#     cache[n]=value
#
#     return value
#
# # for i in range(1,500):
# #
# #    print(f"{i} Term: {fibonacci2(i)}")
#
# from functools import lru_cache
# #L->LAST,R->RECENTLY,C->CACHE
#
# @lru_cache(maxsize=2000)#assigns 1000 more bytes to the original size of the main function//100 bytes by default.Once the fib3 function is done it reallocates
# def fib3(n):
#
#     if n==1 or n==2:
#         return 1
#     elif n>2 :
#         return fib3(n-1)+fib3(n-2)
#
# for i in range(1,10000):
#     print(i, ":",fib3(i))



def TowerOfHanoi(n,source,destination_rod,auxiliary_rod):

    if n==1:
        print("Move disk from 1 from the source",source,"to destination",destination_rod)
        return
    #Recursive case
    TowerOfHanoi(n-1,source,auxiliary_rod,destination_rod)
    print("Move disk",n,"from source",source,"to destination",destination_rod)
    TowerOfHanoi(n-1,auxiliary_rod,destination_rod,source)

n=3
TowerOfHanoi(n,'A','B','C')






