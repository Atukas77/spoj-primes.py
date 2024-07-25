from math import isqrt

def primeList(n):
	if n <= 2:
		return []
	isPrime = [True] * n
	isPrime[0] = False
	isPrime[1] = False
    
	for i in range(2, isqrt(n) + 1):
		if isPrime[i]:
			for x in range(i**2, n, i):
				isPrime[x] = False
            
	return [i for i in range(n) if isPrime[i]]
	

print(primeList(100))