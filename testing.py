# p = [1, 3, 0, 0, 4, 2]
# maxi = len(p)/2
#
# if not '0, 0, 3' in str(p) and not '0, 3' in str(p):
#     print("indeed a wise choice")

# p = "abcdeafgse"
# o = []
# x = [["vtbd"], ["vnrs"]]
# o.append(p[0:8])
#
# print (o[0])
# print (x[0][0] + x[1][0])
# x[0].append("afina")
# print (x)

# x = [0,2,5,64,94,1,2,5,6,1,4,8,1]
# if all(p in x for p in ([555,4,8,64] and [2,994,1,6] and [8,5,2,0])):
#     print ("hallo")
# else:
#     print ("doenst work").

x = [0,2,5,64,94,1,2,2,2,2,5,6,1,4,8,1]
print (str(x))
if ('2, 2, 2, 2') in str(x):
    print ("hallo")
else:
    print ("doenst work")

# x = [[0,2,5]]
# p = [[6,2,7]]
# z = []
# z = x+p
# print (z)


# import numpy as np
#
#
# p = [1,3,0,0,4,2]
# z = [0,1,0,5,6,8,0,0]
# while (0 in p) or (0 in z):
#     p.remove(0)
#     z.remove(0)
# print (p)
# print (z)
# print (len(set(p)))

# import timeit

# def main():
#     options = []
#
#     counter = 8
#     for aminos in range(counter):
#         options.append(0)
#     counter -= 1
#     options2 = 1 * 10**counter
#     print (options2)
#     start = 0
#     st = round(timeit.default_timer(), 2)
#     # getNumbers(options, start, counter)
#     gettingNumbers(options2, counter)
#     stop = round(timeit.default_timer(), 2)
#     print (stop-st)
#
# def getNumbers(options, start, counter):
#     while options[0] != 3:
#         options[counter] += 1
#         if options[counter] == 5:
#             cancel = 0
#             while True:
#                 if options[counter - cancel] == 5:
#                     options[counter - cancel] = 0
#                     options[(counter - cancel) - 1] += 1
#                 else:
#                     break
#                 cancel += 1
#
# def gettingNumbers(options, counter):
#     k = options
#     while options < (k*4):
#         options += 1
#
#
# if __name__ == "__main__":
#     main()

# p = [[1,2],[2,5],[1,3]]
# z = []
# z.append([tuple(l) for l in p])
# list(map(tuple, p))
#
# for i in range(5):
#     print (i)
#
# print (p)
# print (z)
#
# print (set(z[0]))

# dataStructure = [[0,0,0,1],[0,0,0,0],[0,0,0,2]]
# correntCoor = dataStructure[2][3:8]
# for loop in correntCoor:
#     print("niks")
# # print(dataStructure[2][3:4])
# import random
# import math
#
# newScore = -8
# oldScore = -14
# temp = 3.5
# while temp > 0.1:
#     probab =  min(1,(math.expm1(-newPro.strength/temp)/math.expm1(-origPro.strength/temp)))
#     randumb = random.uniform(0,1)
#     if probab > randumb:
#         origPro = newPro
#     temp *= 0.5
