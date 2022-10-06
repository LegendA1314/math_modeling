class Alphabet:
  def __init__ (self, lang_0, qu_0):
    self.lang = lang_0
    self.qu = qu_0
  def pr_all (self, qu_0):
    print(qu_0)
  def coutn_all (self, qu_0):
    count = len(qu_0)
    print(count)
  
lang_1 = [1,2,3,4,5,6,7,8,9,0]
lang_2 = ['f', 'g', 'd', 'a']

a = Alphabet(1, lang_1)
a.pr_all(lang_1)
a.coutn_all(lang_1)
a.pr_all(lang_2)
a.coutn_all(lang_2)

