
print("----- DOCUMENT TEXT PROCESSING UTILITY -----")

sentence = input("Enter a sentence: ")

position = int(input("Enter position to display character: "))
character = sentence[position]


start = int(input("Enter starting index: "))
end = int(input("Enter ending index: "))
portion = sentence[start:end]


upper = sentence.upper()
lower = sentence.lower()

old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")
replaced = sentence.replace(old_word, new_word)

length = len(sentence)

print("\n----- PROCESSED RESULTS -----")
print("Original Sentence:", sentence)
print("Character at Position:", character)
print("Sliced Sentence:", portion)
print("Uppercase:", upper)
print("Lowercase:", lower)
print("Replaced Sentence:", replaced)
print("Length of Sentence:", length)
