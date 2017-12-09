# p = [1, 3, 0, 0, 4, 2]
# maxi = len(p)/2
#
# if not '0, 0, 3' in str(p) and not '0, 3' in str(p):
#     print("indeed a wise choice")

# def main():
#     options = []
#     counter = 3
#     for aminos in range(counter):
#         options.append(0)
#     counter -= 1
#     start = 0
#     reroll = 0
#     print (getNumbers(options, start, reroll))
#
# def getNumbers(options, start, reroll):
#     options[start] += 1
#     if options[start] == 5:
#         reroll = 0
#         getNumbers(options, start + 1, reroll)
#     if options[2] == 2:
#         return options
#     getNumbers(options, 0, reroll)
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

dataStructure = [[0,0,0,1],[0,0,0,0],[0,0,0,2]]
correntCoor = dataStructure[2][3:8]
for loop in correntCoor:
    print("niks")
print(dataStructure[2][3:4])
