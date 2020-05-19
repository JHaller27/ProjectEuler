import utils.sieve_of_eratosthenes as sieve

num = 600851475143
sieve.is_prime(int(num**.5))
print(max(sieve.prime_factors(num)))
