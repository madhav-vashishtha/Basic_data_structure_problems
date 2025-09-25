dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 3, "c": 4, "d": 5}

merged = {}

for d in (dict1, dict2):
    for k, v in d.items():
        merged[k] = merged.get(k, 0) + v

print(merged)
