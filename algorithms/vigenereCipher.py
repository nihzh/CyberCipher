'''
File Name: vigenereCipher.py
Create: 08/02/2025
Description: Encryption, decryption and cryptanalysis function of vigenere cipher
'''
# import cryptanalysis util file
from . import cryptanalysis as ca
# string for traversal letters a-z
import string
# cartesian product calculation
from itertools import product

def vigEnc(plainText, keyword):
    cipherText = ""
    keyNumEq = ca.getNumeralEqus(keyword)

    # the length of keyword, cycling encrypt
    m = len(keyword)
    # point the key
    keyPtr = 0

    for eachChar in plainText:
        # distinguish upper and lower letter
        if eachChar.isupper():
            # minus 65 (charactor A), calculate value and plus 65
            cipherText += chr((ord(eachChar) - ca.ASCII_UPPER_A + keyNumEq[keyPtr]) % 26 + ca.ASCII_UPPER_A)
            keyPtr = (keyPtr + 1) % m
        elif eachChar.islower():
            # minus 97 (charactor a), calculate value and plus 97
            cipherText += chr((ord(eachChar) - ca.ASCII_LOWER_A + keyNumEq[keyPtr]) % 26 + ca.ASCII_LOWER_A)
            keyPtr = (keyPtr + 1) % m
        else:
            # not alpha, copy the origin
            cipherText += eachChar

    return cipherText

def vigDec(cipherText, keyword):
    plainText = ""
    keyNum = ca.getNumeralEqus(keyword)

    # the length of keyword, cycling encrypt
    m = len(keyword)

    # point the key
    keyPtr = 0
    for eachChar in cipherText:
        # distinguish upper and lower letter
        if eachChar.isupper():
            # minus 65 (charactor A), calculate value and plus 65
            plainText += chr((ord(eachChar) - ca.ASCII_UPPER_A - keyNum[keyPtr]) % 26 + ca.ASCII_UPPER_A)
            keyPtr = (keyPtr + 1) % m
        elif eachChar.islower():
            # minus 97 (charactor a), calculate value and plus 97
            plainText += chr((ord(eachChar) - ca.ASCII_LOWER_A - keyNum[keyPtr]) % 26 + ca.ASCII_LOWER_A)
            keyPtr = (keyPtr + 1) % m
        else:
            # not alpha, copy the origin
            plainText += eachChar

    return plainText


# given a piece of texts, calculate 'Index of Coincidence'
# which sum([fi(fi - 1)] / [n(n - 1)])
def icCalculate(texts):
    # ic value
    ic = 0
    # set lowercase for counting
    lowerText = texts.lower()
    
    # n(n - 1)
    textLength = len(texts)
    den = textLength * (textLength - 1) / 26

    # for each alpha in alphabet (a-z)
    for eachAlpha in string.ascii_lowercase:
        # count in lower case text
        alphaCount = lowerText.count(eachAlpha)
        # fi(fi - 1)
        num = alphaCount * (alphaCount - 1)
        ic += num / den

    return ic

# recive a string, divide to k groups: 0, k, 2k; 1, k+1, 2k+1; ...
def matrixStrCut(text, k):
    # create k empty string in a list
    strGroups = ['' for _ in range(k)]

    # process by each char
    for i, char in enumerate(text):
        # filter the non-alpha chars
        if not char.isalpha():
            continue
        # calculate which group, insert
        index = i % k
        strGroups[index] += char

    return strGroups

# calculate correlation between the decrypted column letter frequencies and the relative letter frequencies
def corrCalculate(pureCipherText, decKey):
    # get decrypt text
    plainText = ""
    for eachChar in pureCipherText:
        plainText += chr((ord(eachChar) - ca.ASCII_LOWER_A - decKey) % 26 + ca.ASCII_LOWER_A)
    
    # calculate correlation of decrypted text
    corr = 0
    for eachAlpha in string.ascii_lowercase:
        corr += plainText.count(eachAlpha) * ca.LETTER_PROB[eachAlpha.upper()]
    # print(plainText, corr)
    return corr / len(plainText)


# 轮询k， 分k（质数）组，每组算delta ic，ic在k的倍数1.73最近
def vigAnalysis(cipherText):
    # first, determine the keyword length
    # filter the text to pure letter, switch to lower
    pureLowerText = "".join(filter(str.isalpha, cipherText)).lower()
    # calculate index of coincidence for each possible key length
    keyICs = {}

    # keys with same factor will have similar result, so prime only
    for tmpKeyLen in [2, 3, 5, 7, 11, 13, 17]:
        # cut, calculate each ic, and get avg value
        cuttedStrList = matrixStrCut(pureLowerText, tmpKeyLen)
        cuttedICList = list(map(icCalculate, cuttedStrList))
        avgIC = sum(cuttedICList) / len(cuttedICList)
        keyICs[tmpKeyLen] = avgIC

    # get key length, which ic value nearest to 1.73 (index of coincidence)
    keyLen = min(keyICs, key = lambda x: abs(keyICs[x] - ca.INDEX_OF_COINCIDENCE))

    # second, find the key string, # pi*(fi+g) / n'
    keyStrGuess = []
    # the n'
    cuttedTextLen = len(pureLowerText) / keyLen
    # for each sliced text
    cuttedStrList = matrixStrCut(pureLowerText, keyLen)
    for eachCut in cuttedStrList:
        # in each cut, make few possible guess
        cuttedKeyGuess = []
        # try each of 26 decryption for cutted substring
        for eachAlpha in range(0, 26):
            # correlations between decrypted column letter frequencies and the relative letter frequencies
            corr = corrCalculate(eachCut, eachAlpha)
            # corr value tend to regular English, the key is possible
            if abs(corr - ca.IDEAL_PROB_DISTRIBUTION) <= 0.009:
                cuttedKeyGuess += chr(eachAlpha + ca.ASCII_LOWER_A)
        # record the key that nearest to 0.065 (ideal probability distribution)
        # keyStr += min(corrs, key = lambda x: abs(corrs[x] - ca.IDEAL_PROB_DISTRIBUTION))
        keyStrGuess.append(cuttedKeyGuess)

    # third, plain text recovery
    # make certesian product for each cutted key guess, as possible keys
    certesianProduct = list(product(*keyStrGuess))
    possibleKeys = ["".join(pair) for pair in certesianProduct]

    # for each possible keys, take plain text and check if it is rational English
    possiblePlainText = []
    for eachKey in possibleKeys:
        plainText = vigDec(cipherText, eachKey)
        # find correlation value (no shift)
        corr = corrCalculate(plainText, 0)
        # keep the answer if it similar to regular English
        if abs(corr - ca.IDEAL_PROB_DISTRIBUTION) <= 0.009:
            possiblePlainText.append(plainText)
    
    return possiblePlainText