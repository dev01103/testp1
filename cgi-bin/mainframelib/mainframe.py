#!/usr/bin/env python
import cgitb
import cgi
cgitb.enable()

from template import *
from mainController import *
from database import *
import parts
from parts import frontpage
from parts.frontpage import frontpage
import config


class mainframe:
  me=None
  #Public functions
  @staticmethod
  def getMe():
   if mainframe.me==None:
     mainframe.me=mainframe()
   return mainframe.me
  def getDB(self):
    return self.dbo
  
  #Private functions
  def getTemplate(self):
    self.db=databaseConn.getMe()
    self.db.query('select name from pyshop_templates as t where t.default=1 and type=\'FE\'')
    res=self.db.getResults()
    # print res
    return res[0]['name']
    
  
  
  def __init__(self):
   print "Content-Type: text/html\n\n"
   self.getTemplate()
   self.controller=mainController()
   self.controller.parseRequest()
   tmpl=self.getTemplate()

   self.controller.proceed(tmpl)
  
   
  
   
   
  