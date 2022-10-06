states = ['отсутствует', 'цветение', 'зеленый', 'красный']
index = 0
kol = 5

spra = 'садоводство это весело и прикольно, садишь томаты, балдеешь на свежем воздухе, сказка!!!'
class Tomato:
  def  __init__(self):
    self.state = 1
  def grow(self):
    if self.state < len(states)-1:
      self.state += 1
  def is_ripe(self):
    if state == len(states)-1:
      return True
      

      
class TomatoBush:
  def  __init__(self, tomatos_0):
    self.tomatos = []
    for i in kol:
      self.tomatos.append(Tomato())
  def grow_all(self):
    for tomato in self.tomatos:
      tomato.grow()
  def all_are_ripe(self):
    for tomato in self.tomatos:
      if tomato.is_ripe:
        continue
      else:
        break
      return True
  def give_away_all(self):
    if all_are_ripe():
      self.tomatos.clear()
    

class Gardener:
  def  __init__(self, name_0, plant):
    self.name = name_0
    self.palnt = TomatoBush
  def work(self):
    TomatoBush.grow_all()
  def harvest(self):
    if TomatoBush.all_are_ripe():
      TomatoBush.give_away_all()
  def knowledge_base(self):
    print(spra)
    


    