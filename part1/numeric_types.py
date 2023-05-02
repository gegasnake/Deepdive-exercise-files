import sys
import math
import cmath
import fractions
import decimal
import time
from decimal import Decimal
import string

print(type(100))
print(math.floor(-3.00000000000000001))  # -3

a = int()
print(a)
print(sys.getsizeof(1))
print(int(True), int(False))

b = fractions.Fraction(22, 7)

print(b)
print(type(b))
print("12345")
print(int("101", base=2))
print(int("ff", 16))
print(bin(900))
print(hex(255))
print(0b101 + 0b100)


def from_base10(n, b):
    if b < 2:
        raise ValueError("Base b must be greater than or equal to 2")
    if n < 0:
        raise ValueError("Number n must be greater than or equal to 0")
    if n == 0:
        return [0]
    digits = []
    while n > 0:
        n, m = divmod(n, b)
        digits.insert(0, m)
    return digits


print(from_base10(255, 16))


def encode(digits, digit_map):
    if max(digits) >= len(digit_map):
        raise ValueError("digit_map is not long enough to encode the digits")
    # encoding = ''
    # for d in digits:
    #    encoding += digit_map[d]
    encoding = ''.join([digit_map[d] for d in digits])

    return encoding


print(encode([14, 15], '0123456789ABCDEF'))


def rebase_from10(number, base):
    digit_map = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if base < 2 or base > 36:
        raise ValueError("Invalid base")
    sign = -1 if number < 0 else 1
    number *= sign

    digits = from_base10(number, base)
    encoding = encode(digits, digit_map)
    if sign == -1:
        encoding = "-" + encoding
    return encoding


e = rebase_from10(10, 2)
print(e)
print(int(e, base=2))

f = rebase_from10(3451, 16)
print(f)
print(int(f, base=16))

n = rebase_from10(-314, 2)
print(n)
print(int(n, base=2))

x = fractions.Fraction(0.3)
x = x.limit_denominator(10)
print(x)
y = 0.1
print(format(y, ".25f"))
a = 0.1 + 0.1 + 0.1
b = 0.3
print(a == b)


first = 1000.01
second = 1000.02
L = 0.01
M = 0.02

print(round(first, 1) == round(second, 1))
print(round(L, 1) == round(M, 1))

print(math.isclose(a, b))
print(a == b)

num1 = 123456789.109
num2 = 123456789.110
num11 = 0.109
num22 = 0.110

print(math.isclose(num1, num2, rel_tol=0.001))
print(math.isclose(num11, num22, rel_tol=0.001))

absolute1 = 0.0000001
absolute2 = 0.0000002
print(math.isclose(absolute1, absolute2, rel_tol=0.01, abs_tol=0.01))

# truncation, ceiling and floor
print(math.trunc(10.3), math.trunc(10.9), math.trunc(10 + math.pi))
# math.trunc == int
print(int(10.3), int(10.9), int(10 + math.pi))

# floor
print(math.floor(10.3), math.floor(10.4), math.floor(10.9))
# negative floor
print(math.floor(-10.3), math.floor(-10.4), math.floor(-10.9))

# ceiling
print(math.ceil(10.3), math.ceil(10.4), math.ceil(10.9))
# negative ceiling
print(math.ceil(-10.3), math.ceil(-10.4), math.ceil(-10.5))

rn = round(1.9)
print(rn, type(rn))

rn2 = round(1.9, 0)
print(rn2, type(rn2))

print(round(888.09, -3))

print(round(1.25, 1))

print(round(-1.25, 1))
print(round(-1.35, 1))


def _round(x):
    return int(x + 0.5 * math.copysign(1, x))


print(round(-2.5), _round(-2.5))

# Decimals

print(decimal.getcontext())

print(decimal.getcontext().prec)
g_ctx = decimal.getcontext()
g_ctx.prec = 6
g_ctx.rounding = decimal.ROUND_HALF_UP
print(type(g_ctx.rounding))
print(g_ctx)

# Local context

with decimal.localcontext() as ctx:
    ctx.prec = 8
    ctx.rounding = decimal.ROUND_HALF_UP
    d1 = Decimal('1.25').__round__()
    d2 = Decimal('1.35').__round__()
    print(d1, d2)
    print(ctx)

print(d1, d2)
print(Decimal("10.1"))
print(Decimal(19.1))
t = (1, (1, 9, 9), 2)
print(Decimal(t))
print(Decimal(0.1) == Decimal("0.1"))
print(Decimal(10) == Decimal("10"))

decimal.getcontext().prec = 2
print(Decimal(20.45666) + Decimal(10.22222))

x = -10
y = 3
print(x // y, x % y)
print(divmod(x, y))
print(x == y * (x // y) + (x % y))

x = Decimal(-10)
y = Decimal(3)
print(x // y, x % y)
print(divmod(x, y))
print(x == y * (x // y) + (x % y))

fl = 3.12345
dec = Decimal("3.12345")
print(sys.getsizeof(fl), sys.getsizeof(dec))


def run_float(n=1):
    for i in range(n):
        flt = 3.12345


def run_decimal(n=1):
    for i in range(n):
        decml = Decimal("3.12345")


n = 1000000

start1 = time.perf_counter()
run_float(n)
end1 = time.perf_counter()
print('float operation took {} seconds'.format(end1 - start1))

start2 = time.perf_counter()
run_decimal(n)
end2 = time.perf_counter()
print('decimal operation took {} seconds'.format(end2 - start2))


# Complex Numbers

comp = complex(1, 2)
b = 1 + 2j
c = 1 + 2J
print(comp == b == c)
print(a.real, type(a.real))
print(b.conjugate())

K = 1 + 2j
M = 1 + 10J
print(M - 5 * K)
print(K * M)
print(K / M)

v = 0.1j
print(format(v.imag, '.25f'))
print(type(cmath.pi))
print(cmath.pi)

# booleans

print(issubclass(bool, int))
print(type(True), id(True), int(True))
print(type(False), id(False), int(False))
print(3 < 4)
print(id(3 < 4))
print(True == 1)
print((1 == 2) == False)
print(1 + True)
print(100 * False)
print(True > False)


print(bool(1 + 1j))
print(bool(0 + 0j))
print(bool(Decimal(0.0)))
print(bool(-1))
print((100).__bool__())
print(bool([]))
print(bool([].__len__()))

# boolean precedence
print(True or True and False)
print((True or True) and False)

# Short-circuiting

a = 10
b = 2

if b and a / b > 2:
    print('a is at least 2 * b')

a = 'c'

print(a in string.ascii_uppercase)
print(string.digits)


name = 'abc'
if name and name[0] in string.digits:
    print('Name cannot start with a digit')

# Boolean operators

# X or Y

print('a' or [1, 2])
print('' or [1, 2])
print([1, 2] or 'a')
print(1 or 1/0)
# print(0 or 1/0)

s1 = None
s2 = ''
s3 = 'abc'

# s1 = s1 or 'not available'
# s2 = s2 or 'not available'
# s3 = s3 or 'not available'

print(s1, s2, s3)

# X and Y

print(None and 7)
print([] and [0])

a = 2
b = 4
print(b and a/b)

print((s1 and s1[0]) or '')
print((s2 and s2[0]) or '')
print((s3 and s3[0]) or '')

# not operator

print(not True)
print(not False)
print(not 1)
print(not '')

# Comparison operators

print([1, 2] is [1, 2])
print('a' in 'hello my name is Gega')
print(3 not in [1, 2, 3])
print(3 < 5)
print(Decimal('0.3') > 0.2)
print(fractions.Fraction(2, 5) > 0.2)
print(4 == 4 + 0j)
print(True == fractions.Fraction(4, 4))
print(True < fractions.Fraction(5, 4))
print(1 < 2 < 3)
print(3 < 2 < 1/0)
print(1 < 2 > -4)
print(1 < 2 > -4 == Decimal('-4'))


if __name__ == '__main__':
    print('')

