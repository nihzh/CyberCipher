'''
File Name: cybercipher.py
Create: 12/15/2024
Description: The launch file of Flask
'''

# win: env\Scripts\activate    set FLASK_APP=cibercipher.py set FLASK_DEBUG=1
# linux: . env/bin/acitvate    export FLASK_APP=cybercipher.py
# deactivate

from flask import Flask, url_for, render_template, request, jsonify
from flask_wtf import CSRFProtect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from markupsafe import escape
# import cipher algorithms
from algorithms import affineCipher as aff
from algorithms import shiftCipher as sft
from algorithms import vigenereCipher as vig
# generare random key
import random
# ascii letters
import string
from utils import filterTool

app = Flask(__name__)
app.secret_key = "hello_cybercipher_Z"

# enable csrf protection
csrf = CSRFProtect(app)
# enable API access limit
limiter = Limiter(get_remote_address, app=app, default_limits=["20 per minute"])

INVERSE = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

# CSP strategy
@app.after_request
def apply_csp(response):
    response.headers['Content-Security-Policy'] = (
        "default-src 'self'; "
        "script-src 'self' https://code.jquery.com https://cdn.jsdelivr.net https://cdnjs.cloudflare.com; "
        "style-src 'self' https://cdnjs.cloudflare.com https://cdn.jsdelivr.net 'unsafe-inline'; "
        "font-src 'self' https://cdn.jsdelivr.net; "
        "img-src 'self' data:; "
        "object-src 'none'; "
        "base-uri 'self'; "
        "form-action 'self'; "
        "frame-ancestors 'none';"
    )
    return response


# index
@app.route('/')
def hello():
    # set session history
    # if "history" not in session:
    #     session["history"] = []
    return render_template("cybercipher.html", keyA=INVERSE)

# -------------------------
# Affine cipher controllers
# =========================

# input fileter for affine
def affine_filter(request):
    # get plain text data
    text = str(request.json.get("text"))
    input_keyA = request.json.get("keyA")
    input_keyB = request.json.get("keyB")

    keyA = None
    keyB = None

    # for key a, it needs to be an integer and within the INVERSE list
    if filterTool.is_int(input_keyA) and int(input_keyA) in INVERSE:
        keyA = int(input_keyA)

    # key b, needs be an integer and between 0-25
    if filterTool.is_int(input_keyB):
        keyB = int(input_keyB)
        # if not in 0-25, mod for trim
        if int(input_keyB) < 0 and int(input_keyB) > 25:
            keyB %= 26

    return text, keyA, keyB

# Affine encryption
@app.route('/affine/enc', methods=["POST"])
def affine_enc():
    # get data from fileter
    plainText, keyA, keyB = affine_filter(request)
    if len(plainText) == 0 or keyA == None or keyB == None:
        return jsonify({"status":"falure"})

    # encryption
    cipherText = aff.affineEnc(plainText, keyA, keyB)
    
    return jsonify({"status":"success", "result": cipherText})


# Affine decryption
@app.route('/affine/dec', methods=["POST"])
def affine_dec():
    cipherText, keyA, keyB = affine_filter(request)
    if cipherText == None or keyA == None or keyB == None:
        return jsonify({"status":"falure"})
    # decription
    plainText = aff.affineDec(cipherText, keyA, keyB)
    return jsonify({"status":"success", "result": plainText})

# Affine random key encryption, generate key and call encrypt
@app.route('/affine/rdmenc', methods=["POST"])
def affine_rdmenc():
    plainText = str(request.json.get("text"))

    # generate random key
    keyA = random.choice(INVERSE)
    keyB = random.randint(0, 25)
    # encrypt with random keys
    cipherText = aff.affineEnc(plainText, keyA, keyB)
    return jsonify({"status":"success", "result": cipherText, "keyA": keyA, "keyB": keyB})

# Affine cryptanalysis
@app.route('/affine/anldec', methods=["POST"])
def affine_anldec():
    cipherText = str(request.json.get("text"))
    
    plainText = aff.affineAnalysis(cipherText)
    # when multiple results, paging
    if len(plainText) > 1:
        outputText = ""
        for text, index in enumerate(plainText):
            outputText += f'Result {text}: {{"{index}"}}\n'
        plainText = outputText
    
    return jsonify({"status":"success", "result": plainText})


# -------------------------
# Shift cipher controllers
# =========================

# input fileter for shift
def shift_filter(request):
    # get plain text data
    text = str(request.json.get("text"))
    input_keyA = request.json.get("keyA")

    keyA = None

    # the key needs be an integer and between 0-25
    if filterTool.is_int(input_keyA):
        keyA = int(input_keyA)
        # if not in 0-25, mod for trim
        if int(input_keyA) < 0 and int(input_keyA) > 25:
            keyA %= 26

    return text, keyA

# Shift encryption
@app.route('/shift/enc', methods=["POST"])
def shift_enc():
    # get plain text and key from filter
    plainText, keyA = shift_filter(request)
    if len(plainText) == 0 or keyA == None:
        return jsonify({"status":"falure"})

    # encryption
    cipherText = sft.shiftEnc(plainText, keyA)
    return jsonify({"status":"success", "result": cipherText})

# Shift decryption
@app.route('/shift/dec', methods=["POST"])
def shift_dec():
    # get plain text and key from filter
    cipherText, keyA = shift_filter(request)
    if len(cipherText) == 0 or keyA == None:
        return jsonify({"status":"falure"})
    
    # decryption
    plainText = sft.shiftDec(cipherText, keyA)
    return jsonify({"status":"success", "result": plainText})

# Shift random key encryption, generate key and call encrypt
@app.route('/shift/rdmenc', methods=["POST"])
def shift_rdmenc():
    plainText = str(request.json.get("text"))
    # generate random key, between 0-25
    keyA = random.randint(0, 25)
    cipherText = sft.shiftEnc(plainText, keyA)
    return jsonify({"status":"success", "result": cipherText, "keyA": keyA})

# Shift cryptanalysis
@app.route('/shift/anldec', methods=["POST"])
def shift_anldec():
    cipherText = str(request.json.get("text"))

    plainText = sft.shiftAnalysis(cipherText)
    if len(plainText) > 1:
        outputText = ""
        for text, index in enumerate(plainText):
            outputText += f'Result {text}: {{"{index}"}}\n'
        plainText = outputText

    return jsonify({"status":"success", "result": plainText})


# -------------------------
# Vigenere cipher controllers
# =========================

# input fileter for vigenere
def vigenere_filter(request):
    # get plain text data
    text = str(request.json.get("text"))
    input_keyA = request.json.get("keyA")

    keyA = None

    # the key needs be an integer and between 0-25
    if filterTool.is_pure_str(str(keyA)):
        keyA = str(input_keyA)

    return text, keyA

# Vigenere encryption
@app.route('/vigenere/enc', methods=["POST"])
def vigenere_enc():
    # get plain text and key from filter
    plainText, keyA = vigenere_filter(request)
    if len(plainText) == 0 or keyA == None:
        return jsonify({"status":"falure"})
    
    # encryption
    cipherText = vig.vigEnc(plainText, keyA)

    return jsonify({"status":"success", "result": cipherText})

# Vigenere decryption
@app.route('/vigenere/dec', methods=["POST"])
def vigenere_dec():
    cipherText, keyA = vigenere_filter(request)
    if len(cipherText) == 0 or keyA == None:
        return jsonify({"status":"falure"})
    
    # decryption
    plainText = vig.vigDec(cipherText, keyA)
    return jsonify({"status":"success", "result": plainText})

# Vigenere random key encryption, generate key and call encrypt
@app.route('/vigenere/rdmenc', methods=["POST"])
def vigenere_rdmenc():
    plainText = str(request.json.get("text"))

    # generate random key, length 2-10
    keyLen = random.randint(2, 10)
    keyA = ''.join(random.choices(string.ascii_uppercase, k=keyLen))

    cipherText = vig.vigEnc(plainText, keyA)
    return jsonify({"status":"success", "result": cipherText, "keyA": keyA})

# Vigenere cryptanalysis
@app.route('/vigenere/anldec', methods=["POST"])
def vigenere_anldec():
    cipherText = str(request.json.get("text"))

    plainText = vig.vigAnalysis(cipherText)
    # will only have one result
    return jsonify({"status":"success", "result": plainText})


@app.route('/test')
def test():
    return render_template("test.html")

if __name__ == '__main__':
    app.run(debug = True)