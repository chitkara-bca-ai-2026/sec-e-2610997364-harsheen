
print("----- DOCUMENT ANALYSIS SYSTEM -----")

sentence = input("Enter a sentence: ")

words = len(sentence.split())

vowels = 0
consonants = 0
digits = 0
spaces = 0
special = 0

for ch in sentence:

    if ch.lower() in "aeiou":
        vowels += 1

    elif ch.isalpha():
        consonants += 1

    elif ch.isdigit():
        digits += 1

    elif ch == " ":
        spaces += 1

    else:
        special += 1

print("\n----- DOCUMENT ANALYSIS REPORT -----")
print(f"Total Words: {words}")
print(f"Total Vowels: {vowels}")
print(f"Total Consonants: {consonants}")
print(f"Total Digits: {digits}")
print(f"Total Spaces: {spaces}")
print(f"Total Special Characters: {special}")

print("------------------------------------")
