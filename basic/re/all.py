import re
from colorama import init, Fore, Back, Style

# Initialize colorama for cross-platform colored output
init()

# Sample text containing various patterns to match
sample_text = """
Contact Information:
John Doe
123-45-6789
555-123-4567
john.doe123@email.com
jane_smith@company.co.uk

Important Dates:
Meeting on 2024-03-15
Due by March 15, 2024

Product Codes:
ABC123
XYZ-789
TEST_123

Additional Notes:
#1 - First item
#2 - Second item
$100.00
https://www.example.com
"""

def print_highlighted_matches(text, pattern):
    """
    Print text with matched patterns highlighted in color
    """
    last_end = 0
    matches = list(re.finditer(pattern, text))
    
    if not matches:
        print(f"{Fore.RED}No matches found{Style.RESET_ALL}")
        return
    
    result = ""
    for match in matches:
        start, end = match.span()
        # Add text before the match
        result += text[last_end:start]
        # Add the highlighted match
        result += f"{Fore.GREEN}{Back.BLACK}{text[start:end]}{Style.RESET_ALL}"
        last_end = end
    
    # Add remaining text
    result += text[last_end:]
    print(result)

def demonstrate_pattern(pattern, description, text=sample_text, show_full_text=True):
    print(f"\n{Fore.YELLOW}{'='*70}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Pattern:{Style.RESET_ALL} {pattern}")
    print(f"{Fore.CYAN}Description:{Style.RESET_ALL} {description}")
    print(f"{Fore.CYAN}Matches:{Style.RESET_ALL}")
    
    if show_full_text:
        print(f"\n{Fore.CYAN}Text with highlighted matches:{Style.RESET_ALL}")
        print_highlighted_matches(text, pattern)
    
    # Print individual matches
    matches = list(re.finditer(pattern, text))
    for i, match in enumerate(matches, 1):
        print(f"{Fore.BLUE}Match {i}:{Style.RESET_ALL} '{Fore.GREEN}{match.group()}{Style.RESET_ALL}' "
              f"at position {match.start()}-{match.end()}")

print(f"{Fore.YELLOW}Original Text:{Style.RESET_ALL}")
print(sample_text)

# 1. Basic Symbols
print(f"\n{Fore.YELLOW}=== Basic Symbols ==={Style.RESET_ALL}")

demonstrate_pattern(
    r".",
    "Matches any single character (first 10 characters)",
    sample_text[:10],
    True
)

demonstrate_pattern(
    r"^Contact",
    "Matches 'Contact' at the start of a line"
)

demonstrate_pattern(
    r"com$",
    "Matches 'com' at the end of a line"
)

# 2. Character Classes
print(f"\n{Fore.YELLOW}=== Character Classes ==={Style.RESET_ALL}")

demonstrate_pattern(
    r"[aeiou]",
    "Matches any vowel (first line only)",
    sample_text.split('\n')[1]
)

demonstrate_pattern(
    r"[A-Z]{3}",
    "Matches three consecutive capital letters"
)

demonstrate_pattern(
    r"\d{3}-\d{2}-\d{4}",
    "Matches Social Security Number pattern"
)

demonstrate_pattern(
    r"\w+@\w+\.\w+",
    "Matches basic email pattern"
)

# 3. Quantifiers
print(f"\n{Fore.YELLOW}=== Quantifiers ==={Style.RESET_ALL}")

demonstrate_pattern(
    r"\d+",
    "Matches one or more digits"
)

demonstrate_pattern(
    r"\w{3}",
    "Matches exactly three word characters (first line only)",
    sample_text.split('\n')[1]
)

# 4. Groups and Alternation
print(f"\n{Fore.YELLOW}=== Groups and Alternation ==={Style.RESET_ALL}")

demonstrate_pattern(
    r"(John|Jane)",
    "Matches either 'John' or 'Jane'"
)

demonstrate_pattern(
    r"(\w+)@(\w+)",
    "Matches username and domain in email addresses"
)

# 5. Common Use Cases
print(f"\n{Fore.YELLOW}=== Common Use Cases ==={Style.RESET_ALL}")

demonstrate_pattern(
    r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "Matches email addresses"
)

demonstrate_pattern(
    r"\d{3}-\d{3}-\d{4}",
    "Matches phone numbers"
)

demonstrate_pattern(
    r"\d{4}-\d{2}-\d{2}",
    "Matches dates in YYYY-MM-DD format"
)

# 6. Lookahead and Lookbehind
print(f"\n{Fore.YELLOW}=== Lookahead and Lookbehind ==={Style.RESET_ALL}")

demonstrate_pattern(
    r"\w+(?=@)",
    "Matches usernames before @ in email addresses"
)

demonstrate_pattern(
    r"(?<=\$)\d+\.\d{2}",
    "Matches price values after dollar sign"
)

# 7. Word Boundaries
print(f"\n{Fore.YELLOW}=== Word Boundaries ==={Style.RESET_ALL}")

demonstrate_pattern(
    r"\b\w{4}\b",
    "Matches exactly four-letter words"
)

# 8. Complex Patterns
print(f"\n{Fore.YELLOW}=== Complex Patterns ==={Style.RESET_ALL}")

demonstrate_pattern(
    r"https?://[\w.-]+\.[a-zA-Z]{2,}",
    "Matches URLs"
)

demonstrate_pattern(
    r"\$\d+\.\d{2}",
    "Matches currency values"
)

demonstrate_pattern(
    r"[A-Z]{3}[-_]?\d{3}",
    "Matches product codes"
)

# Cleanup
print(Style.RESET_ALL)