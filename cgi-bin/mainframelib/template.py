import re

class template:
 def __init__(self):
   self.tplpath='templates/basic/'
   self.varArray=dict()
   self.title=''
   
   
 def getHead(self):
   return "<head>"\
   +"\n<title>"\
   +self.title\
   +"\n</title>\n"\
   +"</head>"
 
 def setVar(self,name,value):
   self.varArray[name]=value
  
 def setTitle(self,title):
   self.title=title
   
   
 def parse(self,code):
   newcode=code
   for k in self.varArray:
     newcode=re.sub(r'{{'+k+'}}',self.varArray[k],newcode)
   return newcode
 
 def parseMain(self,code):
   newcode=code
   newcode=re.sub(r'{{head}}',self.getHead(),newcode) #to be done with setVar
   newcode=re.sub(r'{{body}}',self.body_code,newcode,re.MULTILINE | re.DOTALL)
   newcode=self.parse(newcode)
   return newcode
 
 
 
 def getFile(self,fn):
   tplpath=self.tplpath+fn
   try:
    f=open(tplpath)
    tmp_code=f.read()
   except IOError:
     return False
   else:
     return tmp_code
     
 def process(self,filename='main.tpl'):
    tmp_code=self.getFile('index.tpl')
    self.body_code=self.getFile(filename)
    if self.body_code==False:
      if filename=="main.tpl":
       print "Template error!"
       quit()
      else:
	self.process('main.tpl')
    else:
     print self.parseMain(tmp_code)