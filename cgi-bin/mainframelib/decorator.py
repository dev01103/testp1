from mainframelib.template import *
from mainframelib.mainframe import *

class decorator(template):
   def __init__(self,name):
     super(decorator,self).__init__('')
     mf=mainframe.getMe()
     self.path='templates/'+mf.getTemplate()+'/decorators/'
     self.getFile(name+'.tpl')
   
   
     
    
   
     