import smtplib
from email.MIMEMultipart import MIMEMultipart

class Mail:
    """isang class para sa email"""

    def __init__(self, server='smtp.gmail.com', port=587,**keywords):
        self.setServer(server)
        self.setPort(port)
        for key in keywords:
            if key == 'username':
                self.setUser(keywords[key])
            elif key == 'password':
                self.setPassword(keywords[key])
            elif key == 'email':
                self.setEmail(keywords[key])
            elif key == 'to':
                self.setRecipient(keywords[key])
            elif key == 'message':
                self.setMessage(keywords[key])
        print 'mailman module'

    ### SETTERS ###

    def setUser(self, username):
        self.__username = username

    def setPassword(self, password):
        self.__password = password

    def setServer(self, server='smtp.gmail.com'):
        self.smtp_server = server

    def setPort(self, port=587):
        self.smtp_port = port

    def setEmail(self, email):
        self.email = email

    def setRecipient(self, recipient):
        self.recipient = recipient

    def setMessage(self, message):
        self.message = message

    def setSMTP(self):
        self.SMTP = smtplib.SMTP(self.getServer(), self.getPort())
        self.SMTP.ehlo()
        self.SMTP.starttls()
        self.SMTP.ehlo()
        self.SMTP.login(self.getUser(), self.getPassword())
        self.SMTP.sendmail(self.getEmail(), self.getRecipient(), self.getMessage())
        print 'MESSAGE SENT'
        self.SMTP.close()
        
    ### GETTERS ###
        
    def getUser(self):
        return self.__username

    def getPassword(self):
        return self.__password

    def getServer(self):
        return self.smtp_server

    def getPort(self):
        return self.smtp_port

    def getEmail(self):
        return self.email

    def getRecipient(self):
        return self.recipient

    def getMessage(self):
        return self.message


