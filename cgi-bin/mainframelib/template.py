import re
import sys

class template:
  def __init__(self,path):
    self.path=path
    self.varArray=dict()
    self.name=None
    self.hide=False
    self.decorator=None
    #self.iteratedDecorator.getCode(
    
  def hideUnused(self,yes):
    self.hide=yes
  
  
  
  def setVarHref(self,name,link):
    pass
  
  def setVarIterated(self,name,arr):
    pass
  
  def setVar(self,name,value):
   self.varArray[name]=value
   
  def getSubtemplate(self,path):
    return template(self.path+'/'+path)
  
  def getCode(self,code):
    self.code=code
  
  def getFile(self,fn):
   try:
    name=self.path+'/'+fn
    f=open(self.path+'/'+fn)
    self.code=f.read()
   except IOError:
     print self.path+'/'+fn
     sys.exit('ERROR')
   else:
     self.code
     
     
  def getPositions(self):
    p=re.findall(r'{{.*}}',self.code)
    ret=p
    i=0
    for x in p:
	ret[i]=re.sub(r'[{{}}]','',x)
	i=i+1
    return ret
      
  
  def parse(self):
   newcode=self.code
   for k in self.varArray:
     newcode=re.sub(r'{{'+k+'}}',self.varArray[k],newcode)
   if self.hide==True:
     newcode=re.sub(r'{{.*}}','',newcode)
   return newcode
  
  
  
'''

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
 
 
 
 def getFile(self,fn,path=None):
   if path==None:
    tplpath=self.tplpath+fn
   else:
    tplpath=path+fn
   # print tplpath
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
     '''