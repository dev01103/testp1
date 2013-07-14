import mainframelib
import mainframelib.classes
from mainframelib.classes.partClass import *

class frontpagePart(partClass):
  def __init__(self):
    super(frontpagePart,self).__init__()
    self.partdir=self.partdir+'frontpage'
  
  def display(self,template,position):
    super(frontpagePart,self).display(template,position)
    #self.template.setVar('testpart','ttt')