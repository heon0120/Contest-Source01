# 사용전 알림.
# 본 프로그램은 윈도우 10 이상의 환경에서 동작할수있으며, Linux, mac등 타 OS를 지원하지 않음.
# 또한, 프로그램은 단순 참조용으로만 사용해야함.
# 각 키의 디렉토리는 절대경로로 입력되었기 때문에, 이를 수정하고 사용해야함.
# 프로그램의 사용 또는 열람전 License.pdf를 숙지후 사용해야함.
# Made By TEAM Infinity
# Powerd By STUDIO CSGNS

import os
import time
import requests
from lib.encryption import en_text  # 암호화 함수 불러오기
from lib.get_sysinfo import get_sysinfo_sha512 # 해시값 가져오는 함수 불러오기
now = time
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


programversion = "k8nqjwz"
os.system('cls')



logo()
time.sleep(3)

while True:
    text = input("전송할 메시지 입력 (100자 이내): ")

    # 메시지 길이 체크
    if len(text) > 100:
        print("[ERROR] It cannot exceed 100 characters. Please tryagain.")
        time.sleep(2)
        os.system('cls')
        logo()
        continue  # 입력을 다시 받도록 루프의 시작으로 돌아감

    # 시스템 정보 해시 생성
    print("[INFO] Getting Hash...")

    sysinfo_hash = get_sysinfo_sha512()  # 해시 생성


    # 텍스트 암호화

    encrypted_text, key_numbers = en_text(text)  # 암호화 함수 호출

    # 메시지 생성

    send_message = {
        "encrypted_text": encrypted_text,
        "key_numbers": key_numbers,
        "hash": sysinfo_hash,
        "time": now.localtime()
    }

    url = "http://127.0.0.1:5000/decrypt"  # 수신자의 주소

    print("[INFO] Sanding Massage...")
    try:
        # POST 요청 보내기
        response = requests.post(url, json=send_message)

        # 응답 처리
        if response.status_code == 200:
            print("[INFO] Sanding Massage... Done!")
            time.sleep(2)
            os.system('cls')
            logo()
        else:
            print("[ERROR] Sanding Massage... ERROR!")
            print(f"[ERROR] {response.json().get('error')}")
    except requests.exceptions.RequestException as e:
        print("[INFO] Sanding Massage... ERROR!")
        print("[ERROR] Internal Server ERROR - Server is gone")
        time.sleep(2)
        os.system('cls')
        logo()
        continue
    except KeyboardInterrupt:
        print("\n[INFO] Process interrupted by user. Exiting...")
        break  # 사용자에 의해 프로세스가 중단되면 루프 탈출