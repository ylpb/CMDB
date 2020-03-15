from src.plugins import Plugins_Manager
from lib.conf.config import settings
import requests
class Agent():
    def collectAndPost(self):
        ret = Plugins_Manager().execute()
        for k,v in ret.items():
            print(k,v)
        #
        requests.post(settings.API_URL,json=ret)



class mySSh():


    def getHostnames(self):
        '''获取主机名'''
        hostname = requests.get(settings.API_URL)
        return hostname


    def task(self,hostname):
        ret = Plugins_Manager(hostname=hostname).execute()
        requests.post(settings.API_URL,json=ret)

    def collectAndPost(self):
        '''并发发送设备信息给API服务器'''
        hostnames = self.getHostnames()
        from concurrent.futures import ThreadPoolExecutor
        p = ThreadPoolExecutor(10)
        for hostname in hostnames:
            p.submit(self.task,hostname)