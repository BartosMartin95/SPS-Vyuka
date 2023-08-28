class Person:
    def __init__(self, *features):
        self.features = features[:10]  # Limit features to the first 10
        self.num_features = len(self.features)

    def __str__(self):
        return str(self.features)


Person1 = Person("22", 5)
print(Person1)

# Parent/Child inheritance


class Child(Person):
    def __int__(self, *features, plays):
        Person.__init__(self, *features)
        self.plays = plays
    def __str__(self):
        return "help"

Child1 = Child(5, 5)
Child1.plays = 20
print(Child1.plays)

