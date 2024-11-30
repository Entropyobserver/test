import string

def clean_text_translate(text):
    """
    Remove all punctuation from the input text using string.translate method.
    
    Args:
        text (str): Input text containing punctuation
        
    Returns:
        str: Cleaned text with all punctuation removed
    """
    print("\nSTEP 1: CLEANING TEXT")
    print("---------------------")
    print(f"Input text: '{text}'")
    
    # Create translation table
    print("\n1.1: Creating translation table")
    print(f"Punctuation marks to remove: {string.punctuation}")
    translator = str.maketrans('', '', string.punctuation)
    
    # Apply translation
    print("\n1.2: Applying translation")
    cleaned_text = text.translate(translator)
    print(f"Cleaned text: '{cleaned_text}'")
    
    return cleaned_text

def text_segmentation_5(string):
    """
    Segment the text into chunks of 5 words each.
    
    Args:
        string (str): Input text to be segmented
        
    Returns:
        list: List of chunks, where each chunk is a list of words
    """
    print("\nSTEP 2: TEXT SEGMENTATION")
    print("--------------------------")
    print(f"Input string: '{string}'")
    
    # Split text into words
    print("\n2.1: Splitting text into words")
    text = string.split()
    print(f"Word list: {text}")
    print(f"Total words: {len(text)}")
    
    # Initialize variables
    print("\n2.2: Initializing segmentation")
    chunk_size = 5
    chunks = []
    print(f"Chunk size: {chunk_size}")
    print(f"Initial chunks list: {chunks}")
    
    # Segment text into chunks
    print("\n2.3: Creating chunks")
    for i in range(0, len(text), chunk_size):
        print(f"\n  Iteration {i//chunk_size + 1}:")
        print(f"  - Starting position: {i}")
        print(f"  - End position: {i + chunk_size}")
        
        # Extract chunk
        chunk = text[i:i + chunk_size]
        print(f"  - Extracted chunk: {chunk}")
        
        # Add chunk to list
        chunks.append(chunk)
        print(f"  - Updated chunks list: {chunks}")
    
    print("\n2.4: Segmentation complete")
    print(f"Final chunks: {chunks}")
    return chunks

def main():
    """
    Main function to demonstrate the text processing pipeline
    """
    print("TEXT PROCESSING PIPELINE")
    print("=======================")
    
    # Initial test text
    test = "This is a very long text that needs to be processed in smaller parts."
    print(f"Original text: '{test}'")
    
    # Clean the text
    cleaned_string = clean_text_translate(test)
    
    # Segment the text
    result = text_segmentation_5(cleaned_string)
    
    # Display final result
    print("\nFINAL RESULT")
    print("============")
    print("Segmented text chunks:")
    for i, chunk in enumerate(result, 1):
        print(f"Chunk {i}: {chunk}")

if __name__ == "__main__":
    main()