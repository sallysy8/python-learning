'''
This is the note in class
'''

class A:
    def __init__(self):
        print("init A")

    def yo(self):
        print("yo A")

    def num(self, n):
        print("A", n)

class B(A):
    def __init__(self):
        print("init B")
        super().__init__()

    def yo(self):
        print("yo B")
        super().yo()

    def num(self, n):
        print("B", n)
        super().num(n)

class C(A):
    def __init__(self):
        print("init C")
        super().__init__()

    def yo(self):
        print("yo C")
        super().yo()

    def num(self, n):
        print("C", n)


class D(B,C):
    def __init__(self):
        print("init D")
        super().__init__()

    def yo(self):
        print("yo D")
        #super().yo()

        super(B, self).yo()

    def num(self, n):
        print("D", n)
        super(B, self).num(n)
        #c.num(self, n)



d = D()
d.yo()
d.num(20)


sum([1,3,4])
len("".join(["shinv", "uysbvihv", "sbiuyhv"]))

