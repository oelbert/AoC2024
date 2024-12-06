def read_data(file):
    rules = {}
    infile = open(file, "r")
    raw_rules, raw_pages = infile.read().split('\n\n')
    rrr = raw_rules.split('\n')
    for rule in rrr:
        first, second = rule.split('|')
        if int(first) in rules:
            rules[int(first)].add(int(second))
        else:
            rules[int(first)] = {int(second)}
    rps = raw_pages.split('\n')
    pages = [[int(page) for page in printing.split(",")] for printing in rps if printing]
    return rules, pages

def is_order_ok(pages, rules):
    seen_pages = set()
    for pagenum in pages:
        if pagenum in rules.keys():
            if rules[pagenum].intersection(seen_pages):
                return False
        seen_pages.add(pagenum)
    return True

def verify_pages(pageset, rules):
    passing_pages = []
    failing_pages = []
    for pages in pageset:
        if is_order_ok(pages, rules):
            passing_pages.append(pages)
        else:
            failing_pages.append(pages)
    return passing_pages, failing_pages

def midsum_verified(pages):
    return sum(p[len(p)//2] for p in pages)

def fixfails(pageset, rules):
    fixed = []
    for pages in pageset:
        fixed_pages = []
        for pagenum in pages:
            seen_before = []
            if pagenum not in rules.keys():
                fixed_pages.append(pagenum)  # Put it at the end because it has no constraints on what comes after
            else:
                seen_after = list(rules[pagenum].intersection(fixed_pages))
                if seen_after:
                    fixed_pages.insert(fixed_pages.index(seen_after[0]), pagenum)
                else:
                    insert_index = 0
                    if seen_before:
                        for ii in range(len(seen_before)):
                            if pagenum in rules[seen_before[ii]]:
                                insert_index = ii + 1
                        fixed_pages.insert(insert_index, pagenum)
                    else:
                        fixed_pages.append(pagenum)
                seen_before.append(pagenum)
        fixed.append(fixed_pages)
    return fixed

def main():
    example_rules, example_pages = read_data("../data/day5_example.txt")
    example_verified, example_failed = verify_pages(example_pages, example_rules)
    print(midsum_verified(example_verified))
    fixed_example = fixfails(example_failed, example_rules)
    print(midsum_verified(fixed_example))

    rules, pages = read_data("../data/day5.txt")
    verified, failed = verify_pages(pages, rules)
    print(midsum_verified(verified))

if __name__ == '__main__':
    main()
