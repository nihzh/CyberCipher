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

app = Flask(__name__)

name="Z"
INVERSE = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

# index
@app.route('/')
def hello():
    return render_template("index.html", keyA=INVERSE)

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
    # encryption
    cipherText = aff.affineEnc(plainText, keyA, keyB)
    # TODO: add session, timeset
    return jsonify({"result": cipherText})


# Affine decryption
@app.route('/affine/dec', methods=["POST"])
def affine_dec():
    plainText = str(request.json.get("text"))
    keyA = request.json.get("keyA")
    keyB = request.json.get("keyB")
    plainText = aff.affineDec(plainText, keyA, keyB)
    return jsonify({"result": plainText})

# Affine random key encryption, generate key and call encrypt
@app.route('/affine/rdmenc')
def affine_rdmenc(text):
    return f"<h1>Hello worldddddddd!</h1><lt />User: {escape(name)}"

# Affine cryptanalysis
@app.route('/affine/anldec')
def affine_anldec(text):
    return f"<h1>Hello worldddddddd!</h1><lt />User: {escape(name)}"

# -------------------------
# Caesar cipher controllers
# =========================


@app.route('/test')
def test():
    return render_template("test.html")

if __name__ == '__main__':
    app.run(debug = True)