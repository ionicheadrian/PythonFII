input_str = input("Sirul tau:")

print("="*60)
print(f"Input : {input_str}")
print("="*60)

for c in input_str:
    if c.isnumeric():
        input_str = input_str.replace(c,"")

print(f"Input-ul schimbat:{input_str}")