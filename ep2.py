             
import sys
import base64
import irc.client
 

class RetourAuCollege(irc.client.SimpleIRCClient):
 
    def __init__(self, server, nick, bot, port=6667):

        irc.client.SimpleIRCClient.__init__(self)
        self.bot = bot
        self.tic = 0
        self.connect(server, port, nick)
 
    def on_welcome(self, connection, event):

        print("Connection success")
        connection.privmsg(self.bot, "!ep2")
 
    def on_privmsg(self, connection, event):

        print()
        print("From " + str(event.source) + "to " + str(event.target) + "with arguments " + str(event.arguments)) 
        message = event.arguments[0]
        print("Message received:", message)
 
        if self.tic == 0:
            # Challenge

            decode =  str(base64.b64decode(message))
            res = "!ep2 -rep " + decode[2:len(decode)-1]
            connection.privmsg(self.bot, res)
            self.tic += 1

        else:
            sys.exit(0)
 

def main():

    server = 'irc.root-me.org'
    port = 6667
    nick = 'RootMe-ArcturusBot'
    bot = 'Candy'
 
    c = RetourAuCollege(server, nick, bot, port)
    c.start()
 
if __name__ == "__main__":
    print()
    main()
