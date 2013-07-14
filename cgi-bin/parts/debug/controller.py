from mainframelib.classes.controllerClass import *
from mainframelib.mainframe import *

class controller(controllerClass):
  def prepare(self):
    self.mf=mainframe.getMe()
    self.db=databaseConn.getMe()
    self.tmpl.setVar('counter',str(mainframe.counter))