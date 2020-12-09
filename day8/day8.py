def get_input():
    puzinput = []
    with open('day8input.txt') as file:
        for line in file:
            puzinput.append(line.strip())
    return puzinput

def part_one(inp):
    counter = [0] * len(inp)
    acc = 0
    n = 0
    while True:
        action = inp[n].split()
        counter[n] += 1
        if any(x >= 2 for x in counter):
            break
        if action[0] == 'nop':
            n += 1
        elif action[0] == 'acc':
            acc += int(action[1])
            n += 1
        else:
            n += int(action[1])
    return acc

def getjmplist(inp):
    counter = [0] * len(inp)
    acc = 0
    n = 0
    jmplist = []
    while True:
        action = inp[n].split()
        counter[n] += 1
        if any(x >= 2 for x in counter):
            break
        if action[0] == 'nop':
            n += 1
        elif action[0] == 'acc':
            acc += int(action[1])
            n += 1
        else:
            jmplist.append(n)
            n += int(action[1])
    return jmplist

def getnoplist(inp):
    counter = [0] * len(inp)
    acc = 0
    n = 0
    noplist = []
    while True:
        action = inp[n].split()
        counter[n] += 1
        if any(x >= 2 for x in counter):
            break
        if action[0] == 'nop':
            noplist.append(n)
            n += 1
        elif action[0] == 'acc':
            acc += int(action[1])
            n += 1
        else:
            n += int(action[1])
    return noplist


def eval_gamecode_change(inp,change):
    tinp = inp
    counter = [0] * len(tinp)
    
    acc = 0
    n = 0
    temp = tinp[change].split()
    if temp[0] == 'jmp':
        tinp[change] = 'nop '+ temp[1]
    else:
        tinp[change] = 'jmp ' + temp[1]
    suc = False
    while True:
        if n == len(tinp):
            suc = True
            break
        action = tinp[n].split()
        counter[n] += 1
        if any(x >= 2 for x in counter):
            break
        if action[0] == 'nop':
            n += 1
        elif action[0] == 'acc':
            acc += int(action[1])
            n += 1
        else:
            n += int(action[1])
    return [acc,suc]

def part_two(puzzle_input,jmplist,noplist):
    jmplist.extend(noplist)
    for i in jmplist:
        [accum, success] = eval_gamecode_change(get_input(),i)
        if success == True:
            break
    return accum

puzinp = get_input()
jumplist = getjmplist(puzinp)
noplist = getnoplist(puzinp)
part_two(puzinp, jumplist, noplist)