"""
Write a set of Python classes that can simulate an
Internet application in which one party, Alice, is
periodically creating a set of packets that she wants to
send to Bob. An Internet process is continually checking
if Alice has any packets to send, and if so, it delivers
them to Bob's computer, and Bob is periodically
checking if his computer has a packet from Alice, and, if
so, he reads and deletes it.
"""
class User:
    """
    This class receive as paremeter a username, ip address and a email to create 
    a user
    """
    def __init__(self, username="None", ipaddress="None", email_adr="None"):
        self._name = username
        self._ipaddr = ipaddress
        self._email = email_adr

    @property            #getter
    def name(self):
        return self._name

    @property            #getter
    def ipaddr(self):
        return self._ipaddr

    @property            #getter
    def email(self):
        return self._email

    @name.setter
    def name(self, uname):
        self._name = uname

    @ipaddr.setter
    def ipaddr(self, newIP):
        self._ipaddr = newIP

    @email.setter
    def email(self, newEmail):
        self._email = newEmail

    def __str__(self):
        return f"User_name: {self._name}, IP address: {self._ipaddr}, email: {self._email}"

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.ipaddr, self.email)

class Deliver:
    
    """
        This Class take as a parameter a user which is a object created with User class
        and return a delivered message to another user object that must be given as a 
        parameter in send method.

        Example:
        -----------------------------------------------------
            tito = User('Tito', '192.567.32' ,'tito@cat.com')
            jiji = User('Jiji', '97.322.345', 'jiji@cat.com')
            instance1 = Deliver(tito)
            packet = 'Hello how are you'
       Output 
            >> Tito sent -- Hello how are you -- to jiji 
    """
    def __init__(self,user):
         self.name= user.name
         self.ipaddr= user.ipaddr
         self.email= user.email

    def send(self, packet, user2):
        print(f'{self.name} sent -- {packet} -- to {user2.name}')

tito = User('Tito', '192.567.32' ,'tito@cat.com')
jiji = User('Jiji', '97.322.345', 'jiji@cat.com')
instance1 = Deliver(tito)
packet = 'Hello how are you'
instance1.send(packet, jiji)
