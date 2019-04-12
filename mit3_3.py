import sys

print(sys.argv)
x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

bestSoFar = 0  # variable that keeps track of largest number
# of McNuggets that cannot be bought in exact quantity
packages = (x, y, z)  # variable that contains package sizes
ans = {}
candidates = list(range(1, 201))
for n in range(1, 201):  # only search for solutions up to size 150
    ## complete code here to find largest size that cannot be bought
    ## when done, your answer should be bound to bestSoFa
    a = list(range(int((n / x) + 1)))
    b = list(range(int((n / y) + 1)))
    c = list(range(int((n / z) + 1)))

    for candidate_a in a:
        # print(candidate_a)
        for candidate_b in b:
            # print(candidate_b)
            c = (n - ((x * candidate_a) + (y * candidate_b))) / z
            check_c = (n - ((x * candidate_a) + (y * candidate_b))) % z

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

text = "Given package sizes {0}, {1}, and {2}, the largest number of McNuggets that cannot be bought in exact quantity is:{3}".format(
    x, y, z, bestSoFar)
print(text)
