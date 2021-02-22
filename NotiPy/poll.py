import NotiPy.db as db
import telegram
from termcolor import cprint
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters,ConversationHandler

ENTER_PWD=0

def register(update,context):
    update.message.reply_text("hello {} , Enter password".format(update.message.chat.first_name))
    return ENTER_PWD

def forget(update,context):
    db_obj=db.DB()
    db_obj.del_chat_id(update.message.chat.id)
    cprint("[*] Removed {}".format(update.message.chat.first_name),"yellow")
    update.message.reply_text("Unsubscribed successfully")

def msg_handler(update,context):
    update.message.reply_text("Invalid_message")

def check_pwd(update,context):
    db_obj=db.DB()
    if update.message.text==db_obj.get_pwd():
        db_obj.put_chat_id(update.message.chat.id)
        cprint("[*] Added {}".format(update.message.chat.first_name),"yellow")
        update.message.reply_text("Registered successfully")
    else:
        cprint("[*] Failed to add {}".format(update.message.chat.first_name),"yellow")
        update.message.reply_text("Failed registration.Try Again")
    return ConversationHandler.END


def main():
    db_obj=db.DB()
    try:
        updater=Updater(token=db_obj.get_api_key(),use_context=True)
        dp=updater.dispatcher

        conv_handler=ConversationHandler(entry_points=[CommandHandler("register",register)],
        states={
            ENTER_PWD:[MessageHandler(Filters.text,check_pwd)]
        },fallbacks=[]
        )

        dp.add_handler(conv_handler)
        dp.add_handler(CommandHandler("forget",forget))
        dp.add_handler(MessageHandler(Filters.text,msg_handler))
        cprint("[*] Started Polling","yellow")
        updater.start_polling()
        updater.idle()
    except telegram.error.InvalidToken as e:
            cprint("[!] Invalid API token","red")
    except telegram.error.Unauthorized as e:
            cprint("[!] Token Unauthorized.Try after requesting New Token","red")
    except telegram.error.Conflict as e:
            cprint("[!] Conflict: terminated by other getUpdates request; make sure that only one bot instance is running","red")
    except:
            cprint("[!] Some error occured","red")

main()