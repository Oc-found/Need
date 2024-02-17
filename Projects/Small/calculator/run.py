
def _and(a,b):
  return a+b
def _els(a,b):
  # If a and b not the int()...
  try:
    return a-b
  except:
    return "NumBer!"
def _c(a,b):
  #The 5th line, too.
  try:
    return a*b
  except:
    return "number!"
def c_(a,b):
  #too...
  try:
    return a/b
  except:
    return "Must Number!"

class run:
  def __init__(self, a,b,c):
    self.a = a
    self.b = b
    self.c = c


  def runner(self):
    if self.c == "+":
      _and(self.a,self.b)
    if self.c == "-":
      _els(self.a,self.b)
    if self.c == "*":
      _c(self.a,self.b)
    if self.c == "/":
      c_(self.a,self.b)
