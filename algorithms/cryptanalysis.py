'''
File Name: cryptanalysis.py
Create: 12/17/2024
Description: According to the book *Cryptography: Theory and Practice*, 
             some important value for cryptanalysis are assembled in fixed value in python's type
'''

import re

# Probabilities of occurrence of the 26 letters
LETTER_PROB = {
    'A' : 0.082, 'B' : 0.015, 'C' : 0.028, 'D' : 0.043,
    'E' : 0.127, 'F' : 0.022, 'G' : 0.020, 'H' : 0.061,
    'I' : 0.070, 'J' : 0.002, 'K' : 0.008, 'L' : 0.040,
    'M' : 0.024, 'N' : 0.067, 'O' : 0.075, 'P' : 0.019,
    'Q' : 0.001, 'R' : 0.060, 'S' : 0.063, 'T' : 0.091,
    'U' : 0.028, 'V' : 0.010, 'W' : 0.023, 'X' : 0.001,
    'Y' : 0.020, 'Z' : 0.001
}

# diagrams: 30 most common sequences of two consecutive letters
DIGRAMS = ('TH', 'HE', 'IN', 'ER', 'AN', 'RE', 'ED', 'ON', 'ES', 'ST', 
           'EN', 'AT', 'TO', 'NT', 'HA', 'ND', 'OU', 'EA', 'NG', 'AS', 
           'OR', 'TI', 'IS', 'ET', 'IT', 'AR', 'TE', 'SE', 'HI', 'OF')

# trigrams: 12 most common sequences of three consecutive letters
TRIGRAMS = ('THE', 'ING', 'AND', 'HER', 'ERE', 'ENT', 
            'THA', 'NTH', 'WAS', 'ETH', 'FOR', 'DTH')


# recieve a string, return a dict that indicates frequency of occurrence of each letter 
def getLetterOccDict(plainText):
    # check for empty string
    if len(plainText) == 0:
        return dict()
    
    letterOccDict = {}

    # check each letter in the string
    for eachLetter in plainText:
        eachLetter = eachLetter.upper()
        # not existed in dict, create
        if letterOccDict.get(eachLetter) == None:
            letterOccDict[eachLetter] = 0
        # plus the count
        letterOccDict[eachLetter] += 1

    # rank by frequency
    rankedLetterOcc = sorted(letterOccDict.items(), key=lambda x:x[1], reverse = True)

    return letterOccDict

# return popular digrams related to the given letter, including x- and -x
def getLetterDigrams(targetLetter):
    return [eachDigram for eachDigram in DIGRAMS if targetLetter.upper() in eachDigram]

# return popular trigrams related to the given letter, including x--, -x- and --x
def getLetterTrigrams(targetLetter):
    return [eachTrigram for eachTrigram in TRIGRAMS if targetLetter.upper() in eachTrigram]

# find and compute digrams of a single letter in a piece of text
# input: a target letter and a piece of text
# output: all digrams related to the target letter, inlcuding -x and x-
def getLetterDigramsOccInTextDict(targetLetter, plainText):
    # target dict
    digramsOccDict = dict()

    # the analyse is not case sensitive, set to upper case for compaire
    plainText = plainText.upper()
    targetLetter = targetLetter.upper()
    
    # pattern for -x and x-
    pattern_X = fr"[a-zA-Z][{targetLetter}]"
    patternX_ = fr"[{targetLetter}][a-zA-Z]" # {targetLetter.upper()}
    # two matching results in the plain text
    matches_X = re.findall(pattern_X, plainText)# flags = re.IGNORECASE
    matchesX_ = re.findall(patternX_, plainText)

    # combine two answers and calculate occurrence
    for eachDigram in matches_X + matchesX_:
        # count times for each isolate digram
        if digramsOccDict.get(eachDigram) == None:
            digramsOccDict[eachDigram] = 0
        digramsOccDict[eachDigram] += 1

    return digramsOccDict


# find and compute digrams of a single letter in a piece of text
# input: a target letter and a piece of text
# output: all digrams related to the target letter, inlcuding -x and x-
def getLetterTrigramsOccInTextDict(targetLetter, plainText):
    # target dict
    trigramsOccDict = dict()

    # the analyse is not case sensitive, set to upper case for compaire
    plainText = plainText.upper()
    targetLetter = targetLetter.upper()
    
    # pattern for -x and x-
    patternX__ = fr"[{targetLetter}][a-zA-Z][a-zA-Z]"
    pattern_X_ = fr"[a-zA-Z][{targetLetter}][a-zA-Z]"
    pattern__X = fr"[a-zA-Z][a-zA-Z][{targetLetter}]" # {targetLetter.upper()}
    # two matching results in the plain text
    matchesX__ = re.findall(patternX__, plainText)# flags = re.IGNORECASE
    matches_X_ = re.findall(pattern_X_, plainText)
    matches__X = re.findall(pattern__X, plainText)

    # combine two answers and calculate occurrence
    for eachTrigram in matchesX__ + matches_X_ + matches__X:
        # count times for each isolate digram
        if trigramsOccDict.get(eachTrigram) == None:
            trigramsOccDict[eachTrigram] = 0
        trigramsOccDict[eachTrigram] += 1

    return trigramsOccDict