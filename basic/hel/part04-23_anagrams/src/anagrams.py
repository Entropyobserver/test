def anagrams(s1, s2):
    return sorted(s1) == sorted(s2)
# Write your solution here
if __name__ == "__main__":
    print(anagrams("listen", "silent")) # True
    print(anagrams("hello", "world")) # False