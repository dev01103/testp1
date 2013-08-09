import re
import sys
import copy



class template(object):
  def __init__(self,path):
    self.path=path
    self.tplpath=path
    self.varArray=dict()
    self.name=None
    self.hide=False
    self.decorator=None
    self.sorrounding=None
    
  def hideUnused(self,yes):
    self.hide=yes
  
  def setDecorator(self,tmpl,sorrounding=None):
    self.decorator=tmpl
    self.sorrounding=sorrounding
  
  def setVarSingle(self,name,v,decor=None):
    if decor==None:
      decor=self.decorator
    for dk in v:
      decor.setVar(dk,v[dk])
    parsed=decor.parse()
    self.setVar(name,parsed)
    
  def setVarIterated1D(self,name,arr):
    pass
  
  def setVar(self,name,value):
   self.varArray[name]=value
   
  def getSubtemplate(self,path=None):
    #print self.tplpath
    p=self.tplpath+'/parts'
    t=template(p)
    t.tplpath=self.tplpath
    return t
  
  def getCode(self,code):
    self.code=code
  
  def getFile(self,fn):
   try:
    name=self.path+'/'+fn
    self.name=name
    #print "n "+name
    f=open(name)
    self.code=f.read()
   except IOError:
     print ':[ '+self.path+'/'+fn
     sys.exit('ERROR')
   else:
     self.code
     
     
  def getPositions(self):
    cd=self.code
    #cd=re.sub(r'[{{iterate=.*$','',cd,re.MULTILINE|re.DOTALL)
    p=re.findall(r'{{.*}}',cd)
    #print p
    ret=p
    i=0
    for x in p:  #removing {{}} from names
	 ret[i]=re.sub(r'[{{}}]','',x)
	 i=i+1
    return ret
     
  def parseDict(self,code,dic,inside):
    key=code
    key=re.sub(r'{{.*\.',r'',key)
    key=re.sub(r'}}',r'',key)
    key=re.sub(r'\s',r'',key)
    t=template('')
    t.code=code
    for k in dic:
      t.setVar(inside+'.'+k,str(dic[k]))
      
      
    t.code=t.parse()  
    return (key,t.code)
    
    
    
  
  def parseIter(self,code,varname,var):
    t=template('')
    itas=re.search(r'as.*}}',code)
    itas=itas.group(0)
    itas=re.sub(r'as ','',itas)
    itas=re.sub(r'}}','',itas)
    
    insides=re.sub(r'^{{iterate=.*}}','',code)
    insides=re.sub(r'{{/iterate.*}}$','',insides)
    #print insides
    html=''
    n=0
    for v in var:
      t.code=insides
      if(type(v)==type({'x':'y'})):
       (n,v)=self.parseDict(t.code,v,itas)
       t.code=v
      else:
       t.setVar(itas,v)
      
      html=html+t.parse() 
      
      
    
    return html
    
    
    
  
  def parse(self):
   newcode=self.code
   for i in self.varArray:
     regex=r'{{iterate='+i+' as.*}}.*{{/iterate}}'
     iterables=re.findall(regex,self.code,re.MULTILINE|re.DOTALL)
     if iterables<>None:
      for it in iterables: 
       parsed=self.parseIter(it,i,self.varArray[i])
       newcode=re.sub(it,parsed,newcode)
     
     try:
       newcode=re.sub(r'{{'+i+'}}',self.varArray[i],newcode)
     except:
       pass
   
   if self.hide==True:
     newcode=re.sub(r'{{.*}}','',newcode)
   return newcode
  
  
 