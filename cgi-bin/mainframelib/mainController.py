import classes.controllerClass
from mainframelib.mainframe import *
from template import *
import importlib
import sys

class mainController(classes.controllerClass.controllerClass):
  
   
  def loadPart(self,name):
    #try:
     importlib.import_module('parts.'+name+'.controller')
    #except:
    #  print 'Error loading part: ','parts.'+name+'.controller'
    #  sys.exit()
  
  def processParts(self,positions,body):
   parts=self.model.getAllPartsPos(positions)  
   for p in parts:
     self.loadPart(p['name'])
  
  def proceed(self,tpl):
    tmpl='templates/'+tpl
    self.head=template(tmpl)
    self.head.getFile('head.tpl')
    head_code=self.head.parse()
    self.body=template(tmpl)
    self.body.getFile('views/'+self.view+'.tpl')
    positions=self.body.getPositions()
    self.processParts(positions,self.body)
    body_code=self.body.parse()
    self.template=template(tmpl)
    self.template.getFile('index.tpl')
    self.template.setVar('head',head_code)
    self.template.setVar('body',body_code)
    main_code=self.template.parse()  
    print main_code
    #dir(mainframelib.mainframe)
    