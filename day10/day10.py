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
    ''' Need to have any adapters where diff is 3'''
    for i in day_input:
        test = i - last
        if test == 3:
            must_use.append(last)
            must_use.append(i)
        last = i
    must_use = list(set(must_use)).sort()
    return must_use