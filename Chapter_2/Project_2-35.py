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
import pandas as pd
class Packets:
    def __init__(self, username="None", ipaddress="None", email_adr="None"):
        self._name = username
        self._ipaddr = ipaddress
        self._email = email_adr

    @property
    def name(self):
        return self._name

    @property
    def ipaddr(self):
        return self._ipaddr

    @property
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

class GenPackets(Packets):  

    def unpack_data(self, data):
        for k in data.keys():
            self.name = data[k][0]
            self.email = data[k][1]
            self.ipaddr = data[k][2] 
            self.data_frame = pd.DataFrame(data, index=['name','email', 'Ip'])
        print(self.data_frame)

#TODO: Create class for bob to delete or read packets
def custom_input():  # TODO: Add logic to only accept ints in the input
    """
    Void function that takes users input  to fill out username, email,
    and ip address related data
    :returns: All users in a dictionary
    """
    num_packets = int(input("Please state how many packets do you want to generate: "))
    total_users = num_packets
    all_users = dict()
    while num_packets > 0:
        username = input("Please write down a username: ")
        email = input("Please write down an email: ")
        ipaddress = input("Please write down an ip address: ")
        *packet_elements, = username, email, ipaddress
        all_users.setdefault(f"User{(total_users + 1) - num_packets}", tuple(packet_elements))
        num_packets -= 1
    return all_users

Alice = GenPackets()
Alice.unpack_data(custom_input())
