from mainframelib.classes.controllerClass import *
from mainframelib.decorator import *

class controller(controllerClass):
  def defaultAction(self):
    
    self.tmpl.decorator=decorator('href')
    self.tmpl.setVarDSingle('var',{'text':'wp','href':'http://wp.pl'})
    
  
  def prepare(self):
    self.startAction()