def subtract_product_and_sum(n):
    product = 1
    total = 0

    while n > 0:
        digit = n % 10
        product *= digit
        total += digit
        n //= 10

    return product - total

print(subtract_product_and_sum(264))
print(subtract_product_and_sum(4421))