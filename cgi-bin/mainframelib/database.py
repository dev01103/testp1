#!/bin/env python

import config
# import dbo.dbo
import importlib
import sys

from mainframelib.pdo import *


class databaseConn:
 me=None
 
 @staticmethod
 def getPdo(self):
     if self.pdo is None:
         self.pdo=pdo(self.dbo)
     return self.pdo
 
 @staticmethod
 def getMe():
   #global config.global_config
   #print config.db_addr
   if databaseConn.me==None:
     # print "Creating new dbconn"
     databaseConn.me=databaseConn()
   return databaseConn.me

 def connect(self):
  self.dbo.connect(config.db_addr,config.db_user,config.db_pass,config.db_name)
  self.connected=True
  
 def disconnect(self):
   self.connected=False
   self.dbo.disconnect()
  
 def __init__(self):
  self.res_format=None
  self.pdo=None
  try:
   self.dbo=importlib.import_module('mainframelib.dbo.'+config.db_type).dbo()
  except:
   print "No such dbo!"
   sys.exit()
  else:
    self.connected=False
    self.connect()
  
 def __del__(self):
   self.dbo.disconnect()
 
 def setFormat(self,res_format):
   self.res_format=res_format
 
 def countResults(self):
   res=self.dbo.getResults()
   if res<>None:
     return len(res)
   else:
    return 0
 
 def getResults(self): #TODO: optimize for getting results only once
   return self.dbo.getResults()
   
 def q(self,s): #add proper escaping
   s=s.replace('"', '\\"')
   return '"'+s+'"'
 
 def qj(self,a):
  newa=a
  i=0
  for x in a:
     x=self.q(x)
     newa[i]=x
     i=i+1
     
  return ','.join(newa)
 
 def query(self,q):
      self.dbo.query(q)
   
 

  
  
  