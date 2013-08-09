from mainframelib.classes.controllerClass import *
from mainframelib.decorator import *

class controller(controllerClass):
  def defaultAction(self):
    self.tmpl.decorator=decorator('href')
    self.tmpl.setVar('testit',(('a1','a2','a3'),('b1','b2','b3'),('c1','c2','c3')))
    self.tmpl.setVar('heading','test')
    #d={'a':'1','b':'2'}
    #d=tuple(d.items())
    
    
  
  def prepare(self):
    self.title='Frontpage'
    self.addCss('frontpage.css')
    self.addJs('test.js')
    self.startAction()