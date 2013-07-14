from database import *

class mysqldbo(databaseConn): 
 def connect(self,host,user,psw,db):
      try:
	dbo.conn=mdb.connect(host,user,pwd,db)
	dbo.cur=dbo.conn.cursor(mdb.cursors.DictCursor)
	return True
      except mdb.Error:
	return False
   
 def disconnect(self):
    dbo.conn.close()
 
 def query(self,q):
   return cur.execute(q);
 

 
 def getResults(self):
   ret=cur.fetchall()
   return ret