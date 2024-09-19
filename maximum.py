import clearTerminal
import numpy as np
clearTerminal.clear_terminal()


# z = np.array([ 1, -2, +1,  0])
# a = np.array([ 1,  2,  3, 12])
# b = np.array([+2,  1, -3,  6])
# c = np.array([-1, +3,  0,  9])

z = np.array([+2, -2, +3,   0])
a = np.array([-1,  1,  1,   4])
b = np.array([ 2, -1,  1,   2])
c = np.array([ 1,  1,  3,  12])

table = np.array([a, b, c, z])


def repair(table):
    table[-1, :] = table[-1, :]*-1
    m, n = np.size(table, 0), np.size(table, 1)
    tempTable = np.hstack([table[:, :-1], np.eye(n, m-1)])
    tempTable = np.column_stack([tempTable, table[:, -1]])
    return tempTable

def find_max_z(table):
    theMax = np.min(table[-1])
    theind = np.argmin(table[-1])
    return  theMax, theind


def minimum_test(table, ind):
    themin = np.array([])
    for i in range(np.size(table, 0)-1):
        temp = table[i, -1] / table[i, ind]
        if temp > 0:
            themin = np.append(themin, temp)
        else:
            themin = np.append(themin, np.inf)
         
    return np.argmin(themin), np.min(themin)


def create_new_table(table, new_table, exitRow, maxIndZ):
    for i in np.delete(np.array(list(range(np.size(table, 0)))), exitRow):
        temp =(-table[i, maxIndZ] / table[exitRow, maxIndZ])*table[exitRow] + table[i]
        new_table[i] = temp
    return new_table


def check(table):
    lastRow = table[-1]
    for lr in lastRow:
        if lr < 0:
            return True
    return False

# print(repair(z, a, b, c))
table = repair(table)
counter = 1
print(f"STEP {counter}:\n")
print(table)
print('------------------------------\n')
while check(table):
# for i in range(2):
    maxZ, maxIndZ = find_max_z(table)
    exitRow, minExitRow = minimum_test(table, maxIndZ)

    new_table = np.zeros([np.size(table, 0), np.size(table, 1)])
    new_table[int(exitRow)] = table[int(exitRow), :]/table[int(exitRow), maxIndZ]
    # print(new_table)

    table = np.round(create_new_table(table, new_table, exitRow, maxIndZ), 4)
    counter += 1
    print(exitRow+np.size(table, 0))
    print(maxIndZ+1)
    print(f"STEP {counter}:\n")
    print(table)
    print('------------------------------\n')
