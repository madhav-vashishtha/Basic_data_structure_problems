main_string=input("enter the main string: ")
substring=input("enter the substring to search for: ")

if substring in main_string:
    print(f"'{substring}' is present in the main string.")
else:
    print(f"'{substring}' is NOT present in the main string.")
