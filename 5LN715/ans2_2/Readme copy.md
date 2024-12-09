1. Understand the Concept
Phonetic Clarity: Measured via word durations (in milliseconds). Longer durations indicate clearer articulation.
Surprisal: Quantified using a bigram model as 
𝑆
=
−
log
⁡
2
(
𝑃
(
𝑤
)
)
S=−log 
2
​
 (P(w)), where 
𝑃
(
𝑤
)
P(w) is the conditional probability of a word.
2. Prepare the Surprisal Data
Build a Bigram Model: Use wiki.train.raw to train a bigram model. Reuse code from Lab 2 if available.
Test Data: Select or construct 10+ sentences from wiki.test.raw (minimum 15 words each) where all bigrams exist in the dictionary.
Calculate Surprisal: For each sentence, compute surprisal values for all words and save the average surprisal per sentence.
3. Collect Speech Data
Record yourself reading the sentences from the test data.
Use a consistent format and naming convention (sentence1.wav, sentence2.wav, etc.).
Process these recordings through MAUS to get word-level durations.
4. Write the Scripts
get_durations.py:
Function get_lines() to read files.
Function get_durations() to parse MAUS outputs and extract word durations.
get_surprisals.py:
Functions to calculate unigrams, bigrams, probabilities, surprisal, and average surprisal for sentences.
get_linear_model.py:
Implement linear regression to model duration as a function of surprisal.
get_histogram.py:
Generate a histogram of word/sentence durations.
5. Data Validation
Unit Check: Ensure MAUS durations are in milliseconds (convert if needed).
Sanity Check: Cross-check durations with Praat or similar tools.
6. Perform Analysis
Compute the regression model using the data.csv file containing duration and surprisal columns.
Evaluate the model with metrics like p-value, 
𝑅
2
R 
2
 , intercept, and coefficient.
7. Visualizations
Create a histogram of durations.
Generate a scatter plot of durations vs. surprisal with a regression line.


1. Train a Bigram Model and Calculate Surprisal

1.1 Obtain Training Data and Train the Model
Input:
File: wiki.train.raw (a text file containing a large number of sentences)
Output:
Unigram Frequency Dictionary: {word: frequency}, the number of occurrences of each word.
Bigram Frequency Dictionary: {(word1, word2): frequency}, the number of occurrences of each bigram.

1.2 Calculate Conditional Probabilities for the Bigram Model
Input:
Unigram Frequency Dictionary
Bigram Frequency Dictionary
Output:
Bigram Probability Dictionary: {(word1, word2): P(word2 | word1)}, the conditional probability of each bigram.

1.3 Calculate Surprisal
Input:
Bigram Probability Dictionary
Output:
Bigram Surprisal Dictionary: {(word1, word2): surprisal}, the surprisal of each bigram.

1. Extract Test Sentences and Calculate Sentence Surprisal
2.1 Select or Construct Test Sentences
Input:
File: wiki.test.raw (a text file containing test sentences)
Bigram Model
Output:
Test Sentence Files: sentence1.txt, sentence2.txt, ... (each file contains a sentence with at least 15 words, and all bigram combinations can be found in the bigram model).
combine all 15 sentences to a .txt as combine_sentences.txt

2.2 Calculate Average Surprisal of Sentences
Input:
Test Sentence Files
Bigram Surprisal Dictionary
Output:
Sentence Surprisal List: [average_surprisal1, average_surprisal2, ...], the average surprisal of each sentence.

3. Record Speech and Calculate Speech Duration
3.1 Record Speech
Input:
Test Sentence Files: sentence1.txt, sentence2.txt, ...
Output:
Audio Files: sentence1.wav, sentence2.wav, ... (each file corresponds to the speech of a sentence).

3.2 Align Speech Using MAUS
Input:
Audio Files: sentence1.wav, sentence2.wav, ...
Test Sentence Files: sentence1.txt, sentence2.txt, ...
Output:
Alignment Output Files (CSV format): sentence1.csv, sentence2.csv, ... (containing the start and end times and duration of each word).

3.3 Parse Duration
Input:
Alignment Output Files (CSV format)
Sampling Rate Information (e.g., 24000 Hz)
Output:
Word Duration Dictionary: {word: duration_in_ms}, the duration of each word (in milliseconds).


4. Data Merging
4.1 Merge Speech Duration and Surprisal
Input:
Word Duration Dictionary
Sentence Surprisal List
Output:
Data File: data.csv, each row contains the duration and surprisal of a sentence:
duration,surprisal
4.52,18
6.52,6
5.52,14

5. Data Analysis
5.1 Generate Duration Histogram
Input:
Data File: data.csv
Output:
Duration Histogram: showing the distribution of durations (x-axis is duration, y-axis is frequency).

5.2 Linear Regression Analysis
Input:
Data File: data.csv
Output:
Regression Analysis Results:
Regression Coefficient (β1): the effect size of surprisal on duration.
Intercept (β0): the starting point of the linear model.
R² Value: the proportion of variance explained by the model.

p-value: the statistical significance of the relationship.

Scatter Plot and Regression Line Plot: showing the relationship between surprisal and duration.

6. Output Final Files
Report and Code

Input:

Data File: data.csv

Analysis Results

Output:

Report PDF File: containing the experiment background, methods, results, discussion, and conclusion.

Complete Code and README File.

Compressed