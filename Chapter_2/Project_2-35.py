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
    def __init__(self, username="None", ipaddress="None", email="None"):
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
    def email_adr(self):
        return self._email

    @name.setter
    def name(self, uname):
        self._username = uname

    @ip_adr.setter
    def ip_adr(self, newIP):
        if not isinstance(newIP, int):
            self._ipaddress = newIP
        else:
            self._ipaddress = 0

    @email_adr.setter
    def email_adr(self, newEmail):
        self._email = newEmail

    def __str__(self):
        return f"User_name: {self._username} {self.username}, IP address {self._ipaddress} {self.ipaddress}, email {self._email} {self.email}"

    def __repr__(self):
        return "%s, %s, %s" % (self.username, self.ipaddress, self.email)

class GenPackets(Packets):  

    # To review later
    #@Packets.name.setter
    #@Packets.email.setter
    #@Packets.ip_adr.setter 
    #def overall_setter(self, names, emails, ips):
    #    #TODO unpack with zip(*data)
    #    Packets.name.fset(self, names)
    #    Packets.email.fset(self, emails)
    #    Packets.ip_adr.fset(self, ips)
    def unpack_data(self, *data):
        counter = 0
        self.username = tuple(zip(*data))[0][0]
        self.email = tuple(zip(*data))[1][0]
        self.ipaddress = tuple(zip(*data))[2][0]
        #for i in zip(*data):
        #    print(i[0])
        #    self.username = i[0][0]
        #    self.email = i[0][0]
        #    self.ipaddress = i[0][0]
        #    print(i[0][0])
    #        break

#TODO: Create class for bob to delete or read packets
test = Packets()
test.username = 'test'
test.email = 'test'
#test.ipaddress = 'test'
test.ipaddress = 503223
print(test)
Alice = GenPackets()
#Alice.unpack_data([("jiji", "tito"), ("jiji@cats.com", "tito@cats.com"), ("182.784.986", "00000")])
Alice.unpack_data([("jiji", "tito"), ("jiji@cats.com", "tito@cats.com"), ("182.784.986", "00000")])
print(Alice)
Alice.unpack_data([("jiji", "XXXXX"), ("jiji@cats.com", "XX@cats.com"), ("182.784.986", "XXX")])
print(Alice)
Alice.unpack_data([("jiji", "tito"), ("jiji@cats.com", "tito@cats.com"), ("182.784.986", "00000")])
print(Alice)
