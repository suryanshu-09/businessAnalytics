print("Enter word:")
word = input().lower()
vowel_count = 0
for char in word:
    if char in ('a', 'e', 'i', 'o', 'u'):
        vowel_count += 1 
print(vowel_count)
