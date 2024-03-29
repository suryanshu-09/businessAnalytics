import re
print("input 6 names")
names = []
for i in range(6):
    names.append(input())
pattern = r'^a'
print("\noutput:")
for name in names:
    if re.search(pattern, name.lower()):
       print(name)
