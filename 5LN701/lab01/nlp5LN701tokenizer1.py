import re, sys

# Add code here as you did in nlp5LN701tokenizer0.py 
def read_lines(path):
    with open(path,'r') as f:
        lines = f.readlines()
        return lines
"""
def main():
    # And here 
    path = sys.argv[1]
    lines = read_lines(path)
    pattern = "[,;:.!?\"]|"+\
                "\w+" 
    for line in lines:
        tokens = re.findall(pattern, line.strip())
        for token in tokens:
            print(token)

def main():
    # And here 
    path = sys.argv[1]
    lines = read_lines(path)
    pattern = r"\b\d+\.\d+\b|[,;:.!?\"]|\w+"

    for line in lines:
        tokens = re.findall(pattern, line.strip())
        for token in tokens:
            print(token)
    pattern = "\w+(-\w+)*"+\
        "\b\w+'t\b"+\
        "\w+\.(\w+\.)*"+\
        "[%#$]"+\
        "“|”|[.,:;!?‘’]"    

    #pattern = r'\w+(-\w+)*|\w+\.(\w|\.)*|\b\w+\'t\b|[%#$]|[.,:;!?\']'
    #pattern = "\w+\.(\w|\.)*|\b\w+'t\b|\w+\.(\w|\.)*|[%#$]|“|”|[.,:;!?‘’]|\w+(-\w+)*"
    #pattern = r'\w+(?:-\w+)*|\w+(\.\w+)*|\b\w+\'t\b|[%#$][.,:;!?\']'
    #pattern = r"(?:\w+(-\w+)*)|(?:\w+\.(\w|\.)*)|(?:\b\w+'t\b)|(?:[%#$])|(?:“|”|[.,:;!?‘’])"
    #pattern = r"(?:\w+(-\w+)*)|(?:\w+\.(?:\w|\.)*)|(?:\b\w+'t\b)|(?:[%#$])|(?:“|”|[.,:;!?‘’])"
"""

def main():
    path = sys.argv[1]
    lines = read_lines(path)

    
    #pattern = "\w+(?:-\w+)*" 
    #3.1Precision = 0.9207317073170732 (755/820) Recall = 0.8324145534729879 (755/907) F-score = 0.8743485813549507

    #pattern = "\w+(?:-\w+)*|(?:[%#$])"
    #3.2Precision = 0.9216867469879518 (765/830) Recall = 0.8434399117971334 (765/907) F-score = 0.8808290155440416

    #pattern = "\w+(?:-\w+)*|(?:[%#$]|(?:“|”|[.,:;!?‘’]))"
    #3.3Precision = 0.8894736842105263 (845/950) Recall = 0.9316427783902976 (845/907) F-score = 0.9100700053850297

    #!!pattern = "\w+(?:-\w+)*|(?:[%#$]|(?:“|”|[.,:;!?‘’]))|(?:\b\w+'t\b)"
    #3.4Precision = 0.8894736842105263 (845/950) Recall = 0.9316427783902976 (845/907)F-score = 0.9100700053850297

    #pattern = "\w+(?:-\w+)*|(?:[%#$]|(?:“|”|[.,:;!?‘’]))|(?:\b\w+'t\b)|(\w+\.(\w|\.)*)"
    #3.5float division by zero

    #6pattern = "(\w+\.(\w|\.)*)"
    #pattern = "\w+(?:-\w+)*|(?:[%#$]|(?:“|”|[.,:;!?‘’]))|(?:\b\w+'t\b)|(\w+\.(\w|\.)*)"
    #3.7pattern = "(\w+\.(\w|\.)*)|\w+(?:-\w+)*|(?:[%#$]|(?:“|”|[.,:;!?‘’]))|(?:\b\w+'t\b)"

    #pattern = r"\w+(?:-\w+)*|(?:[%#$]|[\"\"\"'']|[.,:;!?])|(?:\b\w+'t\b)|\w+(?:\.\w+)*"
    #3.8Precision = 0.8755144032921811 (851/972) Recall = 0.938257993384785 (851/907) F-score = 0.9058009579563598

    #pattern = "\w+(?:-\w+)*|(?:\b\w+'t\b)|\w+\.(?:\w+\.)*|\w+|[%#$“”.,:;!?‘’]"
    #3.9Precision = 0.8894736842105263 (845/950)Recall = 0.9316427783902976 (845/907)F-score = 0.9100700053850297
    

    ##pattern = "\w+(?:-\w+)*|(?:[%#$]|(?:“|”|[.,:;!?‘’]))|(?:\b\w+'t\b)|(\w+\.(\w|\.)*)"
    #！pattern = r"(?:\d+\.\d+)|(?:\w\.(?:\w\.)+)|(?:\w+(?:-\w+)*)|[%#$“”.,:;!?‘’]"
    #3.10 Precision = 0.9503311258278145 (861/906) Recall = 0.9492833517089305 (861/907) F-score = 0.9498069498069498
    

    #pattern = r"(?:\d+\.\d+)|\w+(?:-\w+)*|(?:[%#$]|(?:“|”|[.,:;!?‘’]))|(?:\b\w+'t\b)"
    #3.11 Precision = 0.9132762312633833 (853/934) Recall = 0.9404630650496141 (853/907) F-score = 0.926670287887018

    #pattern = "(?:\d+\.\d+)|(?:\w\.(?:\w\.)+)|\w+(?:-\w+)*|(?:\b\w+'t\b)|[%#$“”.,:;!?‘’]"
    #3.12 Precision = 0.9503311258278145 (861/906) Recall = 0.9492833517089305 (861/907) F-score = 0.9498069498069498

    #pattern = r"(?:\w+\.(?:\w+\.)+|\d+\.\d+|\w+(?:-\w+)*|\b\w+'t\b|[%#$“”.,:;!?‘’])"
    #3.13 Precision = 0.9545957918050941 (862/903) Recall = 0.9503858875413451 (862/907) F-score = 0.9524861878453038

    #pattern = r"(?:\w+\.(?:\w+\.)+|\d+\.\d+|\w+(?:-\w+)*|\b\w+\'t\b|[%#$“”.,:;!?‘’])"
    #3.14 Precision = 0.9545957918050941 (862/903) Recall = 0.9503858875413451 (862/907) F-score = 0.9524861878453038
    
    #float division by zero 
    for line in lines:
        tokens = re.findall(pattern, line.strip())
        for token in tokens:
            print(token)

if __name__ == "__main__":
    main()
#python nlp5LN701tokenizer1.py '/home/yaxi4987/5LN701/lab01/dev1-raw.txt'
#python nlp5LN701tokenizer1.py '/home/yaxi4987/5LN701/lab01/dev1-raw.txt' > '/home/yaxi4987/5LN701/lab01/dev1-tok.txt'
#vimdiff dev1-gold.txt dev1-tok.txt
#python3 score-tokens.py dev1-gold.txt dev1-tok.txt

#python nlp5LN701tokenizer1.py '/home/yaxi4987/5LN701/lab01/dev1-raw.txt' > '/home/yaxi4987/5LN701/lab01/dev2-tok.txt'
#vimdiff dev1-gold.txt dev2-tok.txt
#python3 score-tokens.py dev1-gold.txt dev2-tok.txt

#python nlp5LN701tokenizer1.py '/home/yaxi4987/5LN701/lab01/dev1-raw.txt'
#python nlp5LN701tokenizer1.py '/home/yaxi4987/5LN701/lab01/dev1-raw.txt' > '/home/yaxi4987/5LN701/lab01/dev3-tok.txt'
#vimdiff dev1-gold.txt dev3-tok.txt
#python3 score-tokens.py dev1-gold.txt dev3-tok.txt