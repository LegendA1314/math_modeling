import random
states = ['отсутствует', 'цветение', 'опыление', 'зеленый', 'красный']

TOMATO_RIPED = 0
TOMATO_READY = len(states)-1


class WrongTomatoState(Exception):
  pass


def get_state_str(state):
  if state > 0 and state <= TOMATO_READY:
    return states[state]
  else:
    raise WrongTomatoState

spra = 'садоводство это весело и прикольно, садишь томаты, балдеешь на свежем воздухе, сказка!!!'


class Tomato:
  start_index = 0
  def  __init__(self):
    self.index = Tomato.start_index
    self.state = 1
    Tomato.start_index+=1
  def grow(self):
    print(self,' > ', end='')
    if self.state < TOMATO_READY:
      self.state += random.randint(0, 1)
    print(self)
  def is_ripe(self):
    return (self.state == TOMATO_READY)
  def __str__(self):
    return f'{self.__class__.__name__}, idx:{self.index}, state:{self.state}'
      

class TomatoBush:
  def  __init__(self, tomatos_count: int):
    self.tomatos = []
    for _ in range(tomatos_count):
      self.tomatos.append(Tomato())
  def grow_all(self):
    for tomato in self.tomatos:
      tomato.grow()
  def all_are_ripe(self):
    for tomato in self.tomatos:
      if not tomato.is_ripe():
        return False
    return True
  def give_away_all(self):
    if self.all_are_ripe():
      self.tomatos.clear()
    

class Gardener:
  def  __init__(self, name: str, bush: TomatoBush):
    self.name = name
    self.bush = bush
  def work(self):
    self.bush.grow_all()
  def harvest(self):
    if self.bush.all_are_ripe():
      self.bush.give_away_all()
      print('дело сделано')
  def knowledge_base(self):
    print(spra)

# ------------------------------------------

b = TomatoBush(15)
g = Gardener("Bob", b)
iter = 0

print(b.all_are_ripe())

while not b.all_are_ripe():
  print(f'Iteration: {iter}')
  g.work()
  g.harvest()
  iter+=1
  print()


print('The end')