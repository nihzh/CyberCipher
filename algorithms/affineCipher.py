'''
File Name: affineCipher.py
Create: 13/1/2024
Description: Encryption, decryption and cryptanalysis function of affine cipher
'''
# import cryptanalysis util file
import cryptanalysis as ca

MULTIPLICATIVE_INVERSE = {
    1:1, 3:9, 5:21, 7:15, 9:3, 11:19,
    15:7, 17:23, 19:11, 21:5, 23:17, 25:25}

# encryption, x * a + b
def affineEnc(plainText, keya, keyb):
    cipherText = ""
    for eachChar in plainText:
        # distinguish upper and lower letter
        if eachChar.isupper():
            # minus 65 (charactor A), calculate value and plus 65
            cipherText += chr(((ord(eachChar) + ca.ASCII_UPPER_A) * keya + keyb) % 26 + ca.ASCII_UPPER_A)
        elif eachChar.islower():
            # minus 97 (charactor a), calculate value and plus 97
            cipherText += chr(((ord(eachChar) - ca.ASCII_LOWER_A) * keya + keyb) % 26 + ca.ASCII_LOWER_A)
        else:
            # not alpha, copy the origin
            cipherText += eachChar
    return cipherText

# decryption, x - b * (inv)a
def affineDec(cipherText, keya, keyb):
    plainText = ""
    for eachChar in cipherText:
        if eachChar.isupper():
            # minus 65 (ascii A), calculate value and plus 65
            plainText += chr((ord(eachChar) - ca.ASCII_UPPER_A - keyb) * MULTIPLICATIVE_INVERSE[keya] % 26 + ca.ASCII_UPPER_A)
        elif eachChar.islower():
            # minus 97 (ascii a), calculate value and plus 97
            plainText += chr((ord(eachChar) - ca.ASCII_LOWER_A - keyb) * MULTIPLICATIVE_INVERSE[keya] % 26 + ca.ASCII_LOWER_A)
        else:
            # not alpha, copy the origin
            plainText += eachChar
    return plainText

# # calculate Extended Euclidean Algorithm `ax + by = gcd(a, b)`
# def extended_gcd(a, b):
#     if b == 0:
#         return a, 1, 0
#     gcd, x1, y1 = extended_gcd(b, a % b)
#     x = y1
#     y = x1 - (a // b) * y1
#     return gcd, x, y

# # calculate multiplicative reverse of a under mod m, return None if not existss
# def mod_inverse(a, m):
#     gcd, x, _ = extended_gcd(a, m)
#     if gcd != 1:
#         return None  # No multiple inverse
#     else:
#         return x % m  # make sure positive

# one assumption, two letters for 'E' and 'T', make equation and calculate results
def keyCalculate(letterA, letterB):
    # assume one letter as 'E', next one as 'T'
    numToE = ord(letterA) - ca.ASCII_UPPER_A
    numToT = ord(letterB) - ca.ASCII_UPPER_A
    # get the equation of solutions (simplified)
    eLeft = ((ord('T') - ca.ASCII_UPPER_A) - (ord('E') - ca.ASCII_UPPER_A)) % 26
    eRight = (numToT - numToE) % 26
    # calculate solution
    if eLeft not in MULTIPLICATIVE_INVERSE:
        return -1, -1
    keyA = (eRight * MULTIPLICATIVE_INVERSE[eLeft]) % 26
    keyB = (numToE - (ord('E') - 65) * keyA) % 26
    if keyA not in MULTIPLICATIVE_INVERSE:
        return -1, -1
    return keyA, keyB


def affineAnalysis(cipherText):
    # get letter occourance in cipher text
    # letterOcc = ca.getLetterOccDict(cipherText)
    letterOccList = ca.getGroupedRankedOccList(cipherText)
    # record digrams and trigrams matching
    matchingDict = {}
    plainTexts = []

    # take 3 most occourance and all permutations of 3 letters
    # for a, b in [(0, 1), (1, 0), (1, 2), (2, 1), (0, 2), (2, 0)]:
    for a, b in [(0, 1), (1, 2), (0, 2)]:
        # two lists with same occourance each
        fstOccs = letterOccList[a][1]
        sndOccs = letterOccList[b][1]
        # try each composition for 'E' and 'T' (most occ in English)
        for fstLetter in fstOccs:
            for sndLetter in sndOccs:
                keyA, keyB = keyCalculate(fstLetter, sndLetter)
                if keyA == -1 or keyB == -1:
                    continue
                # get digrams and trigrams count of the keys
                tempPlain = affineDec(cipherText, keyA, keyB)
                diCount = ca.getDigramsInTextCount(tempPlain)
                triCount = ca.getTrigramsInTextCount(tempPlain)
                # record keys and the scounting result
                matchingDict[(keyA, keyB)] = diCount + triCount

    # take the largest count of digrams and trigrams, take result and return
    maxMatching = max(matchingDict.values())
    # there may have multiple keys which have same digrams and trigrams matching
    maxMatchingDicts = {k: v for k, v in matchingDict.items() if v == maxMatching}
    for keyA, keyB in maxMatchingDicts.keys():
        plainTexts.append(affineDec(cipherText, keyA, keyB))

    return plainTexts
