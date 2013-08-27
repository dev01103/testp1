from mainframelib.classes.controllerClass import *

class controller(controllerClass):
  def defaultAction(self):
    self.tmpl.setVar('backend_header','Pyshop admin')
  
  def prepare(self):
    self.setTitle('Admin')
    self.startAction()
    self.addCss('backend_main.css')
