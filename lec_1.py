class DictD(dict):
  def __init__(self,*k,**kw):
    self.__dict = dict(*k, **kw)
  def __setitem__(self, key, value):
    self.__dict.__setitem__(key,value)
  def __getitem__(self, item):
    if item in self.__dict:
      return self.__dict[item] 
    else:
      return """"
      Something has left my life
      And I dont know where it went to
      Somebody caused me strife
      And its not what I was seeking
      Didnt you see me? Didnt you hear me?
      Didnt you see me standing there?
      Why did you turn out the lights?
      Did you know that I was sleeping?
      Say a prayer for me
      Help me to feel the strength I did
      My identity, has it been taken?
      Is my heart breaking on me?
      All my plans fell through my hand
      They fell through my hands on me
      All my dreams, it suddenly seems
      It suddenly seems empty
      Empty
      Empty
      Empty
      Empty
      Empty
      Empty
      """
    
def main():
  d = DictD({'key':77})
  print(d['77'])


if __name__ == '__main__':
  main()