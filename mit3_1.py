import sys
import math

ans = []
samples = list(range(50, 55))
for comb in samples:
    a = list(range(int((comb / 6) + 1)))
    b = list(range(int((comb / 9) + 1)))
    c = list(range(int((comb / 20) + 1)))

    for candidate_a in a:
        # print(candidate_a)
        for candidate_b in b:
            # print(candidate_b)
            c = (comb - ((6 * candidate_a) + (9 * candidate_b))) / 20
            check_c = (comb - ((6 * candidate_a) + (9 * candidate_b))) % 20

            if check_c == 0 and c >= 0:
                c = int(c)
                print('found it!!')
                ans.append([candidate_a, candidate_b, c])
            else:
                print("false")


print(ans)
