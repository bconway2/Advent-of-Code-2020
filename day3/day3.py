def part_one():
    slope = []
    with open('day3input.txt') as file:
        for line in file:
            slope.append([char for char in line])
    xind = 0
    tree_counts = 0
    for i in range(1,len(slope)):
        xind = xind + 3
        if xind > 30:
            xind -= 31
        if slope[i][xind] == '#':
            tree_counts += 1
    return tree_counts

def get_trees_pattern(slope, numr, numd):
    xind = 0
    tree_counts = 0
    for i in range(numd,len(slope),numd):
        xind = xind + numr
        if xind > 30:
            xind -= 31
        if slope[i][xind] == '#':
            tree_counts += 1
    return tree_counts

def part_two():
    slope = []
    with open('day3input.txt') as file:
        for line in file:
            slope.append([char for char in line])
    p1 = get_trees_pattern(slope,1,1)
    p2 = get_trees_pattern(slope,3,1)
    p3 = get_trees_pattern(slope,5,1)
    p4 = get_trees_pattern(slope,7,1)
    p5 = get_trees_pattern(slope,1,2)
    print(p1,p2,p3,p4,p5)
    return p1 * p2 * p3 * p4 * p5