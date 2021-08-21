class Flower(object):
    def __init__(self, name="Flower", petals=0, price=0):
        self._name = name
        self._petals = petals
        self._price = price    

    @property  # getter
    def flower_name(self):
        return self._name

    @property  # getter
    def num_petals(self):
        return self._petals
    
    @property  # getter
    def num_petals(self):
        return self._petals

    @property  # getter
    def cost(self):
        return self._price

    @flower_name.setter
    def flower_name(self, n):        
        self._name = n 

    @num_petals.setter
    def num_petals(self, num):
        self._petals = num
    
    @cost.setter
    def cost(self, value):
        self._price = value

    def __str__(self):
        return f"Default name: {self._name}\nNew name: {self.name}\nDefault number of Petals: {self._petals}\nNumber of Petals: {self.petals}\nDefault cost: {self._price}\nCost {self.price}"         

    def __repr__(self):
        #return "%s, %s, %d, %d" % (self.__class__.__name__, self.name, self.petals, self.price)  # errors with eval because there's variables not defined before
        #return "%s, tito.name, %d, %d" % (self.__class__.__name__, self.petals, self.price) 
        return "%s, %d, %d" % (self.__class__.__name__, self.petals, self.price) 
    
    
tito = Flower()
tito.price = 64
tito.name = "Tito"
tito.petals = 8
print(tito)
