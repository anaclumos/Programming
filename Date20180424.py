import math
'''
Developed by Sunghyun Cho on 24 April 2018.

If a positive integer N is given,
factorize N in prime factors.
'''

def factorize(number):

	primeNumbers = []
	factors = []
	result = []

	for x in range(2, number+1):
		if isPrime(x):
			primeNumbers.append(x)
	#print("primeNumbers",primeNumbers)

	for member in primeNumbers:
		if number%member == 0:
			factors.append(member)
	#print("factors",factors)

	while len(factors)>0:
		while number%factors[0]==0:
			result.append(factors[0])
			#print(factors[0], "appended to result")
			number/=factors[0]
		#print(factors[0], "removed from factors")
		factors.pop(0)
	return result

def isPrime(number):
	for member in range(2,int(math.sqrt(number)+1)):
		if number % member == 0:
			return False
	return True
print("")
print(factorize(input("Input Number: ")))
print("")