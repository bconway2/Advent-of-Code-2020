def part_one():
    in_compliance = 0
    with open('input.txt') as infile:
        for line in infile:
            l = line.split()
            bounds = l[0].split('-')
            letter = l[1][0]
            passchars = [char for char in l[2]]
            letter_count = passchars.count(letter)
            if (letter_count >= int(bounds[0])) and (letter_count <= int(bounds[1])):
                in_compliance = in_compliance + 1
        return in_compliance

def part_two():
    in_compliance = 0
    with open('input.txt') as infile:
        for line in infile:
            l = line.split()
            bounds = l[0].split('-')
            letter = l[1][0]
            if (l[2][int(bounds[0])-1] == letter) ^ (l[2][int(bounds[1])-1] == letter):
                in_compliance = in_compliance + 1
        return in_compliance