#!/bin/bash

train_files=("wiki.train.raw" 
             "wiki.train_18359.raw" 
             "wiki.train_9179.raw" 
             "wiki.train_4589.raw" 
             "wiki.train_2294.raw" 
             "wiki.train_1147.raw")

for train_file in "${train_files[@]}"
do
    python3 lab2.py "$train_file"
done

