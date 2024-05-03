class Fruit:
    def __init__(self):
        self.has_pulp = False

    def squeeze(self):
        return self.has_pulp

class Orange(Fruit):
    def __init__(self):
        self.has_pulp = True
    # has_pulp = True

    def squeeze(self):
        return self.has_pulp

a=Orange()
print(a.squeeze())