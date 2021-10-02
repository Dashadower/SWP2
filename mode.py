
def mode(seq):
    if len(set(seq)) == 1:  # 모든 원소의 값이 같아, 최빈값이 없는경우입니다. 값을 출력하지 않습니다.
        print("모든 원소가 동일합니다.")

    elif len(set(seq)) == len(seq): # 모든 원소의 값이 달라, 최빈값이 없는 경우입니다. 값을 출력하지 않습니다.
        print("모든 원소의 값이 다릅니다.")

    else:  # 최빈값이 존재하여 출력을 해야하는 경우입니다.
        counter = {}

        for elem in seq:
            if elem not in counter.keys():
                counter[elem] = 1
            else:
                counter[elem] += 1

        maxval = max(counter.values())
        for key, val in counter.items():
            if val == maxval:
                print(key, end=" ")  # 최빈값을 한 줄에 정리하여 보기 편하게 만들었습니다.


mode([1,2,3])
