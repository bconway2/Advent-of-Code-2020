def readfile(infile):
    dayinput = []
    with open(infile) as file:
        for line in file:
            dayinput.append(int(line.strip()))
    return dayinput

def part_one(dayinput):
    prev_vals = dayinput[0:25]
    sumlists = []
    for i in range(1,len(prev_vals)):
        isums = []
        for j in range(0,i):
            isums.append((prev_vals[i] + prev_vals[j]))
        sumlists.append(isums)
    for i in range(25,len(dayinput)):
        if any(dayinput[i] in sublist for sublist in sumlists):
            prev_vals.pop(0)
            jsums = [dayinput[i] + j for j in prev_vals]
            prev_vals.append(dayinput[i])
            sumlists.pop(0)
            for sums in sumlists:
                sums.pop(0)
            sumlists.append(jsums)
        else: 
            return dayinput[i]

def part_two(badinput, dayinput):
    n = 0
    for day0 in dayinput:
        sumdays = day0
        n += 1
        day_list = [day0]
        for day1 in dayinput[n:]:
            day_list.append(day1)
            sumdays += day1
            if sumdays == badinput:
                return (min(day_list) + max(day_list))
            elif sumdays > badinput:
                break


day9input = readfile('day9input.txt')

enc_failint = part_one(day9input)

enc_weakness = part_two(badinput = enc_failint, dayinput = day9input)

print(enc_failint)

print(enc_weakness)