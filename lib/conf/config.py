from conf import settings
from lib.conf import global_settings

class mySettings():
    def __init__(self):
        for k in dir(global_settings):
            # 返回参数的属性、方法列表。如果参数包含方法__dir__()，该方法将被调用
            if k.isupper():
                #getattr返回一个对象的属性值
                v = getattr(global_settings,k)
                setattr(self,k,v)

        for k in dir(settings):
            if k.isupper():
                v = getattr(settings,k)
                setattr(self,k,v)

settings = mySettings()
# print(settings.MODE)