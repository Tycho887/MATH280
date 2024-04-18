import numpy as np
import math
from scipy.special import lambertw

known_primes = [2,3,5]


# the n-th prime is going to be approx n log n
# meaning the prime with index i will be approx f(i) = i ln i = N

def inverse_PNT(N):
    return math.ceil(math.exp(lambertw(N)))

# only want to check values less than the square root of the number, meaning checking indexes corresponding to the inverse PNT of sqrt(N)

def check_if_prime(n,upper_check_limit):
    for prime in known_primes[0:upper_check_limit]:
        if n%prime==0:
            return False
    else:
        return True

def old__batch_candidates(candidates):
    # first we take the square root of every candidate, then split up the batches for each time the square root increases by 2
    batches = []
    sqrt_candidates = [math.sqrt(candidate) for candidate in candidates]
    sqrt_candidates = np.array(sqrt_candidates)
    sqrt_candidates = np.ceil(sqrt_candidates).astype(int)
    for i in range(2,max(sqrt_candidates)+1,2):
        batch = [candidates[j] for j in range(len(candidates)) if sqrt_candidates[j]==i]
        batches.append(batch)
    return batches

def batch_candidates(candidates,batches=10):
    # we want to split the candidates into batches based on the number of primes we expect to find in each batch

    # the expected number of primes up to n is n/ln(n)

    # so the expected number of primes between a and b is b/ln(b) - a/ln(a)

    # we want to find choises of a,b,c.... such that the expected number is the same for each batch

    N = max(candidates)

    batch_limit = lambda i : math.exp(-lambertw(batches/(i*N)))

    batch_limits = [batch_limit(i) for i in range(1,batches+1)]

    print(batch_limits)

def generate_candidates(N):
    # we dont want multiples of 2.
    candidates = list(range(5,N,2))

    for i,candidate in enumerate(candidates):
        if str(candidate)[-1]=='5':
            candidates.pop(i)

    # we want to distribute the candidates into batches, the numbers in each batch have roughly the same square root and therefore the same number of primes to check

    return candidates






def find_primes(N=1000):
    candidates = generate_candidates(N)
    batches = batch_candidates(candidates)
    print(batches)
    # for candidate in candidates:
    #     if check_if_prime(candidate):
    #         known_primes.append(candidate)

find_primes()

