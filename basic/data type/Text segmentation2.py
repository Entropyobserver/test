
import string

def clean_text_translate(text):
    """
    Function to clean text by removing punctuation.
    Called by: main() function
    """
    print("\n[FUNCTION CALL] clean_text_translate()")
    print("Input received from main(): text =", text)
    print("\nStep 1: Text Cleaning Process")
    print("============================")
    
    # Step 1.1: Create translation table
    print("\n1.1 Creating translation table")
    print(f"► Using string.punctuation: {string.punctuation}")
    translator = str.maketrans('', '', string.punctuation)
    print(f"► Translation table created")
    
    # Step 1.2: Apply translation
    print("\n1.2 Applying translation to text")
    print(f"► Before translation: '{text}'")
    cleaned_text = text.translate(translator)
    print(f"► After translation: '{cleaned_text}'")
    
    print("\n[FUNCTION RETURN] clean_text_translate()")
    print(f"Returning to main(): cleaned_text = '{cleaned_text}'")
    return cleaned_text

def text_segmentation_5(string):
    """
    Function to segment text into chunks of 5 words.
    Called by: main() function
    """
    print("\n[FUNCTION CALL] text_segmentation_5()")
    print("Input received from main(): string =", string)
    print("\nStep 2: Text Segmentation Process")
    print("==============================")
    
    # Step 2.1: Split text into words
    print("\n2.1 Splitting text into words")
    print(f"► Input string: '{string}'")
    text = string.split()
    print(f"► Word list created: {text}")
    print(f"► Number of words: {len(text)}")
    
    # Step 2.2: Initialize variables
    print("\n2.2 Initializing variables")
    chunk_size = 5
    chunks = []
    print(f"► Set chunk_size = {chunk_size}")
    print(f"► Created empty chunks list: {chunks}")
    
    # Step 2.3: Create chunks
    print("\n2.3 Creating chunks")
    for i in range(0, len(text), chunk_size):
        print(f"\n  Iteration {i//chunk_size + 1}:")
        print(f"  ► Current position: {i}")
        print(f"  ► Slice range: text[{i}:{i + chunk_size}]")
        
        # Extract chunk
        chunk = text[i:i + chunk_size]
        print(f"  ► Extracted words: {chunk}")
        
        # Add to chunks list
        chunks.append(chunk)
        print(f"  ► Updated chunks list: {chunks}")
    
    print("\n[FUNCTION RETURN] text_segmentation_5()")
    print(f"Returning to main(): chunks = {chunks}")
    return chunks

def main():
    """
    Main function that orchestrates the text processing pipeline.
    Entry point of the program.
    """
    print("\n[PROGRAM START] main()")
    print("=======================")
    
    # Step 1: Initialize test text
    print("\nStep 0: Initialize Data")
    print("=====================")
    test = "This is a very long text that needs to be processed in smaller parts."
    print(f"► Created test string: '{test}'")
    
    # Step 2: Call clean_text_translate
    print("\nStep 1: Calling clean_text_translate()")
    print("► Passing test string to clean_text_translate()")
    cleaned_string = clean_text_translate(test)
    print("► Received result from clean_text_translate()")
    
    # Step 3: Call text_segmentation_5
    print("\nStep 2: Calling text_segmentation_5()")
    print("► Passing cleaned string to text_segmentation_5()")
    result = text_segmentation_5(cleaned_string)
    print("► Received result from text_segmentation_5()")
    
    # Step 4: Display final results
    print("\nFINAL RESULTS")
    print("=============")
    print("Complete processing chain:")
    print(f"1. Original text: '{test}'")
    print(f"2. Cleaned text: '{cleaned_string}'")
    print("3. Segmented text:")
    for i, chunk in enumerate(result, 1):
        print(f"   Chunk {i}: {chunk}")
    
    print("\n[PROGRAM END] main()")

if __name__ == "__main__":
    main()




