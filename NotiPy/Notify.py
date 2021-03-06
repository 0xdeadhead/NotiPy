#!/usr/bin/env python3
from argparse import ArgumentParser
from termcolor import cprint
from telegram import Bot
from NotiPy.db import DB
from art import text2art
import telegram
import sys

def main():
        parser=ArgumentParser()
        parser.add_argument("-C","--configure",action="store_true",help="Configure api_key and pwd")
        parser.add_argument("-S","--silent",action="store_true",help="Dont show banner")
        parser.add_argument("-P","--poll",action="store_true",help="start poll for registering/removing users")
        parser.add_argument("-M","--message",help="Message to send")
        args=parser.parse_args()


        if not args.silent:
                cprint(text2art("Notifier"),"red",file=sys.stderr)
        if not len(sys.argv)>1:
                parser.print_help()
        if args.poll:
                import NotiPy.poll
        if args.configure:
                import NotiPy.configure
        if args.message:
                db_obj=DB()
                try:
                        bot=Bot(token=db_obj.get_api_key())
                        chat_ids=db_obj.get_chat_ids()
                        for chat_id in chat_ids:
                                if args.message:
                                        bot.send_message(chat_id=chat_id,text=args.message)
                except telegram.error.InvalidToken as e:
                        cprint("[!] Invalid API token","red")
                except telegram.error.Unauthorized as e:
                        cprint("[!] Token Unauthorized.Try after requesting New Token","red")
                except:
                        cprint("[!] Some error occured","red")

if __name__=="__main__":
        main()