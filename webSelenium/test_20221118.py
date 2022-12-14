
# --------------1.列表推导式-------------
# list1 = [200, 300, 400, 500]
# result = []
#
# for x in list1:
#     if x > 250:
#         result.append(x)
# print(result)
#
# result1 = [x for x in list1 if x > 250]
# result2 = [x for x in list1]
# print(result1, result2)

# --------------2.while-------------
# while True:print(1)


# x=0
# while x<5:print(x);x+=1



# --------------3.if else-------------
# print("yes") if 8>9 else print("no")
#
# E=2
# print("high") if E==5 else print("数据STUDIO") if E==3 else print("low")
#
# if 3>2:print("exactly")


# --------------4.一行合并字典-------------
# d1 = {'a':1,'b':2}
# d2 = {'c':3,'d':4}
#
# # d1.update(d2)
# # print(d1,d2)
#
#
# d3 = {**d1,**d2}
# print(d3)
#
# print({**d1})



# --------------5.一行函数-------------

# def fun(x): return True if x%2 ==0 else False
# print(fun(3))
#
# func=lambda x : x%2==0
# print(func(2))

# --------------6.一行递归-------------
# def Fib(x):return 1 if x in {0,1} else Fib(x-1)+Fib(x-2)
# print(Fib(0))
# print(Fib(1))
# print(Fib(2))
# print(Fib(3))
# print(Fib(4))
# print(Fib(5))


# list2 = [32,22,11,4,6,8,12]
# # list2.sort()
# # print(list2)
# sorted(list2)
# print(list2)


print(range(1,5))
print(*range(1,5))


for i in range(5):
    print(i)