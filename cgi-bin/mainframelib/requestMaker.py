import cgitb
import cgi

from serverPath import *

class requestMaker(object):
    me=None
    @staticmethod
    def getMe():
        if requestMaker.me==None:
            requestMaker.me=requestMaker()
        return requestMaker.me
    
    def __init__(self):
         self.params=cgi.FieldStorage()
    
    def getGET(self):
        arguments = cgi.FieldStorage()
        
        
    
    def getReq(self,name,default=None):
        v=self.params.getvalue(name)
        if v==None:
            return default
        else:
            return v
   
    def mkRequest(self,dict,append=True): #make it remove duplicates
     sp=serverPath()
     if append:
       req=sp.getUri()
     else:
        req=""
     for k in dict:
        v=dict[k]
        req=req+k+'='+v+"&amp;"
     return req
 