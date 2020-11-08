#1

# def numbers(num):
#     if num >0:
#         print(num)
#         return num, numbers(num-1)

# numbers(4)

#2
# def sum_rec(num):
#     if num ==1:
#         return num
#     return num + sm_rec(num-1)

# print(sum_rec(10))


#3 

# def rec(num):
#     if len(num)==0:
#         return(num)
#     return rec(num[1:]) + num[0] 
# print(rec(num =input('enter numbers: ')))

#4

# def fib_rec(num):
#     if num <=1:
#         return num
#     return fib_rec(num-1)+fib_rec(num-2)
# print(fib_rec(4))

#5
# result[1] = 1
# result[2] = 2
# result[3] = 4
# def stepPerms(n):
#     if n == 0:
#         return 0
#     elif n in result.keys():
#         return result[n]
#     result[n] = stepPerms(n-3) + stepPerms(n-2) + stepPerms(n-1)
#     return result[n]