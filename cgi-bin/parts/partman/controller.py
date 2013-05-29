from mainframelib.classes.controllerClass import *

class controller(controllerClass):
  
  def listParts(self):
    self.tmpl.setVar('partman_content','list')
  
  def editParts(self):
    self.tmpl.setVar('partman_content','edit')
  
  
  def prepare(self):
    self.tmpl.hideUnused(True)
    self.startAction()