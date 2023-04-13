import ctypes
import sys
import gc

my_var = 10
print(hex(id(my_var)))
# a = [1, 2, 3]
# b = a
# c = b
# print(id(a))
# print(sys.getrefcount(a) - 1)


def ref_count(address: int):
    return ctypes.c_long.from_address(address).value


def object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return "Object exists"

    return "Not found"


class A:
    def __init__(self):
        self.b = B(self)
        print("A: self: {0}, b: {1}".format(hex(id(self)), hex(id(self.b))))


class B:
    def __init__(self, a):
        self.a = a
        print("B: self: {0}, a: {1}".format(hex(id(self)), hex(id(self.a))))


gc.disable()

my_var = A()
a_id = id(my_var)
b_id = id(my_var.b)
print(hex(id(my_var)))
print(hex(id(my_var.b)))
print(object_by_id(id(my_var)))
print(object_by_id(id(my_var.b)))
my_var = None
print(ref_count(a_id))
print(ref_count(b_id))

complex_num = 3+4j
complex_num2 = 3+4j
print(hex(id(complex_num)))
print(hex(id(complex_num2)))

# print(ref_count(id(a)))

tup = ([1, 2], [3, 4])
print(id(tup))
tup[0].append(3)
print(id(tup))


def process(s):
    s.append(100)


lst = [1, 2, 3]
process(lst)
print(lst)

k = None
p = None
print(k is p)

print(help(int(0)))
print(int() * 10000000)


def my_func(e):
    a = "a" * 19
    b = "cxd" * 3
    c = 8 * 100
    d = (1, 2) * 4
    if e in {1, 7, 10}:
        pass


print(my_func.__code__.co_consts)

if __name__ == '__main__':
    print('')
