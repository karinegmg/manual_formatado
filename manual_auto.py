import csv
import math
import os
import random
import re
import sys

#file = open('resultado_manual_formatado.csv', 'r')
file = open('fm_ck.csv', 'r')
#output = open('manual_formated_fm_ck.csv')

newFormat = ''

postag_FM = 3
poschange_FM = 2
poschange_CK = 4
postag_CK = 5
tags = []
changes = []

def fm(changes, tags):
    return "todo"


def ck(changes, tags):
    return "TODO"

def fm_ck(changes, tags):
    #newFormat = 
    for c in changes:
        for t in tags:
            print("changes: {} and tags: {}".format(c, t))


for line in file:
    #print(line)
    colummns = line.split(',')
    changes.append(colummns[poschange_FM].split(';'))
    tags.append(colummns[postag_FM].split(';'))

file.close()

fm_ck(changes, tags)


