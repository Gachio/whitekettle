
class CountFromBy:

    def __init__(self, v, i):
        self.val = v
        self.incr = i

    def increase(self):
        self.val += self.incr

    def __repr__(self):
        return str(self.val)

k = CountFromBy(0, 1)
k.increase()
print(k)