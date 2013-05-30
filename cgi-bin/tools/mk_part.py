#!/usr/bin/env python

import sys
import os
import shutil

sys.path.append('..')

from mainframelib.database import *

rootdir='..'

def checkInDB(name):
  db=databaseConn.getMe()
  query="select name from pyshop_parts where name="+db.q(name)
  db.query(query)
  if db.countResults()<>0:
    return False
  else:
    return True

def makeFiles(name):
  os.makedirs(rootdir+'/parts/'+name)
  shutil.copy('data/part_template/controller.py',rootdir+'/parts/'+name+'/controller.py')
  shutil.copy('data/part_template/model.py',rootdir+'/parts/'+name+'/model.py')
  shutil.copy('data/part_template/__init__.py',rootdir+'/parts/'+name+'/__init__.py')
  shutil.copy('data/part_template/template.tpl',rootdir+'/templates/basic/parts/'+name+'.tpl')

  
def insertDB(name):
  db=databaseConn.getMe()
  

print "Pyshop part making utility"

try:
 partname=sys.argv[1]
except:
  print "No params"
  sys.exit(1)

print "Making files..."
makeFiles(partname)
  


print "Making part ",partname
print "Checking for duplicate..."
if checkInDB(partname)==True:
  print "OK"
else:
  print "Failed"
  sys.exit(1)




