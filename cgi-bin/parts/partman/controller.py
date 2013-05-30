from mainframelib.classes.controllerClass import *

class controller(controllerClass):
  
  def listParts(self):
    allparts=self.model.getAllParts()
    
  
  def editParts(self):
    self.tmpl.setVar('partman_content','edit')
  
  def defaultAction(self):
    self.listParts()
  
  
  def prepare(self):
    self.tmpl.hideUnused(True)
    self.startAction()