import sys

bestSoFar = 0  # variable that keeps track of largest number
# of McNuggets that cannot be bought in exact quantity
packages = (6, 9, 20)  # variable that contains package sizes
ans = {}
candidates = list(range(1, 151))
for n in range(1, 151):  # only search for solutions up to size 150
    ## complete code here to find largest size that cannot be bought
    ## when done, your answer should be bound to bestSoFa
    a = list(range(int((n / 6) + 1)))
    b = list(range(int((n / 9) + 1)))
    c = list(range(int((n / 20) + 1)))

    for candidate_a in a:
        # print(candidate_a)
        for candidate_b in b:
            # print(candidate_b)
            c = (n - ((6 * candidate_a) + (9 * candidate_b))) / 20
            check_c = (n - ((6 * candidate_a) + (9 * candidate_b))) % 20

            if check_c == 0 and c >= 0:
                c = int(c)
                print('found it!!')
                ans[n] = [candidate_a, candidate_b, c]
                candidates.remove(n)
                bestSoFar = max(candidates)
                break
            else:
                print("false")
        else:
            continue
        break

text = "Largest number of McNuggets that cannot be bought in exact quantity:" + str(bestSoFar)
print(text)
