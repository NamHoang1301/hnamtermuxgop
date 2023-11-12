import requests
import os
from datetime import datetime, timedelta
import json

def read_ip_from_file():
    try:
        with open('checkip.txt', 'r') as file:
            stored_ip = file.read().strip()
            stored_ip_dict = json.loads(stored_ip)
        return stored_ip_dict
    except FileNotFoundError:
        return None

def write_ip_to_file(ip):
    with open('checkip.txt', 'w') as file:
        ip_str = json.dumps(ip)
        file.write(ip_str)

def read_key_from_file():
    try:
        with open('Key_Nam.txt', 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return None

def write_key_to_file(key):
    with open('Key_Nam.txt', 'w') as file:
        file.write(key)

def check_ip_change(current_ip):
    stored_ip_dict = read_ip_from_file()

    if stored_ip_dict is None or stored_ip_dict != current_ip:
        write_ip_to_file(current_ip)
        return True
    return False

def generate_key(key1):
    return 'namdev' + key1[:8]

def check_expired_key(expiration_date):
    current_date = datetime.now()
    return current_date > expiration_date

def main():
    ip_changed = check_ip_change(requests.get('https://api64.ipify.org?format=json').json())

    key1 = input('Nhập Key API: ')
    key = generate_key(key1)
    long_url = f"https://keytool.namdev131.repl.co/?key={key}"

    api_token = '3fd7f06f-7545-4a1b-81a3-69d89df0d303'
    url = requests.get(f'https://web1s.com/api?token={api_token}&url={long_url}').json()
    url_dilink = requests.get(f'https://dilink.net/QL_api.php?token=58eb43b3c77c5319deaabl02294f9ffd585fafd5396bcbes325d64399fbda87d&url={long_url}').text

    if '<link rel="canonical" href="' in url_dilink:
        link_key_dilink = url_dilink.split('<link rel="canonical" href="')[1].split('">')[0]
    else:
        link_key_dilink = 'Không Thể Tạo Url!!!'

    status = url['status']
    link = url['shortenedUrl']

    key_expired = check_expired_key(datetime.now() + timedelta(days=3))

    if ip_changed or read_key_from_file() is None or key_expired:
        print('API Key Đã Hết Hạn, Vui Lòng Vượt Link Để Lấy Key Mới')
        print(f'-----------------------------------------------------------------')
        while True:
            key1 = input('Nhập Key API: ')
            key = generate_key(key1)
            if key == read_key_from_file():
                print('API Key Đúng!')
                print('Chào Mừng Bạn Đến Với Tool!!')
                write_key_to_file(key)
                exec(requests.get('url_them').text)
                break
            else:
                print(f'API Key Sai, Vui Lòng Nhập Lại!')
    else:
        print('Chào Mừng Bạn Đến Với Tool!!')
        exec(requests.get('url_them').text)

    print(f'-----------------------------------------------------------------')
    print(f"Link Lấy Key Của Tool !!")
    print(f'Truy Cập Vào Link: {link_key_dilink}')
    print(f'Truy Cập Vào Link: {link}')
    print(f'-----------------------------------------------------------------')

if __name__ == "__main__":
    main()
