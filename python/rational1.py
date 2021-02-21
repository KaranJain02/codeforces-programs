from math import gcd

class Rational:
    def __init__(self, p, q):
        g = gcd(p, q)
        self.p = p // g
        self.q = q // g
    def add(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)
    def sub(self, r):
        return Rational(self.p * r.q - self.q * r.p, self.q * r.q)
    def mul(self, r):
        return Rational(self.p * r.p, self.q * r.q)
    def div(self, r):
        return Rational(self.p * r.q, self.q * r.p)
    def toFloat(self):
        return self.p / self.q

oneHalf = Rational(1,2)
oneThird = Rational(1,3)
fiveSixths = oneHalf.add(oneThird)
print(fiveSixths.p, '/', fiveSixths.q)
