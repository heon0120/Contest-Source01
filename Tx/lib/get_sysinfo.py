# 사용전 알림.
# 본 프로그램은 윈도우 10 이상의 환경에서 동작할수있으며, Linux, mac등 타 OS를 지원하지 않음.
# 또한, 프로그램은 단순 참조용으로만 사용해야함.
# 각 키의 디렉토리는 절대경로로 입력되었기 때문에, 이를 수정하고 사용해야함.
# 프로그램의 사용 또는 열람전 License.pdf를 숙지후 사용해야함.
# Made By TEAM Infinity
# Powerd By STUDIO CSGNS

import wmi
import uuid
import socket
import winreg
import hashlib
import getpass
def get_serial_number():
    try:
        c = wmi.WMI()
        # C 드라이브 시리얼 번호 조회
        for item in c.Win32_PhysicalMedia():
            c_drive_serial = item.SerialNumber.strip()
            return c_drive_serial  # 반환값으로 일련번호를 리턴
    except Exception as e:
        print("[ERROR] Getting Hash... ERROR!")
        print(f"[ERROR] Failed to retrieve serial number: {e}")
        return "unknown"

def get_mac_address():
    try:
        # MAC 주소 조회
        mac = [format(i, '02x') for i in uuid.getnode().to_bytes(6, 'big')]
        mac_address = ':'.join(mac)
        return mac_address  # 반환값으로 MAC 주소를 리턴
    except Exception as e:
        print("[ERROR] Getting Hash... ERROR!")
        print(f"[ERROR] Failed to retrieve MAC address: {e}")
        return "unknown"

def get_motherboard_serial():
    try:
        # 메인보드 시리얼 번호 조회
        c = wmi.WMI()
        for item in c.Win32_BaseBoard():
            mb_serial = item.SerialNumber.strip()
            return mb_serial  # 반환값으로 메인보드 일련번호를 리턴
    except Exception as e:
        print("[ERROR] Getting Hash... ERROR!")
        print(f"[ERROR] Failed to retrieve motherboard serial number: {e}")
        return "unknown"

def get_username():
    try:
        # 현재 사용자 이름 조회
        return getpass.getuser()
    except Exception as e:
        print("[ERROR] Getting Hash... ERROR!")
        print(f"[ERROR] Failed to retrieve username: {e}")
        return "unknown"

def get_hostname():
    try:
        # 호스트 이름 조회
        return socket.gethostname()
    except Exception as e:
        print("[ERROR] Getting Hash... ERROR!")
        print(f"[ERROR] Failed to retrieve hostname: {e}")
        return "unknown"

def get_windows_product_key():
    registry_path = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\SoftwareProtectionPlatform"
    key_name = "BackupProductKeyDefault"

    try:
        # 레지스트리에서 키 읽기
        registry = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, registry_path)
        product_key = winreg.QueryValueEx(registry, key_name)[0]
        winreg.CloseKey(registry)
        return product_key
    except Exception as e:
        print("[ERROR] Getting Hash... ERROR!")
        print(f"[ERROR] Failed to retrieve Windows product key: {e}")
        return "unknown"

def get_windows_product_id():
    registry_path = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion"
    key_name = "ProductId"

    try:
        # 레지스트리에서 키 읽기
        registry = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, registry_path)
        product_id = winreg.QueryValueEx(registry, key_name)[0]
        winreg.CloseKey(registry)
        return product_id
    except Exception as e:
        print("[ERROR] Getting Hash... ERROR!")
        print(f"[ERROR] Failed to retrieve Windows product ID: {e}")
        return "unknown"

def calculate_hash(value):
    try:
        # 주어진 값의 SHA-512 해시값 계산
        hash_sha512 = hashlib.sha512()
        hash_sha512.update(value.encode('utf-8'))
        return hash_sha512.hexdigest()
    except Exception as e:
        print("[ERROR] Getting Hash... ERROR!")
        print(f"[ERROR] Failed to calculate hash: {e}")
        return "unknown"

def get_sysinfo_sha512():
    try:
        # 시스템 정보 수집
        c_drive_serial = get_serial_number()
        mac_address = get_mac_address()
        mb_serial = get_motherboard_serial()
        username = get_username()
        hostname = get_hostname()
        windows_product_key = get_windows_product_key()
        windows_product_id = get_windows_product_id()

        # 모든 값을 결합하여 해시값 계산
        combined_values = f"{c_drive_serial}{mac_address}{mb_serial}{username}{hostname}{windows_product_key}{windows_product_id}"
        final_hash = calculate_hash(combined_values)
        print("[INFO] Getting Hash... Done!")
        return final_hash
    except Exception as e:
        print("[ERROR] Getting Hash... ERROR!")
        print(f"[ERROR] Failed to get system info or generate hash: {e}")
        return "unknown"

# 테스트용으로 시스템 정보 해시 출력
if __name__ == "__main__":
    print("System Information Hash: ", get_sysinfo_sha512())
    print("Cdrive Sirial: " + get_serial_number())
    print("mac_addr: " + get_mac_address())
    print("M/B Serial: " + get_motherboard_serial())
    print("User Name: " + get_username())
    print("Host name: " + get_hostname())
    print("windows Product Key: " + get_windows_product_key())
    print("windows Product ID: " + get_windows_product_id())