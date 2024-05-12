'''
You are given a three integers 'X', 'N', and 'M'. Your task is to find ('X' ^ 'N') % 'M'. A ^ B is defined as A raised to power B and A % C is the remainder when A is divided by C.
'''

import sys
sys.setrecursionlimit(10**7)

def modularExponentiation(x, n, m):
	# Write your code here.
	if n == 0:
		return 1 % m
	result = modularExponentiation(x, n // 2, m)
	result = (result * result) % m
	if n % 2 == 1:
		result = (result * x) % m
	return result


if __name__ == "__main__":
    print(modularExponentiation(3,1,2))