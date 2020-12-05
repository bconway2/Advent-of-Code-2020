def gen_seatnums():
    with open('day5input.txt') as file:
        passes = [line for line in file]
    rownum = []
    colnum = []
    seatnum = []
    for entry in passes:
        row = []
        for i in range(0,7):
            if entry[i] == 'F':
                row.append('0')
            else:
                row.append('1')
        col = []
        for i in range(7,10):
            if entry[i] == 'L':
                col.append('0')
            else:
                col.append('1')
        col = ''.join(col)
        colnum.append(int(col,2))
        row = ''.join(row)
        rownum.append(int(row,2))
        seatnum.append(int(row,2) * 8 + int(col,2))
    return seatnum

def part_one(snums):
    return max(snums)

def part_two(snums):
    snums.sort()
    svalue = snums[0]
    for seat in snums:
        if svalue != seat:
            myseat = svalue
            break
        svalue += 1
    return myseat

seatnumbers = gen_seatnums()
print(part_one(seatnumbers))
print(part_two(seatnumbers))