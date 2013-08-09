from mainframelib.classes.controllerClass import *
from mainframelib.mainframe import *

class controller(controllerClass):
  def defaultAction(self):
      pass
      
  
  def prepare(self):
      parts=self.model.getAllParts()
      self.tmpl.setVar('testparts',parts[0]['name'])
      self.tmpl.setVar('ps',parts)
      self.startAction()
    