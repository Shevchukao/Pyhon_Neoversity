from decimal import Decimal, ROUND_HALF_EVEN, R

print(0.1 + 0.2)  # 0.30000000000000004
print(Decimal("0.1") + Decimal("0.2"))  # 0.3
print(Decimal("0.1").log10())  # -1
n = Decimal("3.55")
n_rounded = n.quantize(Decimal("0.0"))
print(n_rounded)  # 3.6
n_rounded = n.quantize(Decimal("0"))
print(n_rounded)  # 4

n = Decimal("3.44")
n_rounded = n.quantize(Decimal("0"))
print(n_rounded)  # 3

n = Decimal("3.5")
n_rounded = n.quantize(Decimal("0"), rounding=ROUND_HALF_EVEN)
print(n_rounded)  # 4, rounding to even number end on 0, 2, 4, 6, 8

n = Decimal("4.5")
n_rounded = n.quantize(Decimal("0"), rounding=ROUND_HALF_EVEN)
print(n_rounded)  # 4, rounding to even number end on 0, 2, 4, 6, 8

n = Decimal("3.55")
n_rounded = n.quantize(Decimal("0.0"), rounding=ROUND_HALF_EVEN)
print(n_rounded)  # 3.6, rounding to even number end on 0, 2, 4, 6, 8

n = Decimal("3.65")
n_rounded = n.quantize(Decimal("0.0"), rounding=ROUND_HALF_EVEN)
print(n_rounded)  # 3.6, rounding to even number end on 0, 2, 4, 6, 8
