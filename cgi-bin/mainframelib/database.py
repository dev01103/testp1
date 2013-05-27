#!/bin/env python

import config
# import dbo.dbo
import importlib
import sys


class databaseConn:
 me=None
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
 
 def getResults(self):
   return self.dbo.getResults()
   
 
 def query(self,q):
      self.dbo.query(q)
   
 

  
  
  