'''Decimal number ko manually binary, octal, aur hexadecimal mein convert karne ke liye hum repeated
division method use karte hain. Is method mein decimal number ko us base se baar-baar divide karte
hain (binary ke liye 2, octal ke liye 8, aur hexadecimal ke liye 16) aur remainders note karte hain.
Last mein remainders ko bottom se top padhte hain.'''

dec_num = int(input("Enter a decimal number: "))

print("The decimal value of", dec_num, "is:")
print(bin(dec_num), "in binary.")
print(oct(dec_num), "in octal.")
print(hex(dec_num), "in hexadecimal.")

