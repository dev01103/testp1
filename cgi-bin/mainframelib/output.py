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
   	self.ct="text/plain" 
   	self.buffer=""
   	self.s='200 OK'
  
  def contentType(self,ct):
  	self.ct=ct
  	
  def status(self,code):
  	self.s=code
  	
  def o(self,c):
    self.buffer=self.buffer+c	
  
  def lockPrint(self):
   #sys.stdout=self.block
   pass
  def unlockPrint(self):
    sys.stdout=self.out
  def o(self,todo):
  	self.buffer=self.buffer+todo
  	def getBuffer(self):
		return self.buffer  
  
  
  def code(self,delimiters):
   pass  
  #def html(self):
    