from mainframelib.classes.modelClass import *

class model(modelClass):
  def getAllParts(self):
    db=databaseConn.getMe()
    query="select * from pyshop_parts"
    db.query(query)
    return db.getResults()