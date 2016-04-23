#!/bin/python

import sys

n = int(raw_input().strip())
words = []

for i in range(n):
    words.append(raw_input().strip())

vowels = set(['a','e','i','o','u'])

for orig in words:
    orig = list(orig)
    cons_idcs = []
    for idx in range(len(orig)):
        letter = orig[idx]
        if not letter in vowels:
            cons_idcs.append(idx)

    new_word = []
    cons_idcs_remaining = cons_idcs[:]
    for idx in range(len(orig)):
        if idx in cons_idcs:
            new_word.insert(idx, orig[cons_idcs_remaining.pop(len(cons_idcs_remaining)-1)])
        else:
            new_word.insert(idx, orig[idx])

    print ''.join(new_word)
