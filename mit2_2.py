import sys
import math
n = sys.argv
n = int(n[1])
samples = list(range(1, n))
odd = []

for num in samples:
    if num != (num // 2) * 2:
        odd.append(num)

primes_logsum = 0
result_list = []
for prime_suspicious in odd:
    delimiter_list = list(range(3, int(prime_suspicious ** 0.5)))

    for delimiter in delimiter_list:
        answer = prime_suspicious % delimiter

        if delimiter != prime_suspicious and answer == 0:
            result_list.append(delimiter)

    if result_list == []:
        z = 'th prime number is' + str(prime_suspicious)
        primes_logsum += math.log(prime_suspicious)
        print(z)
        result_list = []
    else:
        result_list = []

print(primes_logsum)
print(n)
print(n/primes_logsum*100)
