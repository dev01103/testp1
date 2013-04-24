#!/usr/bin/env python
import cgitb
import cgi
cgitb.enable()
import template
import mainController


class mainframe:
  def __init__(self):
   print "Content-Type: text/html\n\n"
   self.controller=mainController.mainController()
   self.controller.parseRequest()
   self.template=template.template()
   self.template.setVar('test','666');
   self.controller.proceed(self.template)

  