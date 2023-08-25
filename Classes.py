class Person:
    def __init__(self, *features):
        self.features = features[:10]  # Limit features to the first 10
        # self.num_features = len(self.features)

    def __str__(self):
        return ', '.join(str(feature) for feature in self.features if feature is not None)


Person1 = Person("22", 5)
print(Person1.features[1])
