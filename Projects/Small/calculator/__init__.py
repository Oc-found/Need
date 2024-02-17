from ver import ver
from run import run
print(f"Calculator v{ver}")

while 1:
  #If not int()
  try:
    a = int(input("First Number: "))
    b = int(input("Second Number: "))
  except:
    pass
  c = input("+ - * / : ")
  #########
  d = run(a,b,c)
  print(d.runner())
  
