import sys

class outputBlocker:
  def write(self,arg):
    pass

class output:
  me=None
  @staticmethod 
  def getMe():
   if output.me==None:
     output.me=output()
   return output.me
  
  def __init__(self):
    self.out=sys.stdout
    self.block=outputBlocker()
    self.lockPrint()
  
  def lockPrint(self):
    sys.stdout=self.block
  def unlockPrint(self):
    sys.stdout=self.out
  def o(self,todo):
    self.unlockPrint()
    print(todo)
    self.lockPrint()
    
  def code(self,delimiters):
   pass  
  #def html(self):
    