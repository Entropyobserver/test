def histogram(s):
    letter_counts = {}
    for letter in s:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    for letter,count in letter_counts.items():
        print(f"{letter} {'*' * count}")
if __name__ == "__main__":
    histogram("hello world")