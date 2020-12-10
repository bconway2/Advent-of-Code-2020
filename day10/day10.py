def get_input(infile):
    with open(infile) as file:
        output = [int(line.strip()) for line in file]
    return output

def part_one(day_input):
    day_input.sort()
    day_input.append(max(day_input) + 3)
    diff_1 = 0
    diff_3 = 0
    last = 0
    for i in day_input:
        test = i - last
        if test == 1:
            diff_1 += 1
        if test == 3:
            diff_3 += 1
        last = i
    return diff_1 * diff_3

def part_two(day_input):
    last = 0
    must_use = []

    '''Must use any adapters where nearest diff is 3'''
    for i in day_input:
        test = i - last
        if test == 3:
            must_use.append(last)
            must_use.append(i)
        last = i
    
    '''remove dups'''
    mand_adpts = []
    for i in must_use:
        if i not in mand_adpts:
            mand_adpts.append(i)

    '''determine dof between mandatory adapters'''
    last = 0
    tricky_cases = []
    combinations = 1
    for adpt in mand_adpts:
        diff = adpt - last
        opt_adpt = [x for x in day_input if last < x < adpt]
        if diff <= 3: # any adapters in this range are optional
            combinations *= 2 ** len(opt_adpt)
        elif diff == 4: # need to have at least one of the included adapters
            combinations *= (2 ** len(opt_adpt) - 1)
        else: # fortunately the gap doesn't get larger because the logic would
            # have quickly gotten very very messy
            tricky_cases.append([x for x in day_input if last < x < adpt])
        last = adpt
    return combinations

day10inp = get_input('day10input.txt')

print(part_one(day10inp))
print(part_two(day10inp))