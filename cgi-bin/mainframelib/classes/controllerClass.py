import cgitb
import cgi



class controllerClass(object):
  def __init__(self):
    self.params=cgi.FieldStorage()
    self.view=''
  
  def setModel(self,m):
    self.model=m
  
  def parseRequest(self):
   if self.params.getvalue('view')<>None:
      self.view=self.params.getvalue('view')
   else:
       self.view='main'
      
    
  def proceed(self,tl):
    print tl.parse(self.view+'.tpl')
    
    
  
  
  def redirect(self):
    pass