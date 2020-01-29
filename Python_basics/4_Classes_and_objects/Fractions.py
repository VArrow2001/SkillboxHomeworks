### YOUR CODE HERE ###
class Fraction:

    def __init__(self, numerator, denominator):
        if numerator * denominator > 0:
            self.num = abs(numerator)
            self.den = abs(denominator)
        else:
            self.num = -abs(numerator)
            self.den = abs(denominator)
        self.num, self.den = self.reduce()

    def primes(n):
        if n < 2:
            return []
        else:
            prime_list = [2]
            for i in range(3, n + 1):
                is_prime = True
                for j in prime_list:
                    if i % j == 0:
                        is_prime = False
                        break
                if is_prime:
                    prime_list.append(i)
            return prime_list

    def reduce(self):
        n_primes = Fraction.primes(abs(int(max([self.num, self.den]) ** 0.5) + 1))
        new_num = self.num
        new_den = self.den
        for i in n_primes:
            while (new_num % i == 0) & (new_den % i == 0):
                new_num //= i
                new_den //= i
        return [new_num, new_den]

    def __add__(self, other):
        if isinstance(other, int):
            new_fr = Fraction(numerator=self.num + other * self.den, denominator=self.den)
        elif isinstance(other, Fraction):
            new_den = self.den * other.den
            new_num = self.num * other.den + self.den * other.num
            new_fr = Fraction(numerator=new_num, denominator=new_den)
        return new_fr

    def __sub__(self, other):
        if isinstance(other, int):
            substr = Fraction(numerator=self.den * other, denominator=self.den)
        elif isinstance(other, Fraction):
            substr = other
        new_den = self.den * substr.den
        new_num = self.num * substr.den - self.den * substr.num
        new_fr = Fraction(numerator=new_num, denominator=new_den)
        return new_fr

    def __mul__(self, other):
        if isinstance(other, int):
            return Fraction(numerator=self.num * other, denominator=self.den)
        elif isinstance(other, Fraction):
            return Fraction(numerator=self.num * other.num, denominator=self.den*other.den)

    def __int__(self):
        return self.num // self.den

    def __float__(self):
        return self.num / self.den

a = Fraction(numerator=1, denominator=2)
b = Fraction(numerator=-1, denominator=4)
c = a + b
d = a - b
print(a.num, a.den, b.num, b.den, c.num, c.den, d.num, d.den)
