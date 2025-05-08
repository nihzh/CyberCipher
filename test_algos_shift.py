from algorithms import shiftCipher

# encryption: regular
def test_shift_encrypt_with_key():
    plain = "HELLO"
    key = 3
    expected = "KHOOR"
    result = shiftCipher.shiftEnc(plain, key)
    assert result == expected

# encryption: key upper boundary
def test_shift_encrypt_with_key_upper():
    plain = "HELLO"
    key = 25
    expected = "GDKKN"
    result = shiftCipher.shiftEnc(plain, key)
    assert result == expected

# encryption: key lower boundary
def test_shift_encrypt_with_key_lower():
    plain = "HELLO"
    key = 0
    expected = "HELLO"
    result = shiftCipher.shiftEnc(plain, key)
    assert result == expected

# encryption: key negative
def test_shift_encrypt_with_key_negative():
    plain = "HELLO"
    key = -5
    expected = "CZGGJ"
    result = shiftCipher.shiftEnc(plain, key)
    assert result == expected

# encryption: key equivalence
def test_shift_encrypt_with_key_equivalence():
    plain = "HELLO"
    key = 29
    expected = "KHOOR"
    result = shiftCipher.shiftEnc(plain, key)
    assert result == expected

# encryption: empty input
def test_shift_encrypt_with_key_input_empty():
    plain = ""
    key = 3
    expected = ""
    result = shiftCipher.shiftEnc(plain, key)
    assert result == expected

# encryption: lower input and punctuation
def test_shift_encrypt_with_key_input_lower():
    plain = "hello!"
    key = 3
    expected = "khoor!"
    result = shiftCipher.shiftEnc(plain, key)
    assert result == expected

# encryption: mix-case input
def test_shift_encrypt_with_key_input_mix():
    plain = "hEllO"
    key = 3
    expected = "kHooR"
    result = shiftCipher.shiftEnc(plain, key)
    assert result == expected



# decryption: regular
def test_shift_decrypt_with_key():
    cipher = "KHOOR"
    key = 3
    expected = "HELLO"
    result = shiftCipher.shiftDec(cipher, key)
    assert result == expected

# decryption: key upper boundary
def test_shift_decrypt_with_key_upper():
    cipher = "GDKKN"
    key = 25
    expected = "HELLO"
    result = shiftCipher.shiftDec(cipher, key)
    assert result == expected

# decryption: key lower boundary
def test_shift_decrypt_with_key_lower():
    cipher = "HELLO"
    key = 0
    expected = "HELLO"
    result = shiftCipher.shiftDec(cipher, key)
    assert result == expected

# decryption: key negative
def test_shift_decrypt_with_key_negative():
    cipher = "CZGGJ"
    key = -5
    expected = "HELLO"
    result = shiftCipher.shiftDec(cipher, key)
    assert result == expected

# decryption: empty input
def test_shift_decrypt_with_key_input_empty():
    cipher = ""
    key = 3
    expected = ""
    result = shiftCipher.shiftDec(cipher, key)
    assert result == expected

# decryption: lower input and punctuation
def test_shift_decrypt_with_key_input_lower():
    cipher = "khoor!"
    key = 3
    expected = "hello!"
    result = shiftCipher.shiftDec(cipher, key)
    assert result == expected

# decryption: mix-case input
def test_shift_decrypt_with_key_input_mix():
    cipher = "kHooR"
    key = 3
    expected = "hEllO"
    result = shiftCipher.shiftDec(cipher, key)
    assert result == expected

# cryptanalysis: regular
def test_shift_cryptanalysis():
    plain = "THISISASHIFTCIPHERCRYPTANALYSISTESTWHICHINEEDLONGERTEXTSFORINPUT"
    key = 7
    cipher = shiftCipher.shiftDec(plain, key)
    recovered = shiftCipher.shiftAnalysis(cipher)
    assert recovered == [plain.upper()]

# cryptanalysis: mix-case, punctuation and equivalence key
def test_shift_cryptanalysis_alter():
    plain = "THISISANOTHERCRYPTANALYSISTEXTINTESTALGORITHMSSHIFT, I hope it can be covered very well!"
    key = 77
    cipher = shiftCipher.shiftEnc(plain, key)
    recovered = shiftCipher.shiftAnalysis(cipher)
    assert recovered == [plain]
