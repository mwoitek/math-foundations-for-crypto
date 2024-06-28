# %%
def mod_exp(b: int, e: int, m: int) -> int:
    result = 1
    for _ in range(e):
        result = (b * result) % m
    return result


# %%
def miller_rabin(s: int, d: int, a: int) -> bool:
    n = (2**s) * d + 1
    minus_1 = (-1) % n

    x = mod_exp(a, d, n)
    if x == 1 or x == minus_1:
        return True

    for _ in range(s):
        x = mod_exp(x, 2, n)
        if x == minus_1:
            return True

    return False


# %%
s = 4
d = 35
a = 7
print(miller_rabin(s, d, a))

# %%
s = 1
d = 281
a = 7
print(miller_rabin(s, d, a))

# %%
s = 2
d = 55
bases = [5, 16, 93, 174]

for a in bases:
    if miller_rabin(s, d, a):
        print(a)
