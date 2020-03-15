
import os
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
USER = 'root'

MODE = 'agent'
DEBUG = True

PLUGINS_DICT = {
    'basic':'src.plugins.basic.Basic',
    'cpu':'src.plugins.cpu.Cpu',
    'disk':'src.plugins.disk.Disk',
    'nic':'src.plugins.nic.Nic',
    'memory': 'src.plugins.memory.Memory',
}

API_URL = 'http://127.0.0.1:8080/api/'
