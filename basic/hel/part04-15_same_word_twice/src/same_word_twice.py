words = []
unique_words = set()
while True:
    word = input("Word: ")
    if word in unique_words:
        print(f"You typed in {len(words)} different words")
        break
    else:
        unique_words.add(word)
        words.append(word)