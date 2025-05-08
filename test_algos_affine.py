from algorithms import affineCipher

# encryption: regular
def test_affine_encrypt_regular():
    plain = "HELLO"
    keyA, keyB = 5, 8
    expected = "RCLLA"
    result = affineCipher.affineEnc(plain, keyA, keyB)
    assert result == expected

# encryption: key lower boundary
def test_affine_encrypt_key_lower():
    plain = "HELLO"
    keyA, keyB = 1, 0
    expected = "HELLO"
    result = affineCipher.affineEnc(plain, keyA, keyB)
    assert result == expected

# encryption: key equivalence
def test_affine_encrypt_key_equivalence():
    plain = "HELLO"
    keyA, keyB = 5, 34
    expected = "RCLLA"
    result = affineCipher.affineEnc(plain, keyA, keyB)
    assert result == expected

# encryption: empty input
def test_affine_encrypt_empty():
    plain = ""
    keyA, keyB = 5, 8
    expected = ""
    result = affineCipher.affineEnc(plain, keyA, keyB)
    assert result == expected

# encryption: mixed case and punctuation
def test_affine_encrypt_case_mixed():
    plain = "hEllO!"
    keyA, keyB = 5, 8
    expected = "rCllA!"
    result = affineCipher.affineEnc(plain, keyA, keyB)
    assert result == expected


# decryption: regular
def test_affine_decrypt_regular():
    cipher = "RCLLA"
    keyA, keyB = 5, 8
    expected = "HELLO"
    result = affineCipher.affineDec(cipher, keyA, keyB)
    assert result == expected

# decryption: key lower bound
def test_affine_decrypt_key_lower():
    cipher = "HELLO"
    keyA, keyB = 1, 0
    expected = "HELLO"
    result = affineCipher.affineDec(cipher, keyA, keyB)
    assert result == expected

# decryption: key equivalence
def test_affine_decrypt_key_equivalence():
    cipher = "RCLLA"
    keyA, keyB = 5, 34
    expected = "HELLO"
    result = affineCipher.affineDec(cipher, keyA, keyB)
    assert result == expected

# decryption: mixed case and punctuations
def test_affine_decrypt_case_mixed():
    cipher = "rCllA!"
    keyA, keyB = 5, 8
    expected = "hEllO!"
    result = affineCipher.affineDec(cipher, keyA, keyB)
    assert result == expected


# cryptanalysis: regular
def test_affine_cryptanalysis():
    original = "THISISANAFFINECIPHERCRYPTOANALYSISTESTITMIGHTNEEDSALONGERPIECEOFTEXTSO, I hope it can runs well!"
    keyA, keyB = 11, 7
    cipher = affineCipher.affineEnc(original, keyA, keyB)
    recovered = affineCipher.affineAnalysis(cipher)
    assert [original] == recovered
