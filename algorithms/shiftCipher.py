'''
File Name: shiftCipher.py
Create: 12/17/2024
Description: Encryption, decryption and cryptanalysis function of shift cipher
'''
import cryptanalysis as ca

# shift cipher: encrypt by key
def enc(plainText, key):
    cipherText = ""
    for eachChar in plainText:
        if eachChar.isupper():
            # minus 65 (charactor A), calculate value and plus 65
            cipherText += chr((ord(eachChar) - 65 + key) % 26 + 65)
        elif eachChar.islower():
            # minus 97 (charactor a), calculate value and plus 97
            cipherText += chr((ord(eachChar) - 97 + key) % 26 + 97)
        else:
            # not alpha, copy the origin
            cipherText += eachChar
    return cipherText

# shift cipher: decrypt by key
def dec(cipherText, key):
    plainText = ""
    for eachChar in cipherText:
        if eachChar.isupper():
            # minus 65 (charactor A), calculate value and plus 65
            plainText += chr((ord(eachChar) - 65 - key) % 26 + 65)
        elif eachChar.islower():
            # minus 97 (charactor a), calculate value and plus 97
            plainText += chr((ord(eachChar) - 97 - key) % 26 + 97)
        else:
            # not alpha, copy the origin
            plainText += eachChar
    return plainText


text = """FMXVEYIFQFMZRWQFYVECFMDZPCVMRZWNMDZVEJBTXCDDUMJ
NDIFEFMDZCDMQZKCEYFCJMYRNCWJCSZREXCHZUNMXZ
NZUCDRJXYYSMRTMEYIFZWDYVZVYFZUMRZCRWNZDZJJ
XZWGCHSMRNMDHNCMFQCHZJMXJZWIEJYUCFWDJNZDIRDKaXMFERBNDKRXRSREXmORUDSDKDVSHVUFEDKAPRkXDLYEVLRHHRH"""

def shiftAnalysis(plainText):
    letterOcc = ca.getLetterOccDict(plainText)
    rankedLetterOcc = sorted(letterOcc.items(), key = lambda item:item[1], reverse = True)
    
    
    return rankedLetterOcc

print(shiftAnalysis(text))