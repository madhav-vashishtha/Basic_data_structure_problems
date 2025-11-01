def calculate_lift_rounds(n, capacity):
    rounds = (n + capacity - 1 ) // capacity
    return rounds
print(calculate_lift_rounds(3,2)) 