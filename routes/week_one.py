from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
import random

week_one_bp = Blueprint('week_one', __name__, url_prefix='/weekOne')


@week_one_bp.route('/caesarEncrypt', methods=['POST', 'GET'])
def caesar_encrypt():
    data = request.get_json()
    plaintext = data.get('plaintext', '')
    shift = data.get('shift', 0)
    encrypted_text = ""
    for char in plaintext:
        encrypted_text += chr((ord(char) + shift) % 256)
    return jsonify({'encrypted_text': encrypted_text})


@week_one_bp.route('/caesarDecrypt', methods=['POST', 'GET'])
def caesar_decrypt():
    data = request.get_json()
    ciphertext = data.get('ciphertext', '')
    shift = data.get('shift', 0)
    plaintext = ""
    for char in ciphertext:
        shift_amount = shift % 256
        new_char = chr(((ord(char) - shift_amount) % 256))
        plaintext += new_char

    return jsonify({'decrypted_text': plaintext})


@week_one_bp.route('/caesarAttack', methods=['POST', 'GET'])
def caesar_attack():
    data = request.get_json()
    ciphertext = data.get('ciphertext', '')
    results = []
    print(ciphertext)
    for shift in range(256):
        decrypted = ''
        for char in ciphertext:
            decrypted += chr((ord(char) - shift) % 256)
        results.append({
            'shift': shift,
            'decrypted_text': decrypted
        })
    return jsonify(results)


@week_one_bp.route('/monoAlphabeticEncrypt', methods=['POST'])
def mono_alphabetic_encrypt():
    data = request.get_json()
    plaintext = data.get('plaintext', '').lower()

    alphabet = [chr(i) for i in range(97, 123)]  # a-z
    shuffled_alphabet = alphabet[:]
    random.shuffle(shuffled_alphabet)

    key_str = ''.join(shuffled_alphabet)  # Concatenated key
    key = dict(zip(alphabet, shuffled_alphabet))

    ciphertext = ''.join(key.get(char, char) for char in plaintext)

    return jsonify({'encrypted_text': ciphertext, 'key': key_str})


@week_one_bp.route('/monoAlphabeticDecrypt', methods=['POST', 'GET'])
def mono_alphabetic_decrypt():
    data = request.get_json()
    ciphertext = data.get('ciphertext', '')
    shift = data.get('shift', {})
    print(shift)
    print(ciphertext)
    plaintext = ""
    for char in ciphertext:
        if char.lower() in shift:
            plaintext_char = shift[char.lower()]
            if char.isupper():
                plaintext += plaintext_char.upper()
            else:
                plaintext += plaintext_char
        else:
            plaintext += char
    return jsonify({'decrypted_text': plaintext})
