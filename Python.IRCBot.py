'''
By FredHappyface (2019/03/08)
Use sockets to attempt to join an irc channel and talk with a bot
'''

'''
Constants
'''
# Run the program in 'debug' mode (print statements provide a running commentary
DEBUG = False
# Number of messages sent when you sign in (registered) (for root-me the value is 3)
INTRO_MSGS = 3
# Additional messages sent when you are not registered (for root-me the value is 2)
NOT_REG_MSGS = 2

'''
Read from a json file. The file in question is going to be simple. In the form: 
{
"host_url":
"protocol":
"port":
"irc_channel":
"bot_name":
"user_name":
"user_password":
}
'''

import json
with open("data.json") as json_file:
    data = json.load(json_file)
    host_url = data["host_url"]
    protocol = data["protocol"]
    port = data["port"]
    irc_channel = data["irc_channel"]
    bot_name = data["bot_name"]
    user_name = data["user_name"]
    user_password = data["user_password"]

if (DEBUG):
    print('host_url: ' + host_url)
    print('protocol: ' + protocol)
    print('port: ' + str(port))
    print('irc_channel: ' + irc_channel)
    print('bot_name: ' + bot_name)
    print('user_name: ' + user_name)


'''
Gets a message in its raw from
'''
def getRawMessage():
    ircmsg = irc.recv(2048).decode("UTF-8")
    ircmsg = ircmsg.strip('\n\r')
    return ircmsg

'''
Takes a raw message and refines it 
'''
def getRefinedMessage(messageData):
    if messageData.find("PRIVMSG") != -1:
        name = messageData.split('!',1)[0][1:]
        message = messageData.split('PRIVMSG',1)[1].split(':',1)[1]
        return name, message
    else:
        '''
        This is an error, you will need to test for this in case you are expecting
        a string
        '''
        return -1, -1


'''
Now start the IRC connection, sign in and go to the desired channel and ignore the
intro messages 
'''

import socket

# Set up the connection 
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if (DEBUG):
    print ("Connecting to " + host_url + " on port " + str(port))
irc.connect((host_url, port))

# Fill in a form with the user name as all fields and set the nickname of our bot 
if (DEBUG):
    print ("Logging in as " + user_name)
irc.send(bytes("USER "+ user_name +" "+ user_name +" "+ user_name + " " + user_name
               + "\n", "UTF-8")) 
irc.send(bytes("NICK "+ user_name +"\n", "UTF-8"))

# Join an irc channel
if (DEBUG):
    print ("Joining channel " + irc_channel)
irc.send(bytes("JOIN "+ irc_channel +"\n", "UTF-8")) 
 
# Cycle through the intro messages and (if debugging) print them 
for introMessage in range(INTRO_MSGS + NOT_REG_MSGS):
    rawMessage = getRawMessage()
    if (DEBUG):
        print(rawMessage)


'''

Application code here. From this point, you can add code to talk to the target bot
deal with any responses and deal with them appropriately. For instance you may want
to implement a 'chatbot' or answer challenge questions (in the case of root-me)

'''

'''
Examples 
'''

# send a private message to our target bot
irc.send(bytes("PRIVMSG "+ bot_name +" :"+ "my message here" +"\n", "UTF-8")) 


# Get a message from the bot 
messageData = getRawMessage()
if (DEBUG):
    print(messageData)
name, message = getRefinedMessage(messageData)
print(name, message)


