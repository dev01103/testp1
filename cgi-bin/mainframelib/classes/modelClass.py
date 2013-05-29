import cgitb
import cgi
import importlib
import mainframelib
from mainframelib.mainframe import *
import os
import sys
import inspect
from runpy import *
from mainframelib.database import *
from mainframelib.renderer import *

class modelClass(object):
  def __init__(self):
    pass
  
  def setController(self,c):
    self.controller=c
    