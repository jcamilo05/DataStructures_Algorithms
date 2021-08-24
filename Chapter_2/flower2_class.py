class Flower:
    def __init__(self, name="Flower", petals=0, price=0):
        self._name = name
        self._petals = petals
        self._price = price

    @property  # getter
    def name(self):
        print('calling getter')
        return self._name

    @property  # getter
    def petals(self):
        return self._petals

    @property  # getter
    def price(self):
        return self._price

    @name.setter
    def name(self, n):
        print('calling setter')
        self._name = n

    @petals.setter
    def petals(self, num):
        self._petals = num

    @price.setter
    def price(self, value):
        self._price = value

    def __str__(self):
        return f'''Default name: {self._name}
               Default number of Petals: {self._petals}
               Default cost: {self._price}'''

    def __repr__(self):
        return "%s, %s, %d, %d" % (self.__class__.__name__, self.name,
                self.petals, self.price)

tito = Flower()
print(tito)
tito.price = 64
tito.name = "Tito"
tito.petals = 8
print(tito)

