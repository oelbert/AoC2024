import numpy as np

def run_day1(infile: str):
    inarr = np.loadtxt(infile)
    part1 = np.sum(np.abs(np.sort(inarr[:,1]) - np.sort(inarr[:,0])))
    part2 = 0.
    for loc in inarr[:,0]:
        part2 += len(inarr[:,1][inarr[:,1] == loc]) * loc
    return part1, part2


def parse_inputs(txtlines: list):
    loc1 = []
    loc2 = []
    for line in txtlines:
        cleanline = line.strip().split()
        loc1.append(int(cleanline[0]))
        loc2.append(int(cleanline[1]))
    return loc1, loc2

def day1_no_np(instr: str):
    infile = open(instr, "r")
    txtlines = infile.readlines()
    loc1, loc2 = parse_inputs(txtlines)
    loc1.sort()
    loc2.sort()
    part1 = 0
    part2 = 0
    tracker1 = 0
    tracker2 = 0
    value = -1
    jsave = 0
    for ii in range(len(loc1)):
        part1 += abs(loc2[ii] - loc1[ii])
        loc = loc1[ii]
        
        for jj in range(jsave, len(loc2)):
            if loc2[jj] > loc:
                jsave = jj
                break
            if loc2[jj] == loc:
                part2 += loc
            
    return part1, part2


def main():
    print(run_day1('../data/day1.txt'))
    print(day1_no_np('../data/day1.txt'))

if __name__ == '__main__':
    main()
