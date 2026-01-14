'''Pronic numbers are numbers that are formed by
the product oftwo consecutive (successive) natural numbers.
FORMULA: 𝑛 ∗ (𝑛 + 1)'''


def is_pronic_number(num):
    for n in range(1, int(num**0.5) + 1):
        if 𝑛 * (𝑛 + 1) == num:
            return True
    return False

print("Pronic numbers between 1 and 100 are:")
for i in range(1, 101):
    if is_pronic_number(i):
        print(i, end=" | ")

