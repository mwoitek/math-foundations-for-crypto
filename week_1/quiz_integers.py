# %%
def is_congruent_pair(pair: tuple[int, int], n: int) -> bool:
    x1, x2 = pair
    return x1 % n == x2 % n


# %%
def find_congruent_pair(pairs: list[tuple[int, int]], n: int) -> tuple[int, int] | None:
    for pair in pairs:
        if is_congruent_pair(pair, n):
            return pair
    return None


# %%
pairs = [
    (-17, 9),
    (-4, 4),
    (21001, 21013),
    (3, 113),
]
n = 13
print(find_congruent_pair(pairs, n))
