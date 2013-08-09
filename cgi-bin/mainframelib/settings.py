from database import *

class siteSettings:
    me=None
    @staticmethod
    def getMe():
        if siteSettings.me==None:
            siteSettings.me=siteSettings()
        return siteSettings.me
    def getVal(self,key):
        db=databaseConn.getMe()
        query="select val from pyshop_settings where pyshop_settings.key="+db.q(key)
        #print query
        db.query(query)
        res=db.getResults()
        return res[0]['val'];
