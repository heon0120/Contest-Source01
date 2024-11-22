# 사용전 알림.
# 본 프로그램은 윈도우 10 이상의 환경에서 동작할수있으며, Linux, mac등 타 OS를 지원하지 않음.
# 또한, 프로그램은 단순 참조용으로만 사용해야함.
# 각 키의 디렉토리는 절대경로로 입력되었기 때문에, 이를 수정하고 사용해야함.
# 프로그램의 사용 또는 열람전 License.pdf를 숙지후 사용해야함.
# Made By TEAM Infinity
# Powerd By STUDIO CSGNS

import os
import time
import json
from tqdm import tqdm
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from flask import Flask, request, jsonify
programversion = "k8nqjwz"
os.system('cls')



KEY_DIR = "key"  # 프라이빗키 위치( 상대경로)
HASH_FILE = "hash.txt"  # 해시 파일 위치
OUTPUT_FILE = "decrypted_output.txt"  # 복호화된 내용을 저장할 파일

app = Flask(__name__)
def logo():

    print(("\n" + "=" * 100 + "\n"))
    print("Powerd By")

    # infinity 아스키아트
    print(
        "          _____                    _____                    _____                    _____                    _____                    _____                _____                _____")
    print(
        "         /\\    \\                  /\\    \\                  /\\    \\                  /\\    \\                  /\\    \\                  /\\    \\              /\\    \\              |\\    \\")
    print(
        "        /::\\    \\                /::\\____\\                /::\\    \\                /::\\    \\                /::\\____\\                /::\\    \\            /::\\    \\             |:\\____\\")
    print(
        "        \\:::\\    \\              /::::|   |               /::::\\    \\               \\:::\\    \\              /::::|   |                \\:::\\    \\           \\:::\\    \\            |::|   |")
    print(
        "         \\:::\\    \\            /:::::|   |              /::::::\\    \\               \\:::\\    \\            /:::::|   |                 \\:::\\    \\           \\:::\\    \\           |::|   |")
    print(
        "          \\:::\\    \\          /::::::|   |             /:::/\\:::\\    \\               \\:::\\    \\          /::::::|   |                  \\:::\\    \\           \\:::\\    \\          |::|   |")
    print(
        "           \\:::\\    \\        /:::/|::|   |            /:::/__\\:::\\    \\               \\:::\\    \\        /:::/|::|   |                   \\:::\\    \\           \\:::\\    \\         |::|   |")
    print(
        "           /::::\\    \\      /:::/ |::|   |           /::::\\   \\:::\\    \\              /::::\\    \\      /:::/ |::|   |                   /::::\\    \\          /::::\\    \\        |::|   |")
    print(
        "  ____    /::::::\\    \\    /:::/  |::|   | _____    /::::::\\   \\:::\\    \\    ____    /::::::\\    \\    /:::/  |::|   | _____    ____    /::::::\\    \\        /::::::\\    \\       |::|___|______")
    print(
        " /\\   \\  /:::/\\:::\\    \\  /:::/   |::|   |/\\    \\  /:::/\\:::\\   \\:::\\    \\  /\\   \\  /:::/\\:::\\    \\  /:::/   |::|   |/\\    \\  /\\   \\  /:::/\\:::\\    \\      /:::/\\:::\\    \\      /::::::::\\    \\")
    print(
        "/::\\   \\/:::/  \\:::\\____\\/:: /    |::|   /::\\____\\/:::/  \\:::\\   \\:::\\____\\/::\\   \\/:::/  \\:::\\____\\/:: /    |::|   /::\\____\\/::\\   \\/:::/  \\:::\\____\\    /:::/  \\:::\\____\\    /::::::::::\\____\\")
    print(
        "\\:::\\  /:::/    \\::/    /\\::/    /|::|  /:::/    /\\::/    \\:::\\   \\::/    /\\:::\\  /:::/    \\::/    /\\::/    /|::|  /:::/    /\\:::\\  /:::/    \\::/    /   /:::/    \\::/    /   /:::/~~~~/~~")
    print(
        " \\:::\/:::/    / \\/____/  \\/____/ |::| /:::/    /  \\/____/ \\:::\\   \\/____/  \\:::\/:::/    / \\/____/  \\/____/ |::| /:::/    /  \\:::\/:::/    / \\/____/   /:::/    / \\/____/   /:::/    /")
    print(
        "  \\::::::/    /                   |::|/:::/    /            \\:::\\    \\       \\::::::/    /                   |::|/:::/    /    \\::::::/    /           /:::/    /           /:::/    /")
    print(
        "   \\::::/____/                    |::::::/    /              \\:::\\____\\       \\::::/____/                    |::::::/    /      \\::::/____/           /:::/    /           /:::/    /")
    print(
        "    \\:::\\    \\                    |:::::/    /                \\::/    /        \\:::\\    \\                    |:::::/    /        \\:::\\    \\           \\::/    /            \\::/    /")
    print(
        "     \\:::\\    \\                   |::::/    /                  \\/____/          \\:::\\    \\                   |::::/    /          \\:::\\    \\           \\/____/              \\/____/")
    print(
        "      \\:::\\    \\                  /:::/    /                                     \\:::\\    \\                  /:::/    /            \\:::\\    \\")
    print(
        "       \\:::\\____\\                /:::/    /                                       \\:::\\____\\                /:::/    /              \\:::\\____\\")
    print(
        "        \\::/    /                \\::/    /                                         \\::/    /                \\::/    /                \\::/    /")
    print(
        "         \\/____/                  \\/____/                                           \\/____/                  \\/____/                  \\/____/")
    print(("\n" + "=" * 100 + "\n"))
    print((
                      "programversion: " + programversion + "\nMade By TEAM INFINITY\n\nLicense\n라이선스에 준수하여 사용하시오.\n자세한것은 License.pdf를 참조하시오.\n\n\n" + "\n" + "=" * 100 + "\n"))
logo()
time.sleep(3)
def load_stored_hash():
    try:
        with open(HASH_FILE, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        print("[ERROR] Hash file not found.")
        return None
    except IOError as e:
        print(f"[ERROR] Unable to read hash file: {e}")
        return None

def decrypt_text(encrypted_json, key_numbers):
    keys = {}
    decrypted_text = ""
    for key_number in key_numbers:
        try:
            with open(f"{KEY_DIR}/priv{key_number}.pem", "r") as f:
                key = RSA.import_key(f.read())
            keys[key_number] = key
        except FileNotFoundError:
            print(f"[ERROR] Private key file {KEY_DIR}/priv{key_number}.pem not found.")
            return None
        except ValueError:
            print(f"[ERROR] Invalid RSA key in file {KEY_DIR}/priv{key_number}.pem.")
            return None

    for key_number in tqdm(key_numbers, desc="Decrypting"):
        encrypted_text = encrypted_json.get(str(key_number))
        if encrypted_text:
            try:
                cipher = PKCS1_OAEP.new(keys[key_number])
                decrypted_char = cipher.decrypt(bytes.fromhex(encrypted_text)).decode("utf-8")
                decrypted_text += decrypted_char
            except ValueError as e:
                print(f"[ERROR] Decryption failed for key {key_number}: {e}")
            except Exception as e:
                print(f"[ERROR] Unexpected error during decryption for key {key_number}: {e}")
    return decrypted_text

# 로그 저장 - 성능리소스 너무 많이 잡아먹음

def save_request_data(headers, body):
    try:
        with open(OUTPUT_FILE, 'a') as f:
            f.write("[REQUEST HEADER]\n")
            for key, value in headers.items():
                f.write(f"{key}: {value}\n")
            f.write("[REQUEST BODY]\n")
            f.write(f"{body}\n")
            f.write("\n" + "=" * 40 + "\n")  # 구분선
    except IOError as e:
        print(f"[ERROR] Unable to write to output file {OUTPUT_FILE}: {e}")

@app.route('/decrypt', methods=['POST'])
def decrypt_request():
    data = request.json
    if not data or 'encrypted_text' not in data or 'key_numbers' not in data or 'hash' not in data or 'time' not in data:
        return jsonify({"error": "Missing required fields"}), 400

    save_request_data(dict(request.headers), request.get_data(as_text=True))

    encrypted_text = data['encrypted_text']
    key_numbers = data['key_numbers']
    received_hash = data['hash']
    timestamp = data['time']

    try:
        request_time = time.mktime((timestamp[0], timestamp[1], timestamp[2],
                                    timestamp[3], timestamp[4], timestamp[5],
                                    0, 0, -1)) # 마지막 세 인자 무시
    except (TypeError, ValueError) as e:
        print(f"[ERROR] Invalid timestamp format: {e}")
        return jsonify({"error": "Invalid timestamp format"}), 400

    current_time = time.time()
    timeout_message = ""
    if current_time - request_time > 600:
        timeout_message = " (Timeout)"

    try:
        encrypted_json = json.loads(encrypted_text)
    except json.JSONDecodeError as e:
        print(f"[ERROR] Failed to decode encrypted text JSON: {e}")
        return jsonify({"error": "Invalid encrypted text format"}), 400

    decrypted_text = decrypt_text(encrypted_json, key_numbers)
    if decrypted_text is None:
        return jsonify({"error": "Decryption failed"}), 500

    stored_hash = load_stored_hash()
    if stored_hash is None:
        return jsonify({"error": "Hash file not found"}), 500

    verification_status = "successful" if received_hash == stored_hash else "failed"
    if verification_status == "failed":
        print(f"[WARNING] Hash mismatch: received={received_hash}, stored={stored_hash}")

    print(f"\n\n[INFO] Decrypted text: {decrypted_text}{timeout_message} (Verification: {verification_status})")
    return jsonify({"message": "ok"})

if __name__ == "__main__":
    app.run(debug=True)
