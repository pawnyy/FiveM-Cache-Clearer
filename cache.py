import shutil
import os
import getpass
user = getpass.getuser()
location = rf"C:\Users\{user}\AppData\Local\FiveM\FiveM.app\cache"
dir = "browser"
path = os.path.join(location, dir)
shutil.rmtree(path, ignore_errors = True)

dir = "db"
path = os.path.join(location, dir)
shutil.rmtree(path, ignore_errors = True)

dir = "priv"
path = os.path.join(location, dir)
shutil.rmtree(path, ignore_errors = True)

dir = "servers"
path = os.path.join(location, dir)
shutil.rmtree(path, ignore_errors = True)

dir = "subprocess"
path = os.path.join(location, dir)
shutil.rmtree(path, ignore_errors = True)

dir = "unconfirmed"
path = os.path.join(location, dir)
shutil.rmtree(path, ignore_errors = True)

file = "crashometry"
path = os.path.join(location, file)
try: 
    os.remove(path) 
    print("% s removed successfully" % path) 
except OSError as error: 
    print(error) 
    print("File path can not be removed") 

file = "launcher_skip_mtl2"
path = os.path.join(location, file)
try: 
    os.remove(path) 
    print("% s removed successfully" % path) 
except OSError as error: 
    print(error) 
    print("File path can not be removed") 

