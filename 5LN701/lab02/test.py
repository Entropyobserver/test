def get_perplexity(bi_surp, test_set):
    """
    Calculate perplexity of a test set using bigram surprisal values.
    
    Args:
        bi_surp (dict): Dictionary with bigrams as keys and surprisal values as values
        test_set (list): List of sentences to evaluate
        
    Returns:
        float: Calculated perplexity value
    """
    total_surp = 0.0
    word_count = 0
    
    for sentence in test_set:
        # Tokenize sentence and add start/end tokens
        words = sentence.split()
        words = ['<s>'] + words + ['<e>']
        
        # Count words (excluding start token but including end token)
        word_count += len(words) - 1
        
        # Process first bigram (start token with first word)
        first_bigram = ('<s>', words[1])
        if first_bigram in bi_surp:
            total_surp += bi_surp[first_bigram]
        
        # Process middle bigrams
        for i in range(1, len(words)-1):
            bigram = (words[i], words[i+1])
            if bigram in bi_surp:
                total_surp += bi_surp[bigram]
    
    # Calculate perplexity using equation 4 (2 raised to average surprisal)
    avg_surprisal = total_surp / word_count
    perplexity = 2 ** avg_surprisal
    
    return perplexity

# Example usage:
# Assuming you have your bigram surprisal dictionary and test sentences loaded:
# with open('wiki.test.raw', 'r', encoding='utf-8') as f:
#     test_sentences = f.readlines()
# perplexity = get_perplexity(bi_surp_dict, test_sentences)