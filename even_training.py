#!/bin/python

import sys


n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))

no_days_training = sum(a)
even_no_days = 'Yes' if no_days_training % 2 == 0 else 'No'

print str(even_no_days) + ' ' + str(no_days_training)

