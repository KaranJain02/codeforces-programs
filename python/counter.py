class Counter:
    def __init__(self):
        self.n = 0
    def get(self):
        return self.n
    def inc(self):
        self.n += 1
    def reset(self):
        self.n = 0

cmps = Counter()
swaps = Counter()

def mySortingFunction(a):
    n = len(a)
    for i in range(n):
        m = i
        for j in range(i, n):
            cmps.inc()
            if a[j] < a[m]:
                m = j
        swaps.inc()
        a[i], a[m] = a[m], a[i]

a = [3, 4, 2, 1]
mySortingFunction(a)
print(cmps.get(), swaps.get())
print(a)


