from mainframelib.classes.controllerClass import *

class controller(controllerClass):
  
  def listParts(self):
    allparts=self.model.getAllParts()
    #print allparts
    self.tmpl.setVar('parts',allparts)
    
  
  def editParts(self):
    self.tmpl.setVar('partman_content','edit')
  
  def testAction(self):
      print "test"
  
  def defaultAction(self):
    pass
  
  def editAction(self):
      pid=self.req.getReq('pid');
      part=self.model.getPart(pid)      
      self.tmpl.setVar('part',part)  
      if part['published']:
          pub="checked"
      else:
          pub=""
      self.tmpl.setVar('published',pub)
      pass
  
  def prepare(self):
    #self.tmpl.hideUnused(True)
    
    self.listParts()
    self.addAction('test',self.testAction)
    self.addAction('edit',self.editAction)
    self.startAction()