# p = [1, 3, 0, 0, 4, 2]
# maxi = len(p)/2
#
# if not '0, 0, 3' in str(p) and not '0, 3' in str(p):
# #     print("indeed a wise choice")
#
# p = [5,4,3,2,5,8,9]
#
# for 5 in p:
#     print ("yes")

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
# print(dataStructure[2][3:4])

for amino in reversed(range(6)):

    print(amino)
# options = 0
# options +=10
# print (options)
