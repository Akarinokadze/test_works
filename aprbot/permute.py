import sys
from itertools import product
import time

N = int(sys.argv[1])
start_time = time.perf_counter()


def permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    for indices in product(range(n), repeat=r):
        if len(set(indices)) == r:
            yield ''.join(tuple(str(pool[i]) for i in indices))


num_pool = [0] * N
num_pool.extend([_ + 1 for _ in range(N)])
nums = set(permutations(num_pool))

with open('output.txt', 'w') as f:
    for num in nums:
        f.write(num + '\n')

end_time = time.perf_counter()
run_time = end_time - start_time
print(f"Finished in {run_time:.10f} seconds")
