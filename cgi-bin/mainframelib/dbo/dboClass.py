

class dboClass:
  def __init__(self):
    self.result_format=None
    
  
  def setDbData(self,host,user,psw,db):
    self.host=host
    self.user=user
    self.psw=psw
    self.db=db
  
  def connect(self,host,user,psw,db):
    pass
  def setFormat(self,result_format):
    self.result_format=result_format
  def disconnect(self):
    pass
  def query(self,q):
    pass
  def getResults(self):
    pass
  def disconnect(self):
    pass
 
    