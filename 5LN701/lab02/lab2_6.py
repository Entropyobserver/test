import nltk
from nltk import sent_tokenize, word_tokenize
from collections import defaultdict
from math import log
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def step(step_name):
    """
    Decorator to log function entry, exit, and provide additional context about data processing
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            logger.info(f"STEP START: {step_name}")
            logger.info(f"Input arguments: {args}")
            
            # Call the original function
            result = func(*args, **kwargs)
            
            logger.info(f"STEP END: {step_name}")
            
            # Additional logging based on function name
            if step_name == 'get_lines':
                logger.info(f"Total characters read: {len(result)}")
                logger.info(f"First 100 characters: {result[:100]}")
            
            elif step_name == 'get_unigrams':
                logger.info(f"Total unique unigrams: {len(result)}")
                logger.info(f"Top 10 unigrams: {list(sorted(result.items(), key=lambda x: x[1], reverse=True)[:10])}")
            
            elif step_name == 'get_bigrams':
                logger.info(f"Total unique bigrams: {len(result)}")
                logger.info(f"Top 10 bigrams: {list(sorted(result.items(), key=lambda x: x[1], reverse=True)[:10])}")
            
            elif step_name == 'get_bigram_surprisal':
                logger.info(f"Total bigram surprisal entries: {len(result)}")
            
            elif step_name == 'get_perplexity':
                logger.info(f"Perplexity calculation complete")
            
            return result
        return wrapper
    return decorator

@step('get_lines')
def get_lines(path):
    """Read lines from a file with enhanced logging"""
    with open(path, 'r') as f:
        train = f.read()
    logger.info(f"Reading file from path: {path}")
    return train

@step('get_unigrams')
def get_unigrams(sentences):
    """Get unigram frequencies with additional logging"""
    unigram_dict = {}
    for idx, sentence in enumerate(sentences):
        words = word_tokenize(sentence)
        words = [word.lower() for word in words]
        words = ['<s>'] + words + ['<e>']
        
        logger.debug(f"Processing sentence {idx+1}: {sentence[:50]}...")
        
        for word in words:
            if word in unigram_dict:
                unigram_dict[word] += 1
            else:
                unigram_dict[word] = 1
    
    return unigram_dict

@step('get_bigrams')
def get_bigrams(sentences):
    """Get bigram frequencies with additional logging"""
    bigram_dict = {}
    for idx, sentence in enumerate(sentences):
        words = word_tokenize(sentence)
        words = [word.lower() for word in words]
        words = ['<s>'] + words + ['<e>']
        
        logger.debug(f"Processing sentence {idx+1}: {sentence[:50]}...")
        
        for i in range(len(words)-1):
            bi_word = (words[i], words[i+1]) 
            if bi_word in bigram_dict:
                bigram_dict[bi_word] += 1
            else:
                bigram_dict[bi_word] = 1
    
    return bigram_dict

def get_surprisal(p):
    """Calculate surprisal (information content)"""
    s = -log(p, 2)
    logger.debug(f"Calculating surprisal for probability {p}: {s}")
    return s

@step('get_bigram_surprisal')
def get_bigram_surprisal(unigram_dict, bigram_dict):
    """Calculate surprisal for bigrams"""
    bi_sur_dict = {}
    for bi_word in bigram_dict:
        first_word, second_word = bi_word
        unigram_count = unigram_dict.get(first_word, 0)
        bigram_count = bigram_dict.get(bi_word, 0) 
        
        # Add-one smoothing
        unigram_count_smooth = unigram_count + 1
        bigram_count_smooth = bigram_count + 1
        
        # Conditional probability
        cond_p = bigram_count_smooth / unigram_count_smooth
        s = -log(cond_p, 2)
        
        bi_sur_dict[bi_word] = s
        
        # Optional detailed logging
        logger.debug(f"Bigram: {bi_word}, Count: {bigram_count}, Surprisal: {s}")
    
    return bi_sur_dict

@step('get_perplexity')
def get_perplexity(bi_surp, test):
    """Calculate perplexity of the test set"""
    total_surp = 0.0
    word_count = 0
    total_bigrams = len(bi_surp)
    default_surp = -log(1/total_bigrams, 2)

    for sentence in test:
        words = word_tokenize(sentence)
        words = ['<s>'] + words + ['<e>']
        word_count += len(words) - 1
        
        first_bigram = ('<s>', words[1])
        total_surp += bi_surp.get(first_bigram, default_surp)

        for i in range(1, len(words)-1):
            bigram = (words[i], words[i+1])
            total_surp += bi_surp.get(bigram, default_surp)

    avg_surprisal = total_surp / word_count
    perplexity = 2 ** avg_surprisal
    
    logger.info(f"Perplexity calculation details:")
    logger.info(f"Total sentences processed: {len(test)}")
    logger.info(f"Total words processed: {word_count}")
    logger.info(f"Average surprisal: {avg_surprisal}")
    
    return perplexity 

def main():
    # Check if sufficient command-line arguments are provided
    if len(sys.argv) < 3:
        logger.error("Usage: python script.py <train_file_path> <test_file_path>")
        sys.exit(1)

    # Log the input file paths
    train_path = sys.argv[1]
    test_path = sys.argv[2]
    logger.info(f"Train file: {train_path}")
    logger.info(f"Test file: {test_path}")

    # Read train and test files
    train = get_lines(train_path)
    test = get_lines(test_path)

    # Tokenize sentences
    train_sentences = sent_tokenize(train)
    test_sentences = sent_tokenize(test)

    logger.info(f"Train sentences: {len(train_sentences)}")
    logger.info(f"Test sentences: {len(test_sentences)}")

    # Get unigram and bigram frequencies
    unigram_freq = get_unigrams(train_sentences)
    bigram_freq = get_bigrams(train_sentences)

    # Calculate bigram surprisal
    bi_sur_dict = get_bigram_surprisal(unigram_freq, bigram_freq)

    # Calculate perplexity
    perplexity = get_perplexity(bi_sur_dict, test_sentences)
    
    print(f"\nPerplexity on Test Set: {perplexity}")
    logger.info(f"Final Perplexity: {perplexity}")

if __name__ == "__main__":
    main()