# %%
def mod_exp(b: int, e: int, m: int) -> int:
    result = 1
    for _ in range(e):
        result = (b * result) % m
    return result


# %%
print(mod_exp(47, 69, 143))
