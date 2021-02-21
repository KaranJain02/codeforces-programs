from math import gcd

class Rational:
    def __init__(self, p, q):
        g = gcd(p, q)
        self.p = p // g
        self.q = q // g
    def __str__(self):
        return '{}/{}'.format(self.p, self.q)
    def __repr__(self):
        return 'Rational({},{})'.format(self.p, self.q)
    
    def __lt__(self, r):
        return self.p * r.q < self.q * r.p
    def __le__(self, r):
        return self.p * r.q <= self.q * r.p
    def __eq__(self, r):
        return self.p * r.q == self.q * r.p
    def __ne__(self, r):
        return self.p * r.q != self.q * r.p
    def __gt__(self, r):
        return self.p * r.q > self.q * r.p
    def __ge__(self, r):
        return self.p * r.q >= self.q * r.p
    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)
    def __sub__(self, r):
        return Rational(self.p * r.q - self.q * r.p, self.q * r.q)
    def __mul__(self, r):
        return Rational(self.p * r.p, self.q * r.q)
    def __div__(self, r):
        return Rational(self.p * r.q, self.q * r.p)
    def toFloat(self):
        # could define __float__, then float(r) will work
        return self.p / self.q

oneHalf = Rational(1,2)
oneThird = Rational(1,3)
fiveSixths = oneHalf + oneThird
print(oneHalf > oneThird)
