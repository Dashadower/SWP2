def mode(seq):
        if len(set(seq)) == 1:  # 얘는 프린트 안 하는 값으로 설정하여 값이 없을 때 출력하는 문제를 해결했습니다.
            print("모든 원소가 동일합니다.")

        else: # 얘는 프린트 하는 값
            counter = {}

            for elem in seq:
                if elem not in counter.keys():
                    counter[elem] = 1
                else:
                    counter[elem] += 1

            if len(set(seq)) == len(seq):
                print("모든 원소의 갯수가 같습니다.")
                for key, val in counter.items():
                    print(key, end=" ") # end 를 이용하여 최빈값을 한 줄에 정리했습니다.
            else:
                maxval = max(counter.values())
                for key, val in counter.items():
                    if val == maxval:
                        print(key)


mode([1,2,2])
