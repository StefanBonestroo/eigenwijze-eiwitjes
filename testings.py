import copy

p = [[0,0,1]]

p.append(copy.copy(p[0]))
print (p)

p[1][1] += 1

print (p)
