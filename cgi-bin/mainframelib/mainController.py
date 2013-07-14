import classes.controllerClass
from mainframelib.mainframe import *
from template import *
import importlib
import sys
import copy
from output import *

class mainController(classes.controllerClass.controllerClass):
  
   
  
     
  def display(self):
    o=output.getMe()
    o.o(self.main_code)
  
  def proceed(self):
    self.head=copy.deepcopy(self.tmpl)
    self.head.getFile('head.tpl')
    head_code=self.head.parse()
    self.body=copy.deepcopy(self.tmpl)
    self.body.getFile('views/'+self.view+'.tpl')
    positions=self.body.getPositions()
    self.processParts(positions,self.body)
    body_code=self.body.parse()
    self.template=self.tmpl
    self.template.getFile('index.tpl')
    self.template.setVar('head',head_code)
    self.template.setVar('body',body_code)
    self.main_code=self.template.parse()  
    
    #dir(mainframelib.mainframe)
    