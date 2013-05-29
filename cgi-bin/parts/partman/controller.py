from mainframelib.classes.controllerClass import *

class controller(controllerClass):
  
  def listParts(self):
    allparts=self.model.getAllParts()
    #r=renderer()
    #self.tmpl.setVar('partman_content',r.iterated(allparts))
  
  def editParts(self):
    self.tmpl.setVar('partman_content','edit')
  
  def defaultAction(self):
    self.tmpl.setVar('partman_content','da')
  
  
  def prepare(self):
    self.tmpl.hideUnused(True)
    self.startAction()