# Python.IRCBot
Use sockets to attempt to join an IRC channel and talk with a bot

# Language information 
## Built for
This program has been written for Python 3 and has been tested with 
Python version 3.4.3 https://www.python.org/downloads/release/python-343/ 
on a Windows 10 PC. 
## Other versions
To install Python, go to https://www.python.org/ and download the latest version. 
# How to run
1. Download or clone this GitHub repository 
2. (If downloaded) Extract the zip archive
3. Open the .py file in IDLE
4. Run by pressing F5 or by selecting Run> Run Module

# What does this program do for you? 
- Read configuration data from a json file ('data.json'). In the form: 
```json
{
"host_url": "irc.hostname.org",
"protocol": "IRC",
"port": 6667,
"irc_channel": "#channel",
"bot_name": "bot_name",
"user_name": "user_name",
"user_password": "user_password"
}
```
- Gets a message in its raw from
```python
getRawMessage()
```
- Takes a raw message and refines it (name, message)
```python
getRefinedMessage(messageData)
```
- Starts an IRC connection, signs in and goes to the desired channel
- Ignore the welcome messages 


# Add your own application code 
You can add code to talk to the target bot
deal with any responses and deal with them appropriately. For instance you may want
to implement a 'chatbot' or answer challenge questions (in the case of root-me)

# Example code

Send a private message to our target bot
```python
irc.send(bytes("PRIVMSG "+ bot_name +" :"+ "my message here" +"\n", "UTF-8")) 
```


Get a message from the bot 
```python
messageData = getRawMessage()
if (DEBUG):
    print(messageData)
name, message = getRefinedMessage(messageData)
print(name, message)
```


