from classes.modelClass import *
from database import *

class mainModel(modelClass):
    def getTemplate(self):
      db=databaseConn.getMe()
      db.query('select name from pyshop_templates as t where t.default=1 and type=\'FE\'')
      res=db.getResults()
      return res[0]['name']
    
    def getAllPartsPos(self,positions):
      db=databaseConn.getMe()
      query="select * from pyshop_parts where position in ("+db.qj(positions)+") order by ordering"
      db.query(query)
      return db.getResults()
     
    def getPartsByPos(self,pos):
      db=databaseConn.getMe()
      query='select * from pyshop_parts where position='+db.q(pos)+' order by ordering'
      db.query(query)
      res=db.getResults()
      return res