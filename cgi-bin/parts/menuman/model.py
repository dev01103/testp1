from mainframelib.classes.modelClass import *

class model(modelClass):
  def getMenus(self):
      db=databaseConn.getMe()
      db.query("select * from pyshop_menus")
      res=db.getResults()
      return res