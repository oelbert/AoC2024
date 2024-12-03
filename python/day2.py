import numpy as np
import copy as copy

def parse_inputs_np(txtlines: list):
    reports = []
    for line in txtlines:
        reports.append(np.array([int(val) for val in line.strip().split()]))
    return reports

def check_report_safety(report):
    grade = 0
    diffs = np.diff(report)
    if (np.abs(np.sum(diffs)) == np.sum(np.abs(diffs))):
        if (min(diffs) >= -3) and (max(diffs) <= 3):
            if (len(diffs[diffs==0])==0):
                grade = 1
    return grade

def check_damped_report_safety(report):
    grade = check_report_safety(report)
    if grade == 1:
        return 1
    else: # if grade == 0:
        for i in range(len(report)):
            dample = np.delete(report, i)
            g2 = check_report_safety(dample)
            if g2 == 1:
                return 1
        return 0

def run_day2(infile: str):
    infile = open(infile, "r")
    txtlines = infile.readlines()
    reports = parse_inputs_np(txtlines)
    total_passing = 0
    damped_passing = 0
    for report in reports:
        total_passing += check_report_safety(report)
        damped_passing += check_damped_report_safety(report)
    return total_passing, damped_passing

def parse_inputs(txtlines: list):
    reports = []
    for line in txtlines:
        reports.append([int(val) for val in line.strip().split()])
    return reports

def no_numpy_check_report(report):
    d1 = report[1] - report[0]
    if d1 == 0:
        return 0
    elif (abs(d1) > 3) or (abs(d1) < 1):
        return 0
    for ii in range(2, len(report)):
        d2 = report[ii] - report[ii-1]
        if d2 == 0:
            return 0
        elif d1 > 0:
            if d2 < 1:
                return 0
            elif d2 > 3:
                return 0
        else:
            if d2 > -1:
                return 0
            elif d2 < -3:
                return 0
    return 1

def damped_no_numpy_check(report):
    grade = no_numpy_check_report(report)
    if grade == 1:
        return 1
    else: # if grade == 0:
        for i in range(len(report)):
            dample = copy.copy(report)
            dample.pop(i)
            g2 = no_numpy_check_report(dample)
            if g2 == 1:
                return 1
        return 0


def day2_no_np(instr: str):
    infile = open(instr, "r")
    txtlines = infile.readlines()
    reports = parse_inputs(txtlines)
    total_passing = 0
    damped_passing = 0
    for report in reports:
        total_passing += no_numpy_check_report(report)
        damped_passing += damped_no_numpy_check(report)
    return total_passing, damped_passing


def main():
    print(run_day2('../data/day2.txt'))
    print(day2_no_np('../data/day2.txt'))

if __name__ == '__main__':
    main()
