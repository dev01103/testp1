#!/usr/bin/env python
import cgitb
import cgi
cgitb.enable()

from template import *
from mainController import *
from database import *
import parts
from parts import frontpage
import config
from mainModel import *
import sys
from output import *


class mainframe:
  me=None
  counter=0
  #Public functions
  
  def addCss(self,css):
    pass
  
  def addScript(self,js):
    pass
  
  @staticmethod
  def getMe():
   if mainframe.me==None:
     mainframe.me=mainframe()
   return mainframe.me
  
  def getTemplate(self):
      if self.templatename==None:
	db=databaseConn.getMe()
	db.query('select name from pyshop_templates as t where t.default=1 and type=\'FE\'')
	res=db.getResults()
	self.templatename=res[0]['name']
      return self.templatename
    
  def getAllPartsPos(self,positions):
      if len(positions)>0 and positions<>None:
       db=databaseConn.getMe()
       query="select * from pyshop_parts where position in ("+db.qj(positions)+") order by ordering"
       db.query(query)
       return db.getResults()
      else:
	return []
     
  def getPartsByPos(self,pos):
      db=databaseConn.getMe()
      query='select * from pyshop_parts where position='+db.q(pos)+' order by ordering'
      db.query(query)
      res=db.getResults()
      return res
  
  def logUser(self,user=None,psw=None): #concept is that even unlogged user is logged as guest
    if user==None:
      #guest login routines
      pass
    else:
      pass
    db=databaseConn.getMe()
    query="select * from pyshop_users where user_name="+db.q(user);
    
  
  
  def go(self):
   print "Content-Type: text/html\n\n"
   o=output.getMe()
   self.model=mainModel()
   tpl=self.getTemplate()
   tmpl=template('templates/'+tpl)
   self.controller=mainController(tmpl,'')
   self.controller.setModel(self.model)
   self.controller.parseRequest()
   self.controller.proceed()
   self.controller.display()
  
  def __init__(self):
    mainframe.counter=mainframe.counter+1
    self.templatename=None
   
   
  
   
  
   
   
  