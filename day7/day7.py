def get_allchildbags(searchterm,exteriorbagslist,interiorbagslist):
    a = []
    for i in searchterm:
        a.extend(interiorbagslist[exteriorbagslist.index(i)])
    return a

def part_one():
    with open('day7input.txt') as file:
        extbaglist = []
        intbaglist = []
        intbagnums = []
        for line in file:
            line = line.strip().split('contain ')
            extbag = (line[0].split(' bags ')[0])
            intbags = line[1].split(', ')
            if intbags[0] != 'no other bags.':
                numintbags = [int(i.split()[0]) for i in intbags]
                nameintbags = [' '.join(i.split()[1:3]) for i in intbags]
            else:
                numintbags = [0]
                nameintbags = []
            extbaglist.append(extbag)
            intbaglist.append(nameintbags)
            intbagnums.append(numintbags)
    contains_shiny_gold = 0
    for bag in extbaglist:
        new_children = get_allchildbags(searchterm = [bag],exteriorbagslist = extbaglist, interiorbagslist = intbaglist)
        while new_children != []:
            if 'shiny gold' in new_children:
                contains_shiny_gold += 1
                print('wow')
                break
            new_children = get_allchildbags(searchterm = new_children,exteriorbagslist = extbaglist, interiorbagslist = intbaglist)
    return contains_shiny_gold


def get_numchildbags(searchterms, searchnums, exteriorbagslist, interiorbagslist, interiorbagsnums):
    a = []
    b = []
    ind = 0
    for term in searchterms:
        if term != 'dead':
            a.extend(interiorbagslist[exteriorbagslist.index(term)])
            b.extend([searchnums[ind] * x for x in interiorbagsnums[exteriorbagslist.index(term)]])
        ind += 1
    return a, b

def part_two():
    with open('day7input.txt') as file:
        extbaglist = []
        intbaglist = []
        intbagnums = []
        for line in file:
            line = line.strip().split('contain ')
            extbag = (line[0].split(' bags ')[0])
            intbags = line[1].split(', ')
            if intbags[0] != 'no other bags.':
                numintbags = [int(i.split()[0]) for i in intbags]
                nameintbags = [' '.join(i.split()[1:3]) for i in intbags]
            else:
                numintbags = [0]
                nameintbags = ['dead']
            extbaglist.append(extbag)
            intbaglist.append(nameintbags)
            intbagnums.append(numintbags)
    [new_children, new_childrennums] = get_numchildbags(['shiny gold'], [1], extbaglist, intbaglist, intbagnums)
    interiorbags = 0
    while new_children != []:
        interiorbags += sum(new_childrennums)
        [new_children, new_childrennums] = get_numchildbags(new_children, new_childrennums, extbaglist, intbaglist, intbagnums)
    return interiorbags



print(part_one())
print(part_two)