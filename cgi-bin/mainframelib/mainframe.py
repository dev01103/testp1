#!/usr/bin/env python
import cgitb
import cgi
cgitb.enable()
import template
import mainController
from mysqldbo import *
import parts
from parts import frontpage
from parts.frontpage import frontpage



class mainframe:
  def __init__(self):
   print "Content-Type: text/html\n\n"
   self.controller=mainController.mainController()
   self.controller.parseRequest()
   self.template=template.template()
   self.template.setVar('test','666');
   self.controller.proceed(self.template)
   #print frontpage
   fp=parts.frontpage.frontpage.frontpagePart()
   fp.display(self.template,'centerpart')
   mysqldbo.getMe()
   
  