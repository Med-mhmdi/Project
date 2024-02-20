class Solution:
    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def primesum(self, A):
        for i in range(2, A): # A//2 is enough
            if self.is_prime(i) and self.is_prime(A - i):
                return [i, A - i]

#Correct
