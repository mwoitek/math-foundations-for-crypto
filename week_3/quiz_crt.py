# %%
from itertools import combinations
from math import gcd, prod

# %%
x = 12345
moduli = [5, 7, 8, 9]
for m in moduli:
    print(f"x mod {m} = {x % m}")


# %%
def multiplicative_inverse_naive(x: int, n: int) -> int | None:
    for i in range(1, n):
        if (x * i) % n == 1:
            return i
    return None


# %%
def crt_coefficients(moduli: list[int]) -> list[int]:
    n = prod(moduli)
    inverses = [multiplicative_inverse_naive(n // m, m) for m in moduli]
    return [(i * n // m) % n for m, i in zip(moduli, inverses) if isinstance(i, int)]


# %%
def least_residue(moduli: list[int], residues: list[int]) -> int:
    coefficients = crt_coefficients(moduli)
    return sum(a * r for a, r in zip(coefficients, residues)) % prod(moduli)


# %%
coefficients = crt_coefficients(moduli)
print(coefficients)

# %%
residues = [0, 4, 0, 3]
lr = least_residue(moduli, residues)
print(lr)

# %%
candidates = [
    [2, 3, 4, 5, 6, 7],
    [5, 7, 8, 18],
    [2, 3, 5, 7],
    [9, 16, 35],
]

for candidate in candidates:
    if prod(candidate) == 5040 and all(gcd(a, b) == 1 for a, b in combinations(candidate, 2)):
        print(candidate)

# %%
moduli = [2, 3, 5]
coefficients = crt_coefficients(moduli)
print(coefficients)

# %%
moduli = [7, 8, 9]
coefficients = crt_coefficients(moduli)
print(coefficients)

residues = [4, 4, 4]
lr = least_residue(moduli, residues)
print(lr)

# %%
x = 12345
for m in moduli:
    print(f"x mod {m} = {x % m}")

# %%
x = 82734
for m in moduli:
    print(f"x mod {m} = {x % m}")

# %%
x = 46189
for m in moduli:
    print(f"x mod {m} = {x % m}")

# %%
residues = [3, 5, 1]
for r, m in zip(residues, moduli):
    print(multiplicative_inverse_naive(r, m))
