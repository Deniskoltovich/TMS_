# method resolution order

class O: pass
class A(O): pass
class B(O): pass
class C(O):pass
class D(O): pass
class E(O): pass
class K1(A, B, C):pass
class K2(B, C): pass
class K3(C, D, E): pass
class Z(K1, K2, K3): pass

print(Z.mro())

