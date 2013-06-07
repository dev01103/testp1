from mainframelib.classes.controllerClass import *
from mainframelib.decorator import *

class controller(controllerClass):
  def defaultAction(self):
    
    self.tmpl.decorator=decorator('href')
    self.tmpl.setVar('testit',('a','b','c'))
    self.tmpl.setVarSingle('var',{'text':'wp','href':'http://wp.pl'})
    self.tmpl.setVarSingle('heading',{'text':'Pyshop frontpage'},decorator('heading'))
    
  
  def prepare(self):
    self.startAction()