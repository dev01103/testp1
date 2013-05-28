import cgitb
import cgi
import importlib
import mainframelib
from mainframelib.mainframe import *


class controllerClass(object):
  def __init__(self,tmpl):
    self.params=cgi.FieldStorage()
    self.tmpl=tmpl
    self.view=''
  
  def loadPart(self,name):
    
     part_model=importlib.import_module('parts.'+name+'.model').model()
     part_template=self.tmpl.getSubtemplate('/parts/')
     part_template.getFile(name+'.tpl')
     part_controller=importlib.import_module('parts.'+name+'.controller').controller(part_template)
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
   self.action=self.getReq('action')
  
  def getAction(self):
    return self.action
    
  def prepare(self): #custom preparations done in parts
    pass
  
  def proceed(self):
    positions=self.tmpl.getPositions()
    self.processParts(positions,self.tmpl)
    self.prepare()
    self.html=self.tmpl.parse()
    return self.html
    
  
  def redirect(self):
    pass