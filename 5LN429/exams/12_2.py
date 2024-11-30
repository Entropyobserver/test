import re

def analyze_regex_groups(pattern, texts):
    """
    Analyzes regex groups for each text match.
    
    Args:
        pattern (str): Regex pattern to match
        texts (list): List of texts to check against the pattern
    """
    print("Pattern:", pattern)
    print("Pattern breakdown:")
    print("- st: literal 'st'")
    print("- (o(le(en)?)|eal(s|ing)?): main group with two alternatives")
    print("  - Alternative 1: o(le(en)?))")
    print("  - Alternative 2: eal(s|ing)?")
    print("\nAnalyzing matches:\n")
    
    for text in texts:
        match = re.match(pattern, text)
        if match:
            print(f"Text: {text}")
            
            # Get all possible groups
            all_groups = match.groups()
            print(f"Total groups found: {len(all_groups)}")
            
            # Show each group with its content
            print("Group 0 (full match):", match.group(0))
            for i in range(1, len(all_groups) + 1):
                group_content = match.group(i)
                if group_content is not None:
                    print(f"Group {i}: '{group_content}'")
                else:
                    print(f"Group {i}: None")
            
            # Show group spans
            for i in range(len(all_groups) + 1):
                span = match.span(i)
                print(f"Group {i} span: {span}")
            
            print("\nGroup explanation:")
            if 'eal' in text:
                print("- Using 'eal' alternative")
            else:
                print("- Using 'ole' alternative")
            print("-" * 40 + "\n")

# Test pattern
pattern = r"st(o(le(en)?)|eal(s|ing)?)"
texts = ["steal", "steals", "stealing", "stole", "stolen"]

analyze_regex_groups(pattern, texts)