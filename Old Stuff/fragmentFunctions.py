#
#
# def middleFragment(origPro, start, fragment, dimension):
#
#     stop = start + fragment
#     shifts = []
#
#     for amino in range(start, stop):
#         # append the shift in coordinates
#         if dimension == '2D':
#             shifts.append((origPro.aminoCoordinates[amino + 1][0] - origPro.aminoCoordinates[amino][0],
#             origPro.aminoCoordinates[amino + 1][1] - origPro.aminoCoordinates[amino][1]))
#         else:
#             shifts.append((origPro.aminoCoordinates[amino + 1][0] - origPro.aminoCoordinates[amino][0],
#             origPro.aminoCoordinates[amino + 1][1] - origPro.aminoCoordinates[amino][1],
#             origPro.aminoCoordinates[amino + 1][2] - origPro.aminoCoordinates[amino][2]))
#
#     check = 0
#     while(check == 0):
#         # initialize a list of new coordinates for the fragment
#         if dimension == '2D':
#             newCoordinates = [(origPro.aminoCoordinates[start][0], origPro.aminoCoordinates[start][1])]
#         else:
#             newCoordinates = [(origPro.aminoCoordinates[start][0], origPro.aminoCoordinates[start][1], origPro.aminoCoordinates[start][2])]
#         # find a new coordinate for every aminoacid of the fragment
#         az = 0
#         while az <= fragment:
#
#             newCtries = 0
#             shifts = shifts # dit was nodig om de random.shuffle te laten werken
#             random.shuffle(shifts)
#
#             # trie different shifts for this az
#             while newCtries < len(shifts):
#
#                 # break when there was no coordinate added for last az
#                 # break if there are already (fragmentlen) coordinates in newCoordinates and they are identical to original coordinates
#                 if az == len(newCoordinates) or (az == fragment - 1 and newCoordinates == origPro.aminoCoordinates[start:stop]):
#                     break
#
#                 newShift = (shifts[newCtries])
#
#                 # new coordinate that will be tested for validity
#                 if dimension == '2D':
#                     newC = (newCoordinates[az][0] + newShift[0] , newCoordinates[az][1] + newShift[1])
#                 else:
#                     newC = (newCoordinates[az][0] + newShift[0] , newCoordinates[az][1] + newShift[1], newCoordinates[az][2] + newShift[2])
#
#                 if (newC not in origPro.aminoCoordinates[0:start + az]
#                 and newC not in origPro.aminoCoordinates[stop + 1:]
#                 and newC not in newCoordinates):
#                     # found a possible coordinate -> remove this shift from possibilities for the other amino acids
#                     shifts.remove(newShift)
#
#                     # add new coordinate
#                     newCoordinates.append(newC)
#
#                     # a possible shift was found, so break the while loop
#                     break
#
#                 # shift created an already excisting coordinate so try again
#                 newCtries += 1
#
#             # (could not find a shift for last az?)
#             if az == len(newCoordinates) and az != fragment:
#                 break
#
#             az +=1
#         # if it finds new possible coordinates, return them
#         if len(newCoordinates) == fragment + 1:
#             return(newCoordinates, stop)
#         else:
#             return('none', stop)
#
#
#         check = 1
#
# def endFragment(origPro, start, fragment, dimension):
#
#     newCoordinates = origPro.aminoCoordinates[0:start]
#
#     for amino in range(start, start + fragment):
#         # print('start: ',start, ', amino: ',amino)
#         possibilities = possibilityCheck(amino, newCoordinates[0:amino])
#         valid = validityCheck(possibilities, newCoordinates, 'randomizer')
#         # print('valid', valid)
#         if valid != None:
#             newCoordinates.append(valid)
#         else:
#             return 'none'
#     return(newCoordinates[start:])
#
# def beginFragment(origPro, fragment, dimension):
#     newCoordinates = origPro.aminoCoordinates[fragment:]
#
#     for i in range(fragment):
#         # print('start: ',start, ', amino: ',amino)
#         possibilities = possibilityCheck(1, newCoordinates)
#         valid = validityCheck(possibilities, newCoordinates, 'randomizer') # wat wordt hier
#         # print('valid', valid)
#         if valid != None:
#             # print('will append valid')
#             oldCoordinates = newCoordinates
#             # print('oldCoordinates before new nc', oldCoordinates)
#             newCoordinates = [valid]
#             # print('oldcoordinates after', oldCoordinates)
#             newCoordinates.extend(oldCoordinates)
#
#         else:
#             # print('should return none')
#             return 'none'
#     # print('lengte nc', len(newCoordinates))
#     return(newCoordinates[:fragment])
