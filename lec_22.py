class OrganicSells:
    def __init__(self, volume = 10, energy = 100):
        self.volume = volume
        self.energy = energy

    def __mul__ (self, other):
      volume_new = self.volume * other
      return OrganicSells()

    def __add__ (self, other):
      volume_new = self.volume + other
      return OrganicSells()

    def __sub__ (self, other):
      volume_new = self.volume - other
      return OrganicSells() 

    def __truediv__ (self, other):
      volume_new = self.volume * self.volume
      return OrganicSells()
  



