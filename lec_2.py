class Man:
  def __init__ (self, default_name, default_age, _security_money, _security_appart):
    self.default_name = default_name
    self.default_age = default_age
    self._security_money = _security_money
    self._security_appart = _security_appart
    
  def info(self):
    print(default_name, default_age, _security_money, _security_appart)
    return
    
  def make_deal(self,  money_lost):
    self._security_money = self._security_money - money_lost 
    self._security_appart += 1
    
  def earn_money(self):
    self._security_money = self._security_money + 60000
    return self._security_money
    
  def buy_house(self, h):
    if self._security_money >= h.final_price():
      m.make_deal(h.final_price())
      print('sdelke but')
    else:
      print('net deneg')
      m.earn_money()

class House:
  def __init__(self, _area, _price):
    self._area = _area
    self._price = _price 

  def final_price (self):
    return self._price * 0.9

class SmallHouse(House):
  def __init__(self, _area, _price):
    super().__init__(_area, _price)

m = Man('jack', 21, 60000, 0)
h1 = House(40, 300000)
h = SmallHouse(40, 300000)
for _ in range(10):
  m.buy_house(h)

