"""
    In computational linguistics, n-gram models were considered
    state-of-the-art for some time. Although these models are not used
    very much anymore (except as baselines), they are definitely a great
    starting point when learning about language models, which in turn
    are central in the field and which you will learn more about later in
    this Master's program.

    An n-gram is a sequence of items (most often words but sometimes e.g.,
    characters).

    The n in n-gram refers to a number > 0. If n=1, we are
    dealing with unigrams, if n=2, we have bigrams, and so on.
    The unigrams in example (1) are simply the words.

(1) I love cheese but only sometimes

    Here are the unigrams:

"I", "love", "cheese", "but", "only", "sometimes"

    This might seem meaningless, but later in the Master's program,
    it will be clear that it isn't.

    The bigrams in (2) are the following:
    
"I love", "love cheese", "cheese but", "but only", and "only sometimes"

    The higher the n in n-gram, the fewer the n-gram tokens. What?
    What does this mean? Well, let's take a step back and first learn
    another distinction:

    The difference between types and tokens.
    The types are the unique word forms, and the tokens are the instances
    of those types. (It can be a little bit more complex than that, but
    this definition is OK for now.)

    For example, consider the sentences in (2).

(2) I love the sun. I love the sun and the sun is a star. I love a star.

    Considering the word level (e.g., not characters), we can see that
    the sentence contains 18 words. If we count the punctiation mark as a
    token, we have 21 tokens. But how many types are there? Let's list them:

I
love
the
sun
.
and
that
is
a
star

    There are 10 types! Why? Well, because some tokens (e.g., "I", "love", ".")
    appear more than once! Here is a dictionary that shows the types in (2)
    along with their frequencies:

{'I': 3, 'love': 3, 'the': 3, 'sun': 3, '.': 3, 'and': 1, 'is': 1, 'a': 2, 'star': 2}

    Imagine now that you had a huge collection of sentences (called a corpus).
    The difference between the number of types and the number of tokens would
    of course be much, much greater.

    Write a function get_bigrams() that takes a list of words (forming a
    sentence) as input and that returns i dictionary where the keys are
    bigrams and the values the frequency of each bigram. Bigrams should
    be in lower case.

    TIP: When populating the dictionaries with the bigrams and frequencies,
    use this:

for i in range(len()):

The trick is to understand what else is needed ;)


"""
def get_bigrams_1(text):
    text = text.lower()
    text = text.replace(".","")
    text = text.split()
    bi_dict = {}
    for i in range(len(text)-1):
        bigram = (text[i],text[i+1])
        bi_str = "".join(bigram)
        if bi_str in bi_dict:
            bi_dict[bi_str] += 1
        else:
            bi_dict[bi_str] = 1
    return bi_dict
print("test for funcation 1 is  running")
lst1 = " I love the sun. I love the sun and the sun is a star. I love a star."
print(get_bigrams_1(lst1))

from collections import defaultdict
import string
def get_bigrams_2(text):
    text = text.lower()
    text = text.translate(str.maketrans('','',string.punctuation))
    text = text.split()
    bigram_dict = defaultdict(list)
    for i in range(len(text) - 1):
        bigram = (text[i],text[i+1])
        bistr = "".join(bigram)
        bigram_dict[bigram].append(i)
    return(bigram_dict)
print("test for function 2 is running")
lst1 = " I love the sun. I love the sun and the sun is a star. I love a star."
print(get_bigrams_2(lst1))


from collections import defaultdict
import string
def get_bigrams_3(text):
    text = text.lower()
    text = text.translate(str.maketrans('','',string.punctuation))
    text = text.split()
    bigram_dict = defaultdict(list)
    for i in range(len(text) - 1):
        bigram = (text[i],text[i+1])
        bistr = "".join(bigram)
        if bistr in bigram_dict:
            bigram_dict[bistr] += 1
        else:
            bigram_dict[bistr] = 1
    return(bigram_dict)
print("test for function 3 is running")
lst1 = " I love the sun. I love the sun and the sun is a star. I love a star."
print(get_bigrams_3(lst1))





