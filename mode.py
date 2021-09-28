
def mode(seq):
    if len(set(seq)) == 1:
        print("모든 원소들이 동일합니다.")

    elif len(set(seq)) == len(seq):
        print("모든 원소들의 갯수가 같습니다.")

    counter = {}
    for elem in seq:
        if elem not in counter.keys():
            counter[elem] = 1
        else:
            counter[elem] += 1

    maxval = max(counter.values())

    for key, val in counter.items():
        if val == maxval:
            print(key)


mode([1,2,2,3,3])