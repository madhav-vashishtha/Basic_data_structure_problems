def remove_duplicates(s):
    return "".join(dict.fromkeys(s))

print(remove_duplicates("programming"))
