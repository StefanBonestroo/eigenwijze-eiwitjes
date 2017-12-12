# import copy
#
# p = [[0,0,1]]
#
# p.append(copy.copy(p[0]))
# print (p)
#
# p[1][1] += 1
#
# print (p)
#
# mmutable inmutable phyton

options = [0,1,2,3,4,5,2,0,1]

for item in range(len(options) - 5):
    if len(set(options[(item):(item+6)])) != 6:
        print ("stuck")
    # if 0 in options[(item):(item+4)] and 1 in options[(item):(item+4)] \
    # and 4 in options[(item):(item+4)] and 5 in options[(item):(item+4)]:
    #     print ("stuck")
    else:
        print ("ok")
