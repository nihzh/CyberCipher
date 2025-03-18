'''
File Name: cybercipher.py
Create: 12/15/2024
Description: The launch file of Flask
'''

# win: env\Scripts\activate    set FLASK_APP=cibercipher.py set FLASK_DEBUG=1
# linux: . env/bin/acitvate    export FLASK_APP=cybercipher.py
# deactivate

from flask import Flask, url_for, render_template, request, session, jsonify
from markupsafe import escape
# import cipher algorithms
from algorithms import affineCipher as aff
from algorithms import shiftCipher as sft
from algorithms import vigenereCipher as vig
# # import history record structure
# from utils.CipherHistory import CipherHistory
# # get datetime for utc+0
# from datetime import datetime, timezone
# generare random key
import random
# ascii letters
import string

app = Flask(__name__)
app.secret_key = "hello_cybercipher_Z"

name="Z"
INVERSE = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

# index
@app.route('/')
def hello():
    # set session history
    if "history" not in session:
        session["history"] = []
    return render_template("cybercipher.html", keyA=INVERSE)

# -------------------------
# Affine cipher controllers
# =========================

# Affine encryption
@app.route('/affine/enc', methods=["POST"])
def affine_enc():
    # get plain text data
    plainText = str(request.json.get("text"))
    keyA = request.json.get("keyA")
    keyB = request.json.get("keyB")
    # TODO: decode
    # TODO: filter
    # 400 Bad Request → 缺少 value 键  422 Unprocessable Entity → value 不能是负数。
    # encryption
    cipherText = aff.affineEnc(plainText, keyA, keyB)
    # TODO: add session, timeset

    # record = CipherHistory(
    #     originText = plainText,
    #     keyA = keyA,
    #     keyB = keyB,
    #     resultText = cipherText,
    #     cipherType = "Affine",
    #     actionType = "Encrypt",
    #     # timestamp = datetime.now(timezone.utc).timestamp()
    #     timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    # )

    return jsonify({"result": cipherText})


# Affine decryption
@app.route('/affine/dec', methods=["POST"])
def affine_dec():
    cipherText = str(request.json.get("text"))
    keyA = request.json.get("keyA")
    keyB = request.json.get("keyB")
    plainText = aff.affineDec(cipherText, keyA, keyB)
    return jsonify({"result": plainText})

# Affine random key encryption, generate key and call encrypt
@app.route('/affine/rdmenc', methods=["POST"])
def affine_rdmenc():
    plainText = str(request.json.get("text"))
    # generate random key
    keyA = random.choice(INVERSE)
    keyB = random.randint(0, 25)

    cipherText = aff.affineEnc(plainText, keyA, keyB)
    # return jsonify({"result": cipherText, "keyA": keyA, "keyB": keyB})
    return jsonify({"result": cipherText, "keyA": keyA, "keyB": keyB})

# Affine cryptanalysis
@app.route('/affine/anldec', methods=["POST"])
def affine_anldec():
    cipherText = str(request.json.get("text"))

    plainText = aff.affineAnalysis(cipherText)
    if len(plainText) > 1:
        outputText = ""
        for text, index in enumerate(plainText):
            outputText += f'Result {text}: {{"{index}"}}\n'
        plainText = outputText
    
    return jsonify({"result": plainText})


# -------------------------
# Shift cipher controllers
# =========================

# Shift encryption
@app.route('/shift/enc', methods=["POST"])
def shift_enc():
    # get plain text data
    plainText = str(request.json.get("text"))
    keyA = request.json.get("keyA")
    # TODO: decode
    # TODO: filter
    # encryption
    cipherText = sft.shiftEnc(plainText, keyA)
    # TODO: add session, timeset

    return jsonify({"result": cipherText})

# Shift decryption
@app.route('/shift/dec', methods=["POST"])
def shift_dec():
    cipherText = str(request.json.get("text"))
    keyA = request.json.get("keyA")
    plainText = sft.shiftDec(cipherText, keyA)
    return jsonify({"result": plainText})

# Shift random key encryption, generate key and call encrypt
@app.route('/shift/rdmenc', methods=["POST"])
def shift_rdmenc():
    plainText = str(request.json.get("text"))
    # generate random key
    keyA = random.randint(0, 25)
    cipherText = sft.shiftEnc(plainText, keyA)
    return jsonify({"result": cipherText, "keyA": keyA})

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

    return jsonify({"result": plainText})


# -------------------------
# Vigenere cipher controllers
# =========================

# Vigenere encryption
@app.route('/vigenere/enc', methods=["POST"])
def vigenere_enc():
    # get plain text data
    plainText = str(request.json.get("text"))
    keyA = request.json.get("keyA")
    # TODO: decode
    # TODO: filter
    # encryption
    cipherText = vig.vigEnc(plainText, keyA)
    # TODO: add session, timeset

    return jsonify({"result": cipherText})

# Vigenere decryption
@app.route('/vigenere/dec', methods=["POST"])
def vigenere_dec():
    cipherText = str(request.json.get("text"))
    keyA = request.json.get("keyA")
    plainText = vig.vigDec(cipherText, keyA)
    return jsonify({"result": plainText})

# Vigenere random key encryption, generate key and call encrypt
@app.route('/vigenere/rdmenc', methods=["POST"])
def vigenere_rdmenc():
    plainText = str(request.json.get("text"))
    # generate random key
    keyLen = random.randint(2, 10)
    keyA = ''.join(random.choices(string.ascii_uppercase, k=keyLen))
    cipherText = vig.vigEnc(plainText, keyA)
    return jsonify({"result": cipherText, "keyA": keyA})

# Vigenere cryptanalysis
@app.route('/vigenere/anldec', methods=["POST"])
def vigenere_anldec():
    cipherText = str(request.json.get("text"))
    plainText = vig.vigAnalysis(cipherText)
    return jsonify({"result": plainText})



@app.route('/test')
def test():
    return render_template("test.html")

if __name__ == '__main__':
    app.run(debug = True)