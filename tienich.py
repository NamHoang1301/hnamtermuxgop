from builtins import all,exec,format,id,print,int,range,set,str,open,quit
exec('')
import os
try:
	import requests,colorama,prettytable
except:
	os.system('pip install requests')
	os.system('pip install colorama')
	os.system('pip install prettytable')
import threading,requests,ctypes,random,json,time,base64,sys,re
from prettytable import PrettyTable
import random
from time import strftime
from colorama import init,Fore
from urllib.parse import urlparse,unquote,quote
from string import ascii_letters,digits
from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import requests
import base64, json,os
from datetime import date
from datetime import datetime
from time import sleep,strftime
from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import uuid, re
from pystyle import Write,Colors
from bs4 import BeautifulSoup
import socket
from datetime import datetime
time=datetime.now().strftime("%H:%M:%S")
from pystyle import *
import platform
import webbrowser
data_machine = []
today = date.today()
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")
def open_webpage(url):
    # Kiểm tra loại thiết bị
    device = platform.system()
    if device == "Windows":
        # Nếu là máy tính cá nhân chạy Windows, mở trang web bằng trình duyệt mặc định của máy tính
        webbrowser.open(url)
    elif device == "Darwin":
        # Nếu là máy tính cá nhân chạy macOS, mở trang web bằng trình duyệt mặc định của macOS
        webbrowser.open(url)
    elif device == "Linux":
        # Nếu là máy tính cá nhân chạy Linux, mở trang web bằng trình duyệt mặc định của Linux
        webbrowser.open(url)
    else:
        # Nếu là thiết bị di động hoặc không xác định, mở trang web bằng trình duyệt mặc định của thiết bị
        webbrowser.open(url)
web_url = "https://hongtet.namdev131.repl.co/"
url2 = "https://tangcau.namdev131.repl.co/"
#IP
def get_ip_from_url(url):
    response = requests.get(url)
    ip_address = socket.gethostbyname(response.text.strip())
    return ip_address
url = "http://kiemtraip.com/raw.php"
ip = get_ip_from_url(url)

import os,sys
import requests,json
from time import sleep
from datetime import datetime, timedelta
import base64,requests,os
#màu
lam = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb="\033[1;37m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'
#đánh dấu bản quyền
edit = vang+"]"+trang+"["+do+"[⟨⟩]"+trang+"]"+vang+"["+trang+" ➩ "+luc
edit1 = trang+"["+do+"[⟨⟩]"+trang+"]"+trang+" ➩ "+luc
# =======================[ NHẬP KEY ]=======================
import os, sys, requests
from time import sleep
from pystyle import *
from time import strftime
from datetime import datetime, timedelta
now=datetime.now()
os.system("cls" if os.name == "nt" else "clear")
def check_internet_connection():
    try:
        response = requests.get("http://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

# Kiểm tra kết nối internet
if check_internet_connection():
    print(f"{luc}Vui Lòng Chờ!!!")
    sleep(0.1)
else:
    print(f"{do}Vui Lòng Kiểm Tra Kết NốI!!!")
    sys.exit()
def get_location_by_ip():
    try:
        response = requests.get("https://ipinfo.io")
        data = response.json()

        city = data.get("city")
        region = data.get("region")
        country = data.get("country")
        loc = data.get("loc").split(",")
        latitude, longitude = loc if len(loc) == 2 else (None, None)

        return city, region, country, latitude, longitude
    except Exception as e:
        print(f"Lỗi: {e}")
        return None, None, None, None, None
city, region, country, latitude, longitude = get_location_by_ip()
def get_weather():
    try:
        # Lấy thông tin vị trí từ dịch vụ ipinfo.io
        response = requests.get("https://ipinfo.io")
        data = response.json()
        location = data.get("loc").split(",")
        latitude, longitude = location
        # Lấy thông tin thời tiết từ trang web công cộng
        base_url = f"https://wttr.in/{latitude},{longitude}?format=%t"
        response = requests.get(base_url)
        weather_description = response.text.strip()
        return weather_description
    except Exception as e:
        print(f"Lỗi: {e}")
        return None
weather_description = get_weather()
System.Clear()
banner=f"""
\033[1;31m┌═════════════════════════════════════════════════════════════════════════════┐
\033[1;31m██████╗ ███╗  ██╗ █████╗ ███╗   ███╗      ██╗  ██╗███╗  ██╗ █████╗ ███╗   ███╗
\033[1;32m██╔══██╗████╗ ██║██╔══██╗████╗ ████║      ██║  ██║████╗ ██║██╔══██╗████╗ ████║
\033[1;33m██████╦╝██╔██╗██║███████║██╔████╔██║█████╗███████║██╔██╗██║███████║██╔████╔██║
\033[1;34m██╔══██╗██║╚████║██╔══██║██║╚██╔╝██║╚════╝██╔══██║██║╚████║██╔══██║██║╚██╔╝██║
\033[1;36m██████╦╝██║ ╚███║██║  ██║██║ ╚═╝ ██║      ██║  ██║██║ ╚███║██║  ██║██║ ╚═╝ ██║
\033[1;35m╚═════╝ ╚═╝  ╚══╝╚═╝  ╚═╝╚═╝     ╚═╝      ╚═╝  ╚═╝╚═╝  ╚══╝╚═╝  ╚═╝╚═╝     ╚═╝  
\033[1;34m┠═════════════════════════════════════════════════════════════════════════════┨
\033[1;34m ➯ Cre : \033[1;31mBảo Nam x Hoàng Nam
\033[1;34m ➯ Nhóm Zalo : \033[1;37mhttps://zalo.me/g/pdsvkf650
\033[1;34m ➯ Facebook Bảo Nam : \033[1;37mhttps://facebook.com/100093509571156
\033[1;34m ➯ Facebook Hoàng Nam : \033[1;37mhttps://facebook.com/nam.nhn131                              
\033[1;34m└═════════════════════════════════════════════════════════════════════════════┘
\033[1;34m ➯ Loại Tool: \033[1;37mTiện Ích Khác
\033[1;34m└═════════════════════════════════════════════════════════════════════════════┘
{do} ➩ {trang}Ngày{trang} : {vang}{ngay_hom_nay}{lam} |{trang} Tháng{trang}: {vang}{thang_nay} {lam}| {trang}Năm{trang}: {vang}{nam_}{lam} | {trang}Thời Gian: {vang}{time}
{do} ➩ {trang}Thành Phố : {vang}{city} {lam}|{trang} Khu Vực: {vang}{region} {lam}| {trang} Quốc gia: {vang}{country} {lam}| {trang} Tọa độ: {vang}{latitude}, {longitude} {lam}| {trang} Nhiệt độ: {vang}{weather_description}
"""
for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.00)
print("\033[1;34m⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦")
print("\033[1;35m╔════════════════════════════════════════════════════╗")
print("\033[1;35m║\033[1;31m[\033[1;33m</>\033[1;31m]\033[1;36m[1] \033[1;32mVÀO TOOL REG ACC GARENA                    \033[1;35m║ ")
print("\033[1;35m╚════════════════════════════════════════════════════╝")
print("\033[1;35m╔════════════════════════════════════════════════════╗")
print("\033[1;35m║\033[1;31m[\033[1;33m</>\033[1;31m]\033[1;36m[2] \033[1;32mVÀO TOOL CHAT GPT                          \033[1;35m║ ")
print("\033[1;35m╚════════════════════════════════════════════════════╝")
print("\033[1;35m╔════════════════════════════════════════════════════╗")
print("\033[1;35m║\033[1;31m[\033[1;33m</>\033[1;31m]\033[1;36m[3] \033[1;32mVÀO TOOL ĐẾM LẦN YÊU                       \033[1;35m║ ")
print("\033[1;35m╚════════════════════════════════════════════════════╝")
print("\033[1;35m╔════════════════════════════════════════════════════╗")
print("\033[1;35m║\033[1;31m[\033[1;33m</>\033[1;31m]\033[1;36m[4] \033[1;32mVÀO TOOL TỎ TÌNH CRUSH                     \033[1;35m║ ")
print("\033[1;35m╚════════════════════════════════════════════════════╝")
print("\033[1;35m╔════════════════════════════════════════════════════╗")
print("\033[1;35m║\033[1;31m[\033[1;33m</>\033[1;31m]\033[1;36m[5] \033[1;32mVÀO TOOL ĐẾM NGÀY TẾT                      \033[1;35m║ ")
print("\033[1;35m╚════════════════════════════════════════════════════╝")
print("\033[1;35m╔════════════════════════════════════════════════════╗")
print("\033[1;35m║\033[1;31m[\033[1;33m</>\033[1;31m]\033[1;36m[6] \033[1;32mVÀO TOOL BUFF MEMBER GROUP TELEGRAM        \033[1;35m║ ")
print("\033[1;35m╚════════════════════════════════════════════════════╝")
print("\033[1;35m╔════════════════════════════════════════════════════╗")
print("\033[1;35m║\033[1;31m[\033[1;33m</>\033[1;31m]\033[1;36m[7] \033[1;32mVÀO TOOL URL LINK GOOGLE                  \033[1;35m ║ ")
print("\033[1;35m╚════════════════════════════════════════════════════╝")
print("\033[1;35m╔════════════════════════════════════════════════════╗")
print("\033[1;35m║\033[1;31m[\033[1;33m</>\033[1;31m]\033[1;36m[8] \033[1;32mVÀO TOOL TẢI VIDEO YOUTUBE                 \033[1;35m║ ")
print("\033[1;35m╚════════════════════════════════════════════════════╝")
print("\033[1;35m╔════════════════════════════════════════════════════╗")
print("\033[1;35m║\033[1;31m[\033[1;33m</>\033[1;31m]\033[1;36m[9] \033[1;32mVÀO TOOL TẢI VIDEO TIKTOK                  \033[1;35m║ ")
print("\033[1;35m╚════════════════════════════════════════════════════╝")
print("\033[1;35m╔════════════════════════════════════════════════════╗")
print("\033[1;35m║\033[1;31m[\033[1;33m</>\033[1;31m]\033[1;36m[10] \033[1;32mVÀO TOOL TẠO SESSION                    \033[1;35m  ║ ")
print("\033[1;35m╚════════════════════════════════════════════════════╝")
print("\033[1;35m╔════════════════════════════════════════════════════╗")
print("\033[1;35m║\033[1;31m[\033[1;33m</>\033[1;31m]\033[1;36m[11] \033[1;32mVÀO TOOL SHARE KEY HMA FREE              \033[1;35m ║ ")
print("\033[1;35m╚════════════════════════════════════════════════════╝")
print("\033[1;35m╔════════════════════════════════════════════════════╗")
print("\033[1;35m║\033[1;31m[\033[1;33m</>\033[1;31m]\033[1;36m[12] \033[1;32mVÀO TOOL TẢI ẢNH H3NTAI                  \033[1;35m ║ ")
print("\033[1;35m╚════════════════════════════════════════════════════╝")
print("\033[1;35m╔════════════════════════════════════════════════════╗")
print("\033[1;35m║\033[1;31m[\033[1;33m</>\033[1;31m]\033[1;36m[13] \033[1;32mVÀO GAME CARO                            \033[1;35m ║ ")
print("\033[1;35m╚════════════════════════════════════════════════════╝")
print("\033[1;35m╔═══════════════════════════════════════╗")
print("\033[1;35m║ \033[1;31m[\033[1;33m</>\033[1;31m]\033[1;36m[0] \033[1;32mQUAY LẠI MENU TOOL          \033[1;35m ║ ")
print("\033[1;35m╚═══════════════════════════════════════╝")
print("\033[1;34m⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦")
chon = int(input('\033[1;33mnhn\033[1;95m@\033[1;36mNamDev$ '))
if chon == 1 :
	exec(requests.get('https://raw.githubusercontent.com/NamHoang1301/hnamtermuxtool/main/regacc.py').text)
elif chon == 2 :
	exec(requests.get('https://raw.githubusercontent.com/NamHoang1301/hnamtermuxtool/main/chatgpt.py').text)
elif chon == 3 :
	exec(requests.get('https://raw.githubusercontent.com/NamHoang1301/hnamtermuxtool/main/yeu.py').text)
elif chon == 4 :
	open_webpage(url2)
elif chon == 5 :
	open_webpage(web_url) 
elif chon == 6 :
	exec(requests.get('https://raw.githubusercontent.com/NamHoang1301/hnamtermuxtool/main/buffmemtele.py').text)
elif chon == 7 :
	exec(requests.get('https://raw.githubusercontent.com/NamHoang1301/hnamtermuxtool/main/urllink.py').text)
elif chon == 8 :
	exec(requests.get('https://raw.githubusercontent.com/NamHoang1301/hnamtermuxtool/main/vidytb.py').text)
elif chon == 9 :
	exec(requests.get('https://raw.githubusercontent.com/NamHoang1301/hnamtermuxtool/main/vidtiktok.py').text)
elif chon == 10 :
	exec(requests.get('https://raw.githubusercontent.com/NamHoang1301/hnamtermuxtool/main/taosession.py').text)
elif chon == 11 :
	exec(requests.get('https://raw.githubusercontent.com/NamHoang1301/hnamtermuxtool/main/keyhma.py').text)
elif chon == 12 :
	exec(requests.get('https://raw.githubusercontent.com/NamHoang1301/hnamtermuxtool/main/h3ntai.py').text)
elif chon == 13 :
	exec(requests.get('https://raw.githubusercontent.com/NamHoang1301/hnamtermuxtool/main/caro.py').text)
elif chon == 0 :
	exec(requests.get('https://raw.githubusercontent.com/NamHoang1301/hnamkeytermux/main/gop.py').text)
else :
    sys.exit('Vui Lòng Chọn Đúng Chế Độ')