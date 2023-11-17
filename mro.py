class A:
    def process(self):
        print('A process()')


class B:
    pass


class C(A, B):
    pass


obj = C()
obj.process()
print(C.mro())   # print MRO for class C


# MRO - Method Resolution Order
class A1:
    num = 10


class B1(A1):
    pass


class C1(A1):
    num = 1


class D1(B1, C1):
    pass
