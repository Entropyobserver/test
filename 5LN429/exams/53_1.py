
"""
import string

def f3(words):
    print(f"\nInput words list: {words}")
    print(f"Input words type: {type(words)}")
    print("\nProcessing each word...")
    
    # Create a dictionary for words longer than five characters with their lengths
    result = {}
    print(f"Initial empty result dictionary: {result}")
    
    for i, word in enumerate(words):
        print(f"\nStep {i+1}:")
        print(f"  Original word: '{word}'")
        
        # Remove punctuation and check word length
        cleaned_word = word.strip(string.punctuation)
        print(f"  After removing punctuation: '{cleaned_word}'")
        print(f"  Word length: {len(cleaned_word)}")
        
        if len(cleaned_word) > 5:
            print(f"  ✓ Word '{cleaned_word}' is longer than 5 characters")
            result[cleaned_word] = len(cleaned_word)
            print(f"  Added to dictionary - Current result: {result}")
        else:
            print(f"  ✗ Word '{cleaned_word}' is NOT longer than 5 characters - skipping")
            
    print(f"\nFinal result dictionary: {result}")
    print(f"Final result type: {type(result)}")
    return result

# Test the function
chomsky_quote = "If we don't believe in freedom of expression for people we despise, we don't believe in it at all".split()
print("Starting function execution with Chomsky quote...")
print(f"Original quote split into words: {chomsky_quote}")
result = f3(chomsky_quote)
print(f"\nFunction returned: {result}")
"""

import string

def f3(words):
    print(f"\nInput words list: {words}")
    print(f"Input words type: {type(words)}")
    print("\nProcessing each word...")
    
    # Create a dictionary for words longer than five characters with their lengths
    result = {}
    print(f"Initial empty result dictionary: {result}")
    
    # Keep track of word occurrences
    word_count = {}
    
    for i, word in enumerate(words):
        print(f"\nStep {i+1}:")
        print(f"  Original word: '{word}'")
        
        # Remove punctuation and check word length
        cleaned_word = word.strip(string.punctuation)
        print(f"  After removing punctuation: '{cleaned_word}'")
        print(f"  Word length: {len(cleaned_word)}")
        
        # Track word occurrences
        word_count[cleaned_word] = word_count.get(cleaned_word, 0) + 1
        print(f"  This word has appeared {word_count[cleaned_word]} times")
        
        if len(cleaned_word) > 5:
            print(f"  ✓ Word '{cleaned_word}' is longer than 5 characters")
            if cleaned_word in result:
                print(f"  ! Note: This word is already in dictionary - value will be updated")
            result[cleaned_word] = len(cleaned_word)
            print(f"  Current result: {result}")
        else:
            print(f"  ✗ Word '{cleaned_word}' is NOT longer than 5 characters - skipping")
            
    print(f"\nFinal result dictionary: {result}")
    print(f"Final result type: {type(result)}")
    print("\nWord occurrence count:")
    for word, count in word_count.items():
        if count > 1 and word in result:
            print(f"  '{word}' appeared {count} times but is only stored once in result")
    return result

# Test the function with repeated words
chomsky_quote = "If we don't believe in freedom of expression for people we despise, we don't believe in it at all".split()
test = "If, we don't believe in freedom. of expression, for people. we despise, we don't believe in it at all".split()
print("Starting function execution with Chomsky quote...")
print(f"Original quote split into words: {chomsky_quote}")
#result = f3(chomsky_quote)
result = f3(test)
print(f"\nFunction returned: {result}")