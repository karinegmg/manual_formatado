import csv
import math
import os
import random
import re
import sys

#file = open('resultado_manual_formatado.csv', 'r')
file = open('fm.csv', 'r')
#output = open('manual_formated_fm_ck.csv')


poscommit = 0
posauthor = 1
poschange_FM = 2
postag_FM = 3
poschange_CK = 4
postag_CK = 5
columnChanges = []

def fm(changes, tags):
    return "todo"


def ck(columns):
    poscommit = 0
    posauthor = 1
    poschange_FM = 2
    postag_FM = 3
    poschange_CK = 4
    postag_CK = 5
    tags = []
    changes = []
    changedLine = []
    ck_line = ""
    
    for line in columnChanges:
        #print(line)
        changedLine = line.split(",")
        commit = changedLine[poscommit]
        author = changedLine[posauthor]
        tags.append(changedLine[postag_FM])
        changes.append(changedLine[poschange_FM])

        i = 0 
        while(i < len(tags)):
            tagsAndChange = "["
            changeLine = changes[i].split(";")
            tagLine = tags[i].split(";")
            j = 0
            diff = 0

            if(len(changeLine) > len(tagLine)):
                while(j < len(tagLine)):
                    tagsAndChange = tagsAndChange + '(\'{}\' | \'{}\')'.format(changeLine[j], tagLine[j])
                    #print(tagsAndChange)
                    j = j + 1
                    diff = j
                while(diff < len(changeLine)):
                    diff = diff + 1
                    tagsAndChange = tagsAndChange + '(\'{}\' | \'{}\')'.format(changeLine[diff], tagLine[j])
                    #diff = diff + 1
            
            elif(len(tagLine) > len(changeLine)):
                while(j < len(changeLine)):
                    tagsAndChange = tagsAndChange + '(\'{}\' | \'{}\')'.format(changeLine[j], tagLine[j])
                    #print(tagsAndChange)
                    j = j + 1
                    diff = j
                while(diff < len(tagLine)):
                    diff = diff + 1
                    tagsAndChange = tagsAndChange + '(\'{}\' | \'{}\')'.format(changeLine[j], tagLine[diff])
                    
            
            elif(len(tagLine) == len(changeLine)):
                while(j < len(changeLine)):
                    tagsAndChange = tagsAndChange + '(\'{}\' | \'{}\')'.format(changeLine[j], tagLine[j])
                    #print(tagsAndChange)
                    j = j + 1
                    
            tagsAndChange = tagsAndChange + "]"
            i = i + 1

            #print(tagsAndChange)
            output_line = "{},{},{}".format(commit, author, tagsAndChange)
            print(output_line)

    return "TODO"

def fm_ck(changes):
    return "to do"

for line in file:
    #print(line)
    columnChanges.append(line)
    #columnChanges.append(colummns[poschange_FM].split(';'))
    #tags.append(colummns[postag_FM].split(';'))

file.close()

fm_ck(columnChanges)
ck(columnChanges)
