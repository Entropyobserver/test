def is_consonant(char):
    #if char in 'bcdfghjklmnpqrstvwxyz':
    char = char.lower()
    #if char not in 'aeiou':
    #    return char
    if char in 'aeiou':
        return False
    else:
        return True
def get_count(text):
    count = 0
    for char in text:
        if is_consonant(char):
            count += 1
    return count
def main():
    text = "test"
    consonant_count = get_count(text)
    print(consonant_count)
main()
