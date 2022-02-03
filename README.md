# Task Planning for Robot Manipulation 
This is the code for task planning designed in PDDL 

You need to install ROS kinetic first http://wiki.ros.org/kinetic/Installation/Ubuntu

To run the planner do:
1. Install Fast Forward (FF) planner

>sudo apt-get install ros-kinetic-ffha

2. Install ROSPlan https://github.com/KCL-Planning/ROSPlan

If you want to run task planning, please run Task_planner.py

You can generate problem file by running problem_generator.py. The example of problem file is shown in generate_p.pddl.

You can generate domain file by running domain_generator.py. The instance of domain file is shown in generate_d.pddl.

The instance of obtained a task plan is depicted in plan.pddl 

