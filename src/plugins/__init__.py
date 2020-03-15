
from  lib.conf.config import settings
import importlib
import traceback

#### 主要是用来管理插件的类
class Plugins_Manager():

    def __init__(self,hostname=None):
        self.plugins_dict = settings.PLUGINS_DICT

        self.settings = settings.MODE

        self.debug = settings.DEBUG
        self.hostname = hostname
    ### 从配置文件中读取采集的插件配置，执行每一个插件类对应的方法
    def execute(self):
        # 1.循环读取配置中的value值
        response = {}
        for k, v in self.plugins_dict.items():
            '''
            k : base, nic, cpu
            v : src.plugins.base.Base
            '''
            ### 2.分析采集类的路径
            '''
            module_path: 'src.plugins.base',
            class_name: 'Base'
            '''
            try:
                ret = {'status':None,'data':None}

                module_path, class_name= v.rsplit('.', 1)

                ### 3.导入模块的路径 import_module:导入字符串的模块路径
                module = importlib.import_module(module_path)
                # print(module)

                ### 4.从模块中导入类
                cls = getattr(module, class_name)

                ### 5.实例化类，执行类对应的具体采集方法
                res = cls().process(self.command_func, self.debug)
                ret['status'] = 10000
                ret['data'] = res
            except Exception as e:
                ret['status'] = 10001
                ret['data'] = f'错误信息：{traceback.format_exc()}'
            response[k] = ret

        return response


    def command_func(self, cmd):
        if self.settings == 'agent':
            import subprocess
            res = subprocess.getoutput(cmd)
            return res

        elif self.settings == 'ssh':
            import paramiko
            # 创建SSH对象
            ssh = paramiko.SSHClient()
            # 允许连接不在know_hosts文件中的主机
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # 连接服务器
            ssh.connect(hostname='192.168.79.131', port=22, username='root', password='root')

            # 执行命令
            stdin, stdout, stderr = ssh.exec_command(cmd)
            # 获取命令结果
            result = stdout.read()

            # 关闭连接
            ssh.close()

            return result