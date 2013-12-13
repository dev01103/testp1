
from dboClass import *
import MySQLdb as mdb

class dbo(dboClass):
  def connect(self):
	try:
	  self.conn=mdb.connect(self.host,self.user,self.psw,self.db)
	  self.cur=self.conn.cursor(mdb.cursors.DictCursor)
	  return True
	except mdb.Error:
	  return False

  def disconnect(self):
      self.conn.close()
 
  def query(self,q):
   self.connect()
   return self.cur.execute(q)
 
  def getResults(self):
   ret=self.cur.fetchall()
   return ret