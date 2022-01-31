import os
import roslaunch
import time 
from subprocess import call 

os.system('python /home/umka/Desktop/ToH_project/JinHwi_ToH_modified/source/problem_generator.py')
time.sleep(10)
os.system('python /home/umka/Desktop/ToH_project/JinHwi_ToH_modified/source/domain_generator.py')
time.sleep(10)
uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
roslaunch.configure_logging(uuid)
launch = roslaunch.parent.ROSLaunchParent(uuid, ['/home/umka/catkin_ws/src/try/launch/ToH_manipulation.launch'])
launch.start()
time.sleep(10)
with open ('/home/umka/catkin_ws/src/try/scripts/ToH_manipulation.bash') as file:
    script = file.read() 
bash = call(script, shell=True)


