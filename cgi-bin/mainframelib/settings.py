from database import *

class siteSettings:
    me=None
    @staticmethod
    def getMe():
        if me==None:
            me=siteSettings()
        return me
    def getVal(self,key):
        db=databaseConn.getMe()
        query="select distinct key,val from pyshop_settings where key="+db.q(key)
        db.query(query)
        res=db.getResults()
        return res[0];
