def part_one():
    formans = []
    with open('day6input.txt') as file:
       partyform = ''
       for line in file:
            if line == '\n':
                formans.append(partyform)
                partyform = ''
            else:
                partyform += line.strip()
    numunique = []
    formans.append(partyform)
    for party in formans:
        numunique.append(len(set(party)))
    return sum(numunique)

def part_two():
    partyans = []
    with open('day6input.txt') as file:
       member = 0
       for line in file:
            if line == '\n':
                partyans.append(len(partyform))
                partyform = []
                member = 0
            elif member == 0:
                partyform = set(line.strip())
                member += 1
            else:
                partyform = partyform & set(line.strip())
    partyans.append(len(partyform))
    return sum(partyans)

print(part_one())
print(part_two())