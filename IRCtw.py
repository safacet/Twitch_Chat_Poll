import socket
from Database import ChatPoll
from threading import Thread
from TwUI import Ui_TabWidget

class IRCclient(Thread):
    def __init__(self, window, channel):
        Thread.__init__(self)
        self.window = window

        self.ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server = "irc.chat.twitch.tv" # Server
        port = 6667
        self.ircsock.connect((server, port))
        self.send("PASS Your_Oauth_Password")
        self.send("NICK Your_Twitch_Nick")
        self.connect(channel)
        
        
    
    
    def send(self, message):
        self.ircsock.send(bytes(message + "\r\n", "UTF-8"))



    def connect(self, channel):
        self.send("JOIN #" + channel)
        while True:
            buffer = self.ircsock.recv(1024).decode("UTF-8")
            msg = buffer.split("\r\n")
            msg.pop()
            count = 0
            for i in msg:
                parted = i.split(":")
                parted.pop(0)
                if len(parted) > 1:
                    if parted[1] == "End of /NAMES list":
                        self.joinControl = True
                        return
                    else:
                        count += 1
                        if count > 1000:
                            self.joinControl = False
                            return
    def quit(self):
        self.ircsock.close()
        
    def run(self):
        self.chatpoll = ChatPoll()
        self.chatpoll.connect()
        while True:
            buffer = self.ircsock.recv(1024).decode("UTF-8")
            msg = buffer.split("\r\n")
            if msg != '':
                for i in msg:
                    if "PING" in i:
                        self.send("PONG :tmi.twitch.tv")
                    elif "PRIVMSG" in i:
                        part = i.split(":")
                        usernameparts = part[1].split("!")
                        username = usernameparts[0]
                        message = part[2]
                        keyword = self.window.keyword
                        if keyword in message:
                            self.chatpoll.control(message, username)
                            result = self.results()
                            if result != None:
                                self.window.rslt = str()
                                self.window.results_browser.append("*****************************")
                                for i in result:
                                    self.window.results_browser.append(i[0] + " --> " + str(i[2]))
                            self.window.rslt = result   
                            

                    
    
    def results(self):
        result = self.chatpoll.select()
        return result



    
