# Prerequisites :
This tool requires python3, pip3 to be installed in the system.
<br><br><br>

# Installation : 
Type these below commands in the terminal:
<br>
```git clone https://github.com/da3m0n-28/NotiPy.git```
<br>
```cd NotiPy```
<br>
```pip3 install .```
<br><br><br>

# Configuring the tool :
We need a Telgram Bot API token for which the tool sends the Notification<br>
You can read more about [How to create a Telegram bot here.](https://core.telegram.org/bots#6-botfather)
<br>
After acquiring Bot API Token,We need to configure our tool to use the token by typing below commands.<br>
```NotiPy -C```
<br>
Now create a password and enter the API Token.
<br>
## Registering a device to recieve Notification :
Start Notifier with ```-P``` flag.<br>
Go to bot's chat and send  " ```/register``` " ,Upon correct password entry the device will be registered for notifications.
<br>

## Removing the device :
send "```/forget```" to the chat to unsub from notifications.
<br><br><br>

# Usage : 
Specify the message to send with "```-M```"  flag<br>

```$ sleep 10 ; NotiPy -M "Process Completed"```.<br>

Send different Messages according to return status from previous Command<br>

```$ Commandwhichdoesnotexist && NotiPy -M "Process ran Sucessfully" || NotiPy -M "Failed" ```<br><br><br>
# Uninstalling NotiPy:
```$ pip3 uninstall NotiPy```





