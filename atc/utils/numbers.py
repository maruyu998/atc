def factorize(n):
    ret = []
    while n % 2 == 0: 
        ret.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            ret.append(f)
            n //= f
        else:
            f += 2
    if n != 1: ret.append(n)
    return ret

def divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors

from collections import Counter
import functools, operator, itertools
def divisors(n):
    fact = factorize(n)
    collect = Counter(fact)
    keys, values = collect.keys(), collect.values()
    ret = []
    for nums in itertools.product(*[range(k+1) for k in values]):
        ret.append(functools.reduce(operator.mul,[key**num for key, num in zip(keys, nums)]))
    ret.sort()
    return ret

import functools, operator
def num_divisors(n):
    fact = factorize(n)
    return functools.reduce(operator.mul, [i+1 for i in Counter(fact).values()])