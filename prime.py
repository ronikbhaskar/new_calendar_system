
from typing import List, Dict
from copy import deepcopy

def prime_factorize(n : int) -> Dict[int, int]:
	"""
	returns dict representation of prime factors
	12 -> {1: 1, 2: 2, 3: 1}
	if n is not a natural number, returns None
	"""
	
	if type(n) is not int:
		return None
		
	if n < 1:
		return None
		
	if n == 1:
		return {1: 1}
	
	factors = {1: 1}
	list_of_primes = []
	prime = 1
	
	if n % 2 == 0:
		count = 0
		while not n % 2:
			count += 1
			n /= 2
		factors[2] = count
	
	while n != 1:
		
		prime += 2
		
		if is_prime(prime, list_of_primes):
			list_of_primes.append(prime)
			
			temp = 0
			
			while n % prime == 0:
				temp += 1
				n = n / prime
				
			if temp:
				factors[prime] = temp
	
	return factors
	
def is_prime(n : int, primes : List[int]) -> bool:
	"""
	given list of primes, checks if divisible by any
	assumes list is complete up to possible divisors of n
	"""
	
	if type(n) is not int:
		return None
	
	if n < 2:
		return False
		
	for prime in primes:
		if prime >= n:
			return True
		
		if n % prime == 0:
			return False
			
	return True
	
def get_primes(n : int) -> List[int]:
	"""
	returns list of primes up to n
	accidental Sieve of Eratosthenes
	"""
	
	if type(n) is not int:
		return None
	if n < 2:
		return None
		
	primes_not_2 = []
	
	for i in range(3,n+1,2):
		if is_prime(i,primes_not_2):
			primes_not_2.append(i)
		
	return [2] + primes_not_2
	
def product(factors : list, default):
	"""
	factors is just a list of everything you are multiplying together
	works like built-in sum function
	takes a default by which to multiply everything
	"""
	
	p = default
	for x in factors:
		p *= x
	return p
	
def factors_to_num(factors : Dict[int, int]) -> int:
	"""
	multiplies all the prime factors together
	"""
	if factors is None:
		return None
	return product([factor ** exp for factor, exp in factors.items()],1)
	
def one():
	return {1: 1}
	
def find_factors(prime_factors : Dict[int,int]) -> List[Dict[int,int]]:
	original = factors_to_num(prime_factors)
	
	factors = []
	index = 0
	sorted_primes = sorted(prime_factors.keys())
	sorted_primes.remove(1)
	max_of_factor = [prime_factors[prime] for prime in sorted_primes if prime != 1]
	
	mods = [max + 1 for max in max_of_factor]
	
	for i in range(1, product(mods,1)):
		temp = 1
		num = i # technically not necessary in Python
		for prime,mod in zip(sorted_primes,mods):
			temp *= prime ** ((num % mod))
			num = num // mod
			
		factors.append((temp,original // temp))
		
	return factors
	
def gcd(p : int, q : int) -> int:
	"""
	implements euclid's algorithm
	"""
	
	if p <= 0 or q <= 0:
		return None
		
	while p != q:
		if p > q:
			p -= q
		else:
			q -= p
			
	return p
	
	
def move_prime_factor(dest : Dict[int,int], src : Dict[int,int]) -> int:
	"""
	no longer needed
	"""
	
	if dest is None or src is None or src == {1:1}:
		return None
		
	factors = list(src.keys()).copy()
		
	for factor in factors:
		if factor != 1:
			dest[factor] = dest.get(factor, 0) + 1
			if src[factor] == 1:
				src.pop(factor)
			else:
				src[factor] -= 1
			# mutations done between each yield
			yield factor
			# fixed before next iteration
			src[factor] = src.get(factor, 0) + 1
			if dest[factor] == 1:
				dest.pop(factor)
			else:
				dest[factor] -= 1
				


