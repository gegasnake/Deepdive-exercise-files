def my_func(a=1, b=2, c=3):
    print(f"a={a}, b={b}, c={c}")


my_func(1, 2, 5)
# Error: my_func(1, 2)
# Error: def my_func(a, b=2, c)
my_func(10, 20, 30)
my_func(10)
my_func()


def my_func(a, b=2, c=3):
    print(f"a={a}, b={b}, c={c}")


my_func(c=41, b=10, a=30)
my_func(30, c=41, b=10)
my_func(10, c=30)

# Unpacking iterables
a = (1, 2, 3)
print(type(a))
a = 1, 2, 3
print(type(a))

a = (1)
print(type(a))

a, b, c = [1, 3.14, 'g']
print(a)
print(b)
print(c)

(a, b) = (1, 2)
print(a)
print(b)

x, y, z = 'gega', {1, 2}, [1, 2, 3, 4]
print(x)
print(y)
print(z)

# Swapping variables

x, y, z = z, y, x
print(x)
print(y)
print(z)

for e in "XYZ":
    print(e)

v, n, m = "VNM"
print(v, n, m)

# Set is unordered
j, k, l = {'j', 'k', 'l'}
print(j, k, l)

dct = {'one': 1, "two": 2, "three": 3, "four": 4}
one, two, three, four = dct
print(one, two, three, four)

one, two, three, four = dct.values()
print(one, two, three, four)

for a, b in dct.items():
    print(f"key={a}, value={b}")


# Extended unpacking

lst = [1, 2, 3, 4, 5, 6]

# The first way
a = lst[0]
b = lst[1:]
print(a)
print(b)

# The second way
a, b = lst[0], lst[1:]
print(a)
print(b)

# The third way
a, *b = lst
print(a)
print(b)

s = 'python'

a, *b = s
print(a)  # prints string
print(b)  # prints list

t = ('a', 'b', 'c')

a, *b = t
print(a)  # prints string
print(b)  # prints list

a, b, *c, d = 'python'
print(a)
print(b)
print(c)
print(d)

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l = [*l1, *l2]
print(l)

l1 = [1, 2, 3]
s = {'a', 'b', 'c'}
print([*l1, *s])

s1 = 'abc'
s2 = 'cde'
print({*s1, *s2})

# The first way to convert set to list
s = {1, 'd', 'hello', 99}
print(list(s))

# The second way to convert set to list
*c, = s
print(c)

s1 = {1, 2, 3}
s2 = {3, 4, 5}
print({*s1, *s2})
print(s1.union(s2))

d1 = {'key1': 1, "key2": 2}
d2 = {'key2': 3, "key3": 4}
print({*d1, *d2})
print({**d1, **d2})
print({**d2, **d1})


# Nested unpacking
a, b, e = [1, 2, "XYZ"]
print(a, b, e)

a, b, *e = [1, 2, "XYZ"]
print(a, b , e)

# *args


def func1(a, b, *args):
    print(a, b, args)


print(func1(10, 20))
print(func1(10, 20, 1, 2, 3))


def avg(*args):
    count = len(args)
    total = sum(args)
    return count and total / count


print(avg(2, 2, 4, 4))
print(avg())

l = [10, 20, 30]


def func(a, b, c):
    print(a)
    print(b)
    print(c)


print(func(*l))

# Keyword arguments


def func1(a, b, c):
    print(a, b, c)


func1(1, 2, 3)
func1(1, c=3, b=2)


def func2(a, b, *args, d):
    print(a, b, args, d)


func2(1, 2, 4, 5, d=8)


def func3(*args, d):
    print(args, d)


func3(1, 2, 3, 4, 5, 69, d=41)


def no_pos_arguments(*, d):
    print(d)


no_pos_arguments(d=7)


def func4(a, b, *, d):
    print(a, b, d)


func4(1, 2, d=7)


def func(a, b=1, *args, d, e=True):
    print(a, b, args, d, e)


func(1, 5, 3, 4, d='a', e=False)

# **kwargs


def func(**kwargs):
    print(kwargs)


func(a=1, b=2, c='n')


def func2(*args, **kwargs):
    print(args, kwargs)


func2(1, 3, 4, "gega", a=1, b=100000)


def func(a, b, *, d, **kwargs):
    print(a)
    print(b)
    print(d)
    print(kwargs)


func(1, 2, c=4, d=3)


def fun(a, b=2, c=3, *args):
    print(a, b, c, args)


fun(1, 9, 9, 9, 9)
# fun(1, 'x', 'y', 'z', b=2)

print(1, 2, flush=True)


def cal_hi_lo_avg(*args, log_to_console=False):
    hi = int(bool(args)) and max(args)
    lo = (bool(args)) and min(args)
    avg = (hi + lo) / 2
    if log_to_console:
        print("high={0}, low={1}, avg={2}".format(hi, lo, avg))
    return avg


is_debug = True
av = cal_hi_lo_avg(1, 2, 3, 4, 5, log_to_console=is_debug)

if __name__ == '__main__':
    print('')
