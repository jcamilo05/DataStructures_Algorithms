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
# packet --> user_name - ip_address - email
class Packets:
    def __int__(self, username="None", ipaddress="None", email="None"):
        self._username = username
        self._ipaddress = ipaddress
        self._email = email

    @property
    def name(self):
        return self._username

    @property
    def ip_adr(self):
        return self._ipaddress

    @property
    def email(self):
        return self._email

    @name.setter
    def name(self, uname):
        self._username = uname

    @ip_adr.setter
    def ip_adr(self, newIP):
        self._ipaddress = newIP

    @email.setter
    def email(self, newEmail):
        self._email = newEmail

    def __str__(self):
        #return f"User_name: {self._username} {self.username}, IP address {self._ipaddress} {self.ipaddress}, email {self._email} {self.email}"
        #return f"User: {self._username}, IP address {self._ipaddress}, email {self._email}"
        return f"User: {self.username}, IP address {self.ipaddress}, email {self.email}"

    #def __repr__(self):
    #    return "%s, %s, %s" % (self.username, self.ipaddress, self.email)

class GenPackets(Packets):
    def __init__(self):
        super().__init__(self)
tito = Packets()
tito.username = "TITO"
tito.ipaddress = "182.784.986"
tito.email = "tito@cats.com"
print(tito)
