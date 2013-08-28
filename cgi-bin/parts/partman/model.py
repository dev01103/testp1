from mainframelib.classes.modelClass import *

class model(modelClass):
  def getAllParts(self):
    db=databaseConn.getMe()
    query="select * from pyshop_parts"
    db.query(query)
    return db.getResults()
  
  def getPart(self,pid):
      db=databaseConn.getMe()
      query="select * from pyshop_parts where part_id="+pid
      db.query(query)
      return db.getResults()[0]