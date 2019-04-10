import sys
n = sys.argv
n = int(n[1])

samples = list(range(1, n))
odd = []
for num in samples:
    if num != (num // 2) * 2:
        odd.append(num)

counter = 0
result_list = []
for prime_suspicious in odd:
    delimiter_list = list(range(3, int(prime_suspicious ** 0.5)))

    for delimiter in delimiter_list:
        answer = prime_suspicious % delimiter

        if delimiter != prime_suspicious and answer == 0:
            result_list.append(delimiter)

    if result_list == []:
        counter += 1
        z = str(counter+2) + 'th prime number is' + str(prime_suspicious)
        print(z)
        if counter == 999:
            break
        result_list = []
    else:
        result_list = []
