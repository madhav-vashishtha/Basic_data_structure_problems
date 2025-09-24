num=int(input("enter your number: "))

def sum_of_list(number):
    total=0
    for digit in str(number):
        total += int(digit)
    return total
print(sum_of_list(num))
