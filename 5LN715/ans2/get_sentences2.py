import os
import re
import random
import nltk
from nltk import sent_tokenize, word_tokenize

def read_text_file(file_path):
    """
    Read the entire content of a text file.

    Args:
        file_path (str): Path to the input file.

    Returns:
        str: File contents as a string.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return ""
    except Exception as e:
        print(f"Error reading file: {e}")
        return ""

def preprocess_sentences(sentences, 
                          num_sentences=20, 
                          min_words=15, 
                          max_words=50):
    """
    Select and preprocess random sentences.

    Args:
        sentences (list): List of original sentences
        num_sentences (int): Number of sentences to select
        min_words (int): Minimum number of words in a sentence
        max_words (int): Maximum number of words in a sentence

    Returns:
        list: Processed sentences
    """
    try:
        # Randomly sample sentences
        sampled_sentences = random.sample(
            sentences, 
            min(num_sentences, len(sentences))
        )
        
        processed_sentences = []
        for i, sentence in enumerate(sampled_sentences, 1):
            # Remove punctuation
            sentence = re.sub(r'[^\w\s]', '', sentence)
            
            # Tokenize and filter by length
            words = sentence.split()
            if min_words <= len(words) <= max_words:
                cleaned_sentence = ' '.join(words).lower().strip()
                processed_sentences.append(cleaned_sentence)
                print(f"Selected Sentence {i}: {cleaned_sentence}")
        
        return processed_sentences
    
    except Exception as e:
        print(f"Error processing sentences: {e}")
        return []

def save_sentences_to_files(
    sentences, 
    output_directory='sentence_outputs', 
    file_prefix='sentence'
):
    """
    Save processed sentences to individual text files.

    Args:
        sentences (list): List of sentences to save
        output_directory (str): Directory to save sentence files
        file_prefix (str): Prefix for output files
    """
    try:
        # Create output directory if it doesn't exist
        os.makedirs(output_directory, exist_ok=True)
        
        # Save each sentence to a separate file
        for i, sentence in enumerate(sentences, 1):
            file_path = os.path.join(
                output_directory, 
                f"{file_prefix}_{i}.txt"
            )
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(sentence)
            print(f"Saved: {file_path}")
    
    except Exception as e:
        print(f"Error saving sentences: {e}")

def main():
    # Download NLTK resources if not already available
    nltk.download('punkt', quiet=True)

    # Input file path
    input_file_path = '/home/yaxi4987/5LN715/ans2/wiki.train.raw'
    
    # Output directory configuration
    output_directory = '/home/yaxi4987/5LN715/ans2/outputs'
    
    # Read text from file
    text_content = read_text_file(input_file_path)
    
    if not text_content:
        print("No text to process.")
        return
    
    # Sentence tokenization
    all_sentences = sent_tokenize(text_content)
    
    # Select and preprocess sentences
    processed_sentences = preprocess_sentences(
        all_sentences, 
        num_sentences=20,  # Number of sentences to select
        min_words=15,      # Minimum sentence length
        max_words=50       # Maximum sentence length
    )
    
    # Print selected sentences
    print("\nSelected Sentences:")
    for sentence in processed_sentences:
        print(sentence)
    
    # Save sentences to files
    save_sentences_to_files(
        processed_sentences, 
        output_directory=output_directory,
        file_prefix='sentence'
    )

if __name__ == "__main__":
    main()