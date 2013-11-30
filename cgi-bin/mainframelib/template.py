import re
import sys
import copy

from serverPath import *
from requestMaker import *

class template(object):
  def __init__(self, path):
    self.path = path
    self.tplpath = path
    self.varArray = dict()
    self.name = None
    self.hide = False
    self.decorator = None
    self.sorrounding = None
    
  def hideUnused(self, yes):
    self.hide = yes
  
  def setDecorator(self, tmpl, sorrounding=None):
    self.decorator = tmpl
    self.sorrounding = sorrounding
  
  def setVarSingle(self, name, v, decor=None):
    if decor == None:
      decor = self.decorator
    for dk in v:
      decor.setVar(dk, v[dk])
    parsed = decor.parse()
    self.setVar(name, parsed)
    
  def setVarIterated1D(self, name, arr):
    pass
  
  def setVar(self, name, value):
   self.varArray[name] = value
   
  def getSubtemplate(self, path=None):
    # print self.tplpath
    p = self.tplpath + '/parts'
    t = template(p)
    t.tplpath = self.tplpath
    return t
  
  def getCode(self, code):
    self.code = code
  
  def getFile(self, fn):
   try:
    name = self.path + '/' + fn
    self.name = name
    # print "n "+name
    f = open( os.path.dirname(__file__) + "/../"+name)
    self.code = f.read()
   except IOError:
     #print name
     #print ':[ ' + self.path + '/' + fn
     sys.exit('ERROR '+ self.path + '/' + fn)
   else:
     self.code
     
     
  def getPositions(self):
    cd = self.code
    p = re.findall(r'{{.*}}', cd)
    ret = p
    i = 0
    for x in p:  # removing {{}} from names
	 ret[i] = re.sub(r'[{{}}]', '', x)
	 i = i + 1
    return ret
     
  def parseDict(self, code, dic, inside):
    key = code
    key = re.sub(r'{{.*\.', r'', key)
    key = re.sub(r'}}', r'', key)
    key = re.sub(r'\s', r'', key)
    t = template('')
    t.code = code
    for k in dic:
      t.setVar(inside + '.' + k, str(dic[k]))
    t.code = t.parse()  
    return (key, t.code)
    
    
    
  
  def parseDicts(self, code, var,itas):
      html = ''
      n = 0
      t = template('')
      for v in var:
       t.code = code
       if(type(v) == type({'x':'y'})):
        (n, v) = self.parseDict(t.code, v, itas)
        t.code = v
       else:
        t.setVar(itas, v)
       html = html + t.parse()
      return html
    
  
  def parseIter(self, code, varname, var):
    t = template('')
    itas = re.search(r'as.*}}', code)
    itas = itas.group(0)
    itas = re.sub(r'as ', '', itas)
    itas = re.sub(r'}}', '', itas)
    #print itas
    insides = re.sub(r'^{{iterate=.*}}', '', code)
    insides = re.sub(r'{{/iterate.*}}$', '', insides)
    html = ''
    html=self.parseDicts(insides,var,itas)   
    return html
    
  
    
  def parseLink(self, link): 
          isself = re.findall(r'SELF', link);
          if isself:
              isself = True
          else:
              isself = False
          
          datastr = re.findall(r' .*=.*', link)[0]
          datastr = re.sub(r'}}', '', datastr)
          data = datastr.rsplit(' ')
          data_dict = {}
          for d in data:
              vals = d.rsplit('=')
              # print vals
              if len(vals) == 2:
                  data_dict[vals[0]] = vals[1].replace('\"', '')
          return (data_dict, isself)
          
    
  
  def parse(self):
   
   
   newcode = self.code  
   for i in self.varArray:
     regex = r'{{iterate=' + i + ' as.*}}.*{{/iterate}}'
     iterables = re.findall(regex, self.code, re.MULTILINE | re.DOTALL)
     if iterables <> None:
      for it in iterables: 
       parsed = self.parseIter(it, i, self.varArray[i])
       newcode = re.sub(it, parsed, newcode)
     # else:
     try:
       newcode = re.sub(r'{{' + i + '}}', self.varArray[i], newcode)
     except:
       pass
       
   regex = r'{{.*\..*}}'
   dicts=re.findall(regex,newcode)
   #print dicts
   
   for d in dicts:
       
       
       k=d
       k=re.sub(r'\..*}}','',k)
       k=re.sub(r'{{', '', k)
       
       if k in self.varArray.keys(): 
           subk=d
           subk = re.sub(r'{{.*\.', '', subk)
           subk = re.sub(r'}}', '', subk)
           dk,dr=self.parseDict(d, self.varArray[k],subk)
           newcode=newcode.replace(dr,self.varArray[k][dk])
       
       
   
       
       
   hrefregex = r'{{link.*}}'
   links = re.findall(hrefregex, newcode, re.MULTILINE)
   if links <> None:
    req = requestMaker.getMe()
    for link in links:   
     d, slf = self.parseLink(link)
     newcode = re.sub(hrefregex, req.mkRequest(d, slf), newcode)
   if self.hide == True:
     newcode = re.sub(r'{{.*}}', '', newcode)
   return newcode
  
  
 
