# 사용전 알림.
# 본 프로그램은 윈도우 10 이상의 환경에서 동작할수있으며, Linux, mac등 타 OS를 지원하지 않음.
# 또한, 프로그램은 단순 참조용으로만 사용해야함.
# 각 키의 디렉토리는 절대경로로 입력되었기 때문에, 이를 수정하고 사용해야함.
# 프로그램의 사용 또는 열람전 License.pdf를 숙지후 사용해야함.
# Made By TEAM Infinity
# Powerd By STUDIO CSGNS

import json
import random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes

KEY_DIR = "D:\\workspace\\pythonProject3\\Tx\\lib\\key"  # 퍼블릭키 위치(절대경로)

def encrypt(text):
    print("[INFO] Encrypting text...")
    try:
        key_numbers = random.sample(range(1, 101), len(text))
    except ValueError as e:
        print("[ERROR] Encrypting text... ERROR!")
        print("[ERROR] You need more keys than text length.")
        return None, None

    keys = {}
    encrypted_data = {}
    for i, char in enumerate(text):
        key_number = key_numbers[i]
        try:
            with open(f"{KEY_DIR}/pub{key_number}.pem", "r") as f:
                key = RSA.import_key(f.read())
            keys[key_number] = key
        except FileNotFoundError:
            print("[ERROR] Encrypting text... ERROR!")
            print(f"[ERROR] Key file {KEY_DIR}/pub{key_number}.pem Not found")
            return None, None
        except ValueError:
            print("[ERROR] Encrypting text... ERROR!")
            print(f"[ERROR] The file {KEY_DIR}/pub{key_number}.pem is not a valid RSA key.")
            return None, None

        try:
            cipher = PKCS1_OAEP.new(keys[key_number])
            encrypted_data[str(key_number)] = cipher.encrypt(char.encode("utf-8")).hex()
        except Exception as e:
            print("[ERROR] Encrypting text... ERROR!")
            print(f"[ERROR] Error encryption with key {key_number}: {str(e)}")
            return None, None

    return json.dumps(encrypted_data), key_numbers  # 두 값을 반환

def en_text(plain_text):
    encrypted_json, key_numbers = encrypt(plain_text)# 두 값을 받아옴
    print("[INFO] Encrypting text... Done!")
    if encrypted_json is None or key_numbers is None:
        print("[ERROR] Encrypting text... ERROR!")
    return encrypted_json, key_numbers  # 두 값을 반환
