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


class mainframe:
  me=None
  #Public functions
  @staticmethod
  def getMe():
   if mainframe.me==None:
     mainframe.me=mainframe()
   return mainframe.me

  def __init__(self):
   print "Content-Type: text/html\n\n"
   self.model=mainModel()
   self.controller=mainController()
   self.controller.setModel(self.model)
   self.controller.parseRequest()
   tmpl=self.model.getTemplate()
   self.controller.proceed(tmpl)
  
   
  
   
   
  