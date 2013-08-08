class singleton(object):
  me=None
  @staticmethod
  def getMe():
   if singleton.me==None:
     singleton.me=singleton()
   return singleton.me
  