class StarSystem:
    def __init__(self, planets, name):
        self.planets = list(planets)
        self.name = name
        
    def __sub__(self, other):
        planets_1 = self.planets.copy()
        planets_1.remove(other)
        return StarSystem(planets_1, self.name)
    
  # def __rsub__ (self, other):
  #      print (' radd ', self.val, other)
    #    return other - self.val
        
   # def __isub__(self, other):
    #    self.planets.remove(other)
    #    return self
      
      
system = StarSystem(['planet1', 'planet2', 'planet3'], 'StarSystem1')
system = system - 'planet2'
system.planets
print (system.planets)

