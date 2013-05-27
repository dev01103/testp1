#!/bin/env python

class partClass(object):
  def __init__(self):
    self.partdir='parts/'
 
  
  def display(self,template,position):
    self.template=template
    self.position=position
    self.code=template.getFile('/template.tpl',self.partdir)
    # print self.partdir+'/template.tpl'
    if self.code==False:
      print "error"
    print self.code
    self.template.setVar(self.position,self.code)
    
  