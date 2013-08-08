

class renderer(object): #this is obsolete
  def __init__(self):
    defaultIterated=template('')
    defaultIterated.getCode()
  def setIteratedTmpl(self,tmpl):
    pass
  def iterated(self,arr):
    html=''
    for a in arr:
      for k in a:
	html=html+' '+str(a[k])
    return html