from algorithms import vigenereCipher

# encryption: regular
def test_vigenere_encrypt_regular():
    plain = "HELLO"
    key = "KEY"
    expected = "RIJVS"
    result = vigenereCipher.vigEnc(plain, key)
    assert result == expected

# encryption: empty input
def test_vigenere_encrypt_empty():
    plain = ""
    key = "KEY"
    expected = ""
    result = vigenereCipher.vigEnc(plain, key)
    assert result == expected

# encryption: mixed case and punctuations
def test_vigenere_encrypt_case_mixed():
    plain = "hEllO!"
    key = "KEY"
    expected = "rIjvS!"
    result = vigenereCipher.vigEnc(plain, key)
    assert result == expected

# decryption: regular
def test_vigenere_decrypt_regular():
    cipher = "RIJVS"
    key = "KEY"
    expected = "HELLO"
    result = vigenereCipher.vigDec(cipher, key)
    assert result == expected

# decryption: mixed case and punctuations
def test_vigenere_decrypt_case_mixed():
    cipher = "rIjVs!"
    key = "KEY"
    expected = "hElLo!"
    result = vigenereCipher.vigDec(cipher, key)
    assert result == expected

# cryptanalysis: longer text
def test_vigenere_cryptanalysis():
    original = "The sun dipped below the horizon, painting the sky in hues of orange and pink. A gentle breeze rustled the leaves, carrying the scent of blooming flowers. Birds chirped their evening songs, while the distant hum of the city faded into the background. The world seemed to pause, embracing the tranquility of the moment. As stars began to twinkle above, a sense of peace settled over the landscape. It was a perfect evening, a reminder of nature's beauty and the simple joys it brings. In that serene setting, time felt infinite, and worries melted away."
    key = "KEYWORD"
    cipher = vigenereCipher.vigEnc(original, key)
    recovered = vigenereCipher.vigAnalysis(cipher)
    # Cryptanalysis may only recover the plain text, regardless of case
    assert recovered == original
