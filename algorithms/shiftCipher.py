'''
File Name: shiftCipher.py
Create: 12/17/2024
Description: Encryption, decryption and cryptanalysis function of shift cipher
'''
# import cryptanalysis util file
from . import cryptanalysis as ca

# shift cipher: encrypt by key
def shiftEnc(plainText, key):
    cipherText = ""
    for eachChar in plainText:
        if eachChar.isupper():
            # minus 65 (charactor A), calculate value and plus 65
            cipherText += chr((ord(eachChar) - ca.ASCII_UPPER_A + key) % 26 + ca.ASCII_UPPER_A)
        elif eachChar.islower():
            # minus 97 (charactor a), calculate value and plus 97
            cipherText += chr((ord(eachChar) - ca.ASCII_LOWER_A + key) % 26 + ca.ASCII_LOWER_A)
        else:
            # not alpha, copy the origin
            cipherText += eachChar
    return cipherText

# shift cipher: decrypt by key
def shiftDec(cipherText, key):
    plainText = ""
    for eachChar in cipherText:
        if eachChar.isupper():
            # minus 65 (charactor A), calculate value and plus 65
            plainText += chr((ord(eachChar) - ca.ASCII_UPPER_A - key) % 26 + ca.ASCII_UPPER_A)
        elif eachChar.islower():
            # minus 97 (charactor a), calculate value and plus 97
            plainText += chr((ord(eachChar) - ca.ASCII_LOWER_A - key) % 26 + ca.ASCII_LOWER_A)
        else:
            # not alpha, copy the origin
            plainText += eachChar
    return plainText


# 取所有字母出现次数，算差值得明文，匹配digram trigram
def shiftAnalysis(cipherText):
    # letterOcc = ca.getLetterOccDict(cipherText)
    # rankedLetterOccList = sorted(letterOcc.items(), key = lambda item:item[1], reverse = True)
    
    # get occourance list of letters in ciphertext, grouping as occourance times
    letterOccList = ca.getGroupedRankedOccList(cipherText)

    # a dict that record keys and matching digrams and trigrams
    keyMatching = {}
    plainTexts = []

    if len(letterOccList) < 3:
        return []

    # get first 3 occourence letter group, try 'E'
    mostOcc3 = letterOccList[0][1] + letterOccList[1][1]+letterOccList[2][1]
    for eachLetter in mostOcc3:
        key = (ord(eachLetter) - ord('E'))
        # get a attempted plain text
        tempPlain = shiftDec(cipherText, key)
        digramsCount = ca.getDigramsInTextCount(tempPlain)
        trigramsCount = ca.getTrigramsInTextCount(tempPlain)
        # store the key and matching counts
        keyMatching[key] = digramsCount + trigramsCount

    maxMatching = max(keyMatching.values())
    # there may have multiple keys which have same digrams and trigrams matching
    maxMatchingDicts = {k: v for k, v in keyMatching.items() if v == maxMatching}
    for eachKey in maxMatchingDicts.keys():
        plainTexts.append(shiftDec(cipherText, eachKey))

    return plainTexts
