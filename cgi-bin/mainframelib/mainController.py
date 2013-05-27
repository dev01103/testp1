import classes.controllerClass
from template import *


class mainController(classes.controllerClass.controllerClass):
  
    
   
  def proceed(self,tpl):
    tmpl='templates/'+tpl
    self.head=template(tmpl)
    self.head.getFile('head.tpl')
    head_code=self.head.parse()
    self.body=template(tmpl)
    self.body.getFile('views/'+self.view+'.tpl')
    body_code=self.body.parse()
    self.template=template(tmpl)
    self.template.getFile('index.tpl')
    self.template.setVar('head',head_code)
    self.template.setVar('body',body_code)
    main_code=self.template.parse()  
    print main_code
    