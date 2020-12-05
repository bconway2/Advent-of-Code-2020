import pandas as pd
import regex as re

def validpasses():
    passlist = []
    with open('day4input.txt') as file:
        passport = []
        for line in file:
            if line == '\n':
                passentry = dict(passport)
                passlist.append(passentry)
                passport = []
            entries = line.split()
            for item in entries:
                passport.append(item.split(':'))
    passentry = dict(passport)
    passlist.append(passentry)
    passport = []
    passdf = pd.DataFrame(passlist)
    passdf['cid'].fillna('NP',inplace = True)
    passdf.dropna(inplace=True)
    return passdf

def part_one(df):
    validpasses = df.shape[0]
    return validpasses

def count_digits(string):
    return sum(item.isdigit() for item in string)

def is_hclvalid(string):
    haircolor = [char for char in string]
    boolans = True
    validcolors = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f']
    if len(haircolor) != 7:
        boolans = False
    elif haircolor[0] == '#':
        for i in range(1,len(haircolor)):
            if not haircolor[i] in validcolors:
                boolans = False
    else:  
        boolans = False
    return boolans

def is_hgtvalid(string):
    print(string)
    m = re.findall(r'[A-Za-z]+|\d+', string)
    boolans = True
    if len(m) != 2:
        boolans = False
    elif m[1] == 'in':
        if (int(m[0]) < 59) | (int(m[0]) > 76):
            boolans = False
    elif m[1] == 'cm':
        if (int(m[0]) < 150) | (int(m[0]) > 193):
            boolans = False
    else:
        boolans = False
    return boolans 


def part_two(df):
    df = df[(df['byr'].astype(int) >= 1920) & (df['byr'].astype(int) <= 2002)]
    df = df[(df['iyr'].astype(int) >= 2010) & (df['iyr'].astype(int) <= 2020)]
    df = df[(df['eyr'].astype(int) >= 2020) & (df['eyr'].astype(int) <= 2030)]
    validecl = ['amb','blu','brn','gry','grn','hzl','oth']
    df = df[df['ecl'].isin(validecl)]
    df = df[df['pid'].apply(count_digits) == 9]
    df = df[df['hcl'].apply(is_hclvalid)]
    df = df[df['hgt'].apply(is_hgtvalid)]
    validpasses = df.shape[0]
    return validpasses