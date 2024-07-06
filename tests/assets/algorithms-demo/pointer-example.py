class C:
    @staticmethod
    def main():
        c = C()  # o_3
        c.m()

    def m(self):
        n1 = One()  # o_12
        n2 = Two()  # o_13
        x = self.id(n1)
        y = self.id(n2)
        x.get()

    def id(self, n: "Number") -> "Number":
        return n


class Number:
    def __init__(self, value):
        self.value = value

    def get(self):
        return self.value


class One(Number):
    def __init__(self):
        super().__init__(1)


class Two(Number):
    def __init__(self):
        super().__init__(2)
