
def most_common_character(s):
    char_counts = {}
    for c in s:
        if c in char_counts:
            char_counts[c] += 1
        else:
            char_counts[c] = 1
    max_count = max(char_counts.values())
    for c in s:
        if char_counts[c] == max_count:
            return c
if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))
if __name__ == "__main__":
    second_string = "exemplaryelementary"
    print(most_common_character(second_string))