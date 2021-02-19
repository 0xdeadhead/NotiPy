from NotiPy.db import DB
import os
from termcolor import colored,cprint

def get_api():
    api_key=str(input(colored("[+] Enter api_key : ","cyan")))
    return api_key

def configure(api="",pwd=""):
    db_obj=DB()
    db_obj.set_pwd(pwd) if pwd else None
    db_obj.set_api(api) if api else None

def pass_confirmation():
   while True:
            pwd1=str(input(colored("[+] Enter pass : ","cyan")))
            pwd2=str(input(colored("[+] Confirm pass : ","cyan")))
            if pwd1==pwd2:
                return pwd1
            else:
                cprint("[!] Passwords dont match.Try again","red")


if os.path.exists("{}/Tbot.db".format(os.environ["HOME"])):
    if str(input(colored("[!] Configuration already exists.Do you want to overwrite[y/N]? : ","red")))=="y":
        cprint("[*] Set password","yellow")
        configure(pwd=pass_confirmation())
        cprint("[*] Set api_key","yellow")
        configure(api=get_api())
    else:
        cprint("[*] No changes made","blue")
else:
    configure(pwd=pass_confirmation())
    configure(api=get_api())