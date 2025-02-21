from flask import Blueprint, request, jsonify

week_one_bp = Blueprint('week_one', __name__, url_prefix='/weekOne')


@week_one_bp.route('/caesarEncrypt', methods=['GET', 'POST'])
def caesar_encrypt():
    data = request.get_json()
    plaintext = data.get('plaintext', '')
    shift = data.get('shift', 0)
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return jsonify({'encrypted_text': encrypted_text})


@week_one_bp.route('/caesarDecrypt', methods=['GET', 'POST'])
def caesar_decrypt():
    data = request.get_json()
    ciphertext = data.get('ciphertext', '')
    shift = data.get('shift', 0)
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr(((ord(char) - ord('A' if char.isupper() else 'a') - shift_amount) % 26) + ord(
                'A' if char.isupper() else 'a'))
            plaintext += new_char
        else:
            plaintext += char
    return jsonify({'decrypted_text': plaintext})


@week_one_bp.route('/caesarAttack', methods=['GET', 'POST'])
def caesar_attack():
    data = request.get_json()
    ciphertext = data.get('ciphertext', '')
    results = []
    print(ciphertext)
    for shift in range(26):
        decrypted = ''
        for char in ciphertext:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                decrypted += chr((ord(char) - base - shift) % 26 + base)
            else:
                decrypted += char
        results.append({
            'shift': shift,
            'decrypted_text': decrypted
        })
    return jsonify(results)


@week_one_bp.route('/monoAlphabeticEncrypt', methods=['GET', 'POST'])
def mono_alphabetic_encrypt():
    data = request.get_json()
    plaintext = data.get('plaintext', '')
    shift = data.get('shift', 0)
    encrypted_text = "".join(chr((ord(char) + shift) % 256) for char in plaintext)
    return jsonify({'encrypted_text': encrypted_text})


@week_one_bp.route('/monoAlphabeticDecrypt', methods=['GET', 'POST'])
def mono_alphabetic_decrypt():
    data = request.get_json()
    ciphertext = data.get('ciphertext', '')
    shift = data.get('shift', 0)
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            ascii_set = ord('A') if char.isupper() else ord('a')
            position = (ord(char) - ascii_set - shift) % 256
            plaintext += chr(position + ascii_set)
        else:
            plaintext += char
    return jsonify({'decrypted_text': plaintext})
