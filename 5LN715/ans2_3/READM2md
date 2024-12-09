Phonetic Clarity and Linguistic Surprisal Analysis

This project explores the interaction between phonetic clarity and linguistic surprisal, based on the theory that higher information density in speech is related to clearer articulation Jaeger & Buz (2017). In this work, word duration is used as an approximation for phonetic clarity, and the surprisal is computed using a probabilistic language model.
The project involves a series of steps: training a bigram model, calculating surprisal values for the sentences, extracting phonetic duration based on the MAUS alignment system, and statistical validation to confirm the hypothesized relation.

1. Sources for Data
   
Surprisal Data:
Training Corpus: wiki.train.raw for training a bigram language model.
Test Sentences: 15sentences picked from wiki.test.raw(Every sentence is at least 15 words long and the combination of bigrams that existed in the training corpus)

Phonetic Duration Data:
Audio Files:.wav files of 15 test sentences recorded as read. 
Alignment Output: output from MAUS system, a file ending in.csv format; has word durations.

2. Function Descriptions
   
2.1 In get_duration.py script: 

get_lines(file_path)
Input: Path to a MAUS.csv file.
Output: List of strings (file lines).
Logic: Reads file contents for processing.

get_durations(lines)
Input: List of strings (lines from MAUS output).
Output: Dictionary mapping words to durations (in ms)
Logic: Extracts and sums durations for each word,saved the duration of each word and sentence in Json format

2.2 In get_surprisals.py script

get_lines(file_path)
Input: File path.
Output: List of strings (file lines).

get_unigrams(sentences)
Input: List of sentences (strings).
Output: Dictionary of unigram frequencies.
Logic: Tokenizes sentences and counts unigram occurrences.

get_bigrams(sentences)
Input: List of sentences.
Output: Dictionary of bigram frequencies.
Logic: Tokenizes sentences and counts bigram occurrences.

get_surprisal(p)
Input: Probability p.
Output: Surprisal value.
Logic: Computes -log2(p).

get_bigram_surprisal(unigram_dict, bigram_dict)
Input: Unigram and bigram dictionaries.
Output: Dictionary of bigram surprisal values.
Logic: Applies Laplace smoothing and computes surprisal for each bigram.

get_test_surprisal(sentence, bi_sur_dict, durations)
Input: Sentence (string), bigram surprisal dictionary, word durations.
Output: Average surprisal and word-level surprisal data.
Logic: Computes surprisal values for words in a sentence.

2.3 In get_linear_model.py
Functionality:
Input:combined_sentences.csv combined_words.csv
Fits a linear regression model to investigate the relationship between word duration and surprisal. It prints out statistics and plots. 
 

2.4 In get get_histogram.py
Functionality:
Reads word durations from combined_sentences.csv combined_words.csv.
Generates a histogram with rounded durations on the x-axis and their frequencies on the y-axis.

3. Analysis Workflow

Step 1: Data Preparation

Surprisal Data Preparation:
Train a bigram model using the wiki.train.raw file.
Create unigram and bigram dictionaries.
Calculate bigram probabilities.
Select 15 sentences from the wiki.test.raw dataset.
Calculate surprisal for each word and compute the average surprisal for each sentence.

Speech Data Preparation:
Record the selected sentences and save them as .wav files.
Prepare the recordings for MAUS and run MAUS to get phone-level durations.

Step  2: Data Processing

Extract Word Durations:
Implement get_durations.py to read MAUS .csv files and calculate total word durations.
Convert durations to milliseconds if necessary.
Validate durations using Praat.

Compute Surprisal Values:
Implement get_surprisals.py to compute surprisal values.
Save the average surprisal values for each sentence in data.csv.

Step 3: Analysis

Regression Analysis:
Prepare get_linear_model.py to load data.csv and perform linear regression analysis.
Output regression coefficients and model performance metrics.
Interpret the results to check for a positive correlation between surprisal and duration.

Visualize Data:
Generate a histogram of word durations using seaborn.
Overlay the regression line on a scatterplot of duration vs. surprisal.