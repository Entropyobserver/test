import re, sys
try:
    from f_score import f_score
except ModuleNotFoundError:
    pass

def eq_tokens(gt, st):
    if gt.strip() in ["``", "''"] and st.strip() == '"':
        return True
    else:
        return gt == st

if len(sys.argv) != 3:
    print("usage: python score-tokens.py goldfile testfile")
    exit()

gfile = open(sys.argv[1])
sfile = open(sys.argv[2])

lcs = {}

gtokens = gfile.readlines()
stokens = sfile.readlines()


for i in range(0, len(gtokens)+1):
    lcs[(i, 0)] = 0
for j in range(0, len(stokens)+1):
    lcs[(0, j)] = 0
for i in range(1, len(gtokens)+1):
    for j in range(1, len(stokens)+1):
        if eq_tokens(gtokens[i-1], stokens[j-1]):
            lcs[(i, j)] = lcs[(i-1, j-1)] + 1
        else:
            if lcs[(i-1, j)] >= lcs[(i, j-1)]:
                lcs[(i, j)] = lcs[(i-1, j)]
            else:
                lcs[(i, j)] = lcs[(i, j-1)]    

tp = lcs[(len(gtokens),len(stokens))]
g = len(gtokens)
s = len(stokens)

def f_score(Precision,recall):
    f_score = 2 * (Precision * recall) / (Precision + recall)
    return f_score
    
print()
print("Precision = " + str(float(tp)/float(s)) + " (" + str(tp) + "/" + str(s) + ")")
print("Recall = " + str(float(tp)/float(g)) + " (" + str(tp) + "/" + str(g) + ")")
prec = float(tp)/float(s)
reca = float(tp)/float(g)
try:
    print("F-score = " + str(f_score(prec,reca)))
except NameError:
    print()
    print("Once you have written code for a function f_score in a file called f_score.py, you will get the f-score as well.")

print()
