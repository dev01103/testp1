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
from mainframelib.serverPath import  *
from mainframelib.requestMaker import *


class controllerClass(object):

  def getTitle(self):
    return self.title

  def setTitle(self,title):
      self.title=title
      
  def addCss(self,fn,dir=None):
      if dir is None:
          dir=self.wwwpath
      code='<link rel="stylesheet" href="'+dir+self.p.S+'css'+self.p.S+fn+'" />\n'
      self.appendToHead(code)
  
  def addJs(self,fn,dir=None):
      if dir is None:
          dir=self.wwwpath
      code='<script src="'+dir+self.p.S+'js'+self.p.S+fn+'"></script>\n'
      self.appendToHead(code)
  
  def appendToHead(self,code):
    self.appendHead=self.appendHead+code

  def getAppend(self):
      return self.appendHead
  
  def getAcl(self):
    db=databaseConn.getMe()
    #query="select * 
    return True
  
  def isAllowed(self):
    return self.allowed & self.allowed_children
    
  
  def __init__(self,tmpl,name):
    self.req=requestMaker.getMe()
    self.p=serverPath.getMe()
    self.wwwpath=self.p.getWebUrlRoot()
    self.title=''
    self.appendHead=''
    self.tmpl=tmpl
    self.view=''
    self.name=name
    self.allowed=True
    self.allowed_children=True
    self.actions={}
    self.addAction('default',self.defaultAction)
    
  def linkLay(self,layout): #temporary
    lay=name+"_layout="+layout    
    return lay
  
    
  def loadPart(self,name):
     part_model=importlib.import_module('parts.'+name+'.model').model()
     part_template=self.tmpl.getSubtemplate()
     lay=self.req.getReq(name+'_layout','')
     if lay<>"":
         lay="."+lay
     #print lay
     part_template.getFile(name+lay+'.tpl')
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
     ap=c.getAppend()
     self.appendToHead(ap)
     tit=c.getTitle()
     if tit!='':
        self.title=self.title+' - '+tit
     body.setVar(p['position'],html)
  
  
  def setModel(self,m):
    self.model=m
  
  
  
  def parseRequest(self):
   self.view=self.req.getReq('view','main')
   if self.name<>'':
     name=self.name+'_'
   else:
     name=''
   self.action=self.req.getReq(name+'action')
  
  def getAction(self):
    return self.action
  
  def defaultAction(self):
    pass
  
  def addAction(self,name,function):
    self.actions[name]=function
    
  def startAction(self):
   act=self.getAction()
   if act=='' or act==None or act not in self.actions.keys():
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