#!/usr/bin/bash

# name of the current tagger experiment
EXP=t3

# train tagger with -t 3 (four-gram model)
hunpos-train $EXP\_tagger -t 3 < ewt-train-wt.txt

# run tagger
hunpos-tag $EXP\_tagger < ewt-dev-w.txt > ewt-dev-$EXP.txt

# score tagger
python3 score.py tag ewt-dev-wt.txt ewt-dev-$EXP.txt > result_$EXP.txt
