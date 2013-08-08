import cgitb
import cgi
import importlib
import mainframelib
from mainframelib.mainframe import *
import os
import sys
import inspect
from runpy import *
from mainframelib.database import *



class controllerClass(object):
  def setTitle(self,title): #head  not from template (?), but auto-generated or choice
    self.title=title
  
  def getTitle(self):
    return self.title
  
  def appendToHead(self,code):
    pass
  
  def getAcl(self):
    db=databaseConn.getMe()
    #query="select * 
    return True
  
  def isAllowed(self):
    return self.allowed & self.allowed_children
    
  
  def __init__(self,tmpl,name):
    self.title='Title'
    self.params=cgi.FieldStorage()
    self.tmpl=tmpl
    self.view=''
    self.name=name
    self.allowed=True
    self.allowed_children=True
    self.actions={}
    self.addAction('default',self.defaultAction)
    
    
  def loadPart(self,name):
     part_model=importlib.import_module('parts.'+name+'.model').model()
     part_template=self.tmpl.getSubtemplate()
     part_template.getFile(name+'.tpl')
     part_controller=importlib.import_module('parts.'+name+'.controller').controller(part_template,name)
     self.allowed_children=self.allowed_children & part_controller.isAllowed()
     return (part_model,part_template,part_controller)
    
  
  def processParts(self,positions,body):
   mf=mainframelib.mainframe.mainframe.getMe()
   parts=mf.getAllPartsPos(positions)  
   for p in parts:
     (m,v,c)=self.loadPart(p['name'])
     c.setModel(m)
     html=c.proceed()
     body.setVar(p['position'],html)
  
  
  def setModel(self,m):
    self.model=m
  
  def getReq(self,name,default=None):
    v=self.params.getvalue(name)
    if v==None:
      return default
    else:
      return v
  
  def parseRequest(self):
   if self.params.getvalue('view')<>None:
      self.view=self.params.getvalue('view')
   else:
       self.view='main'
   if self.name<>'':
     name=self.name+'_'
   else:
     name=''
   self.action=self.getReq(name+'action')
  
  def getAction(self):
    return self.action
  
  def defaultAction(self):
    pass
  
  def addAction(self,name,function):
    self.actions[name]=function
    
  def startAction(self):
   act=self.getAction()
   if act=='' or act==None:
     act='default'
   self.actions[act]()
   
  
  def prepare(self): #custom preparations done in parts
    pass
  
  def proceed(self):
    #if self.getAcl()==False:
    #  return 'NO!'
    self.parseRequest()
    positions=self.tmpl.getPositions()
    self.processParts(positions,self.tmpl)
    self.prepare()
    self.html=self.tmpl.parse()
    return self.html
    
  
  def redirect(self):
    pass