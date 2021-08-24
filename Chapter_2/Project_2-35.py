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
#TODO: Test setters and getters
class Packets:
    def __init__(self, username="None", ipaddress="None", email_adr="None"):
        self._name = username
        self._ipaddr = ipaddress
        self._email = email_adr

    @property
    def name(self):
        print("calling name getter")
        return self._name

    @property
    def ipaddr(self):
        print("calling ipaddr getter")
        return self._ipaddr

    @property
    def email(self):
        print("calling email getter")
        return self._email

    @name.setter
    def name(self, uname):
        print("calling name setter")
        self._name = uname

    @ipaddr.setter
    def ipaddr(self, newIP):
        print("calling ipadr setter")
        if not isinstance(newIP, int):
            self._ipaddr = newIP
        else:
            self._ipaddr = 0

    @email.setter
    def email(self, newEmail):
        print("calling email setter")
        self._email = newEmail

    def __str__(self):
        return f"User_name: {self._name}, IP address: {self._ipaddr}, email: {self._email}"

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.ipaddr, self.email)

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
        self.name = tuple(zip(*data))[0][0]
        self.email = tuple(zip(*data))[1][0]
        self.ipaddr = tuple(zip(*data))[2][0]
        #for i in zip(*data):
        #    print(i[0])
        #    self.username = i[0][0]
        #    self.email = i[0][0]
        #    self.ipaddress = i[0][0]
        #    print(i[0][0])
    #        break

#TODO: Create class for bob to delete or read packets
Alice = GenPackets()
#Alice.unpack_data([("jiji", "tito"), ("jiji@cats.com", "tito@cats.com"), ("182.784.986", "00000")])
Alice.unpack_data([("jiji", "tito"), ("jiji@cats.com", "tito@cats.com"), ("182.784.986", "00000")])
print(Alice)
#Alice.unpack_data([("jiji", "XXXXX"), ("jiji@cats.com", "XX@cats.com"), ("182.784.986", "XXX")])
#print(Alice)
#Alice.unpack_data([("jiji", "tito"), ("jiji@cats.com", "tito@cats.com"), ("182.784.986", "00000")])
#print(Alice)
