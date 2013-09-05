from mainframelib.classes.controllerClass import *

class controller(controllerClass):
  def defaultAction(self):
    #default action for part
    pass
  def prepare(self):
      menus=self.model.getMenus()
      self.tmpl.setVar('menus',menus)