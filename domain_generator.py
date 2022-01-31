import numpy as np 
import random as rn
import os 
import sys
import graspable_checker_tree as gct
import graspable_checker_all as gca
import candidate_make as cmake
class workspace:
    def __init__(self,rows,cols):
       
        self.obstacles = []

    
    def rev_manual_index_loop(self,mylist):
        a = []
        reverse_index = len(mylist) - 1
        for index in range(len(mylist)):
            a.append(mylist[reverse_index - index])
        return a

    def make_str_pick_obstacles(self): 
        sequence_of_obstacles = gct.graspable_checker()
        out_str = ""
        sequence_of_obstacles = sequence_of_obstacles[:-1]
        for idx, element in enumerate(sequence_of_obstacles):
            out_str+="(pick_obstacle" + str(idx) + ")\n" 
        return out_str

    def make_str_pick(self):
        sequence_of_obstacles = gct.graspable_checker()
        out_str = ""
        sequence_of_obstacles = sequence_of_obstacles[:-2]
        for idx, element in enumerate(sequence_of_obstacles):
            out_str+="(pick" + str(idx) + ")\n" 
        return out_str

    def make_str_param_obstruct(self):
        sequence_of_obstacles = gct.graspable_checker()
        out_str = ""
        sequence_of_obstacles = sequence_of_obstacles[:-1]
        for idx, element in enumerate(sequence_of_obstacles):
            out_str+="(obstruct" + str(idx) + " " + "?x" + " " + "?y" + " " + "-" +" " + "objects" + ")\n"   
        return out_str
    
    def make_str_pick_up_action(self):
        sequence_of_obstacles = gct.graspable_checker() 
        out_str = "(:action pick_up \n   :parameters(?x - objects ) \n   :precondition (and (clear ?x) (on-table ?x) (emptyhand) (canGrasp ?x)" 
        sequence_of_obstacles = sequence_of_obstacles[:-1]
        for idx, element in enumerate(sequence_of_obstacles):
            out_str += "(not (obstruct" + str(idx) + " " + "?x" + " " + "?x" + " " + "))"   
        out_str += ")\n"
        out_str += "   " + ":effect (and (holding ?x) (not (clear ?x)) (not (on-table ?x)) (not (emptyhand))))\n"
        return out_str

    def make_str_pick_up_obstruct2_action(self):
        sequence_of_obstacles = gct.graspable_checker() 
        out_str="(:action pick_up_obstruct \n   :parameters(?x - objects ) \n   :precondition (and (clear ?x) (on-table ?x) (emptyhand)" + " "
        sequence_of_obstacles = sequence_of_obstacles[:-1]
        for idx, element in enumerate(sequence_of_obstacles):
            out_str+=" (obstruct" + str(idx) + " " + "?x" + " " + "?x" + " " + ")"   
        out_str += ")\n"
        out_str += "   " + ":effect (and (holding ?x) (not (clear ?x)) (not (on-table ?x))" 
        for idx, element in enumerate(sequence_of_obstacles):
            out_str+=" (pick_obstacle" + str(idx) + " " + ")"
        out_str += "(not (emptyhand))))\n"  
        return out_str

    def make_str_pick_up_obstruct_action(self):
        sequence_of_obstacles = gct.graspable_checker() 
        out_str = " "
        sequence_of_obstacles = sequence_of_obstacles[:-1]
        seq = 0
        #fis = 1
        seq2 = len(sequence_of_obstacles)-1 
        sequence_of_obstacles = len(sequence_of_obstacles)
        #print(seq)
        #sequence_of_obstacles = [sequence_of_obstacles[-1], sequence_of_obstacles[0]]
        #sequence_of_obstacles = list(reversed(sequence_of_obstacles))
        #print(sequence_of_obstacles)
        for idx in range(sequence_of_obstacles):
            #print(idx)
            out_str+="(:action pick_up_obstruct \n   :parameters(?x - objects ) \n   :precondition (and (clear ?x) (on-table ?x) (emptyhand)" + " " 
            out_str+=" (obstruct" + str(idx) + " " + "?x" + " " + "?x" + " " + ")" 
            if idx == seq:
                out_str+=" "
            #elif idx == seq2:
                #out_str+=" "
            else:
                idx = idx - 1
                out_str+=" (pick" + str(idx) + ")"
                #print(idx)
                idx = idx + 1
            out_str+= ")\n"
            out_str+= "   " + ":effect (and (holding ?x) (not (clear ?x)) (not (on-table ?x))" 
            #print(idx)
            if idx == seq:
                out_str+= " (pick_obstacle" + str(idx) + " " + ")"
            else:
                #idx = idx + 1
                out_str+=" (pick_obstacle" + str(idx) + " " + ")"
            out_str+= "(not (emptyhand))))\n"  
        return out_str


    def make_str_pick_up_target_action(self):
        out_str = "(:action pick_up_target \n   :parameters(?x - objects ) \n   :precondition (and (clear ?x) (on-table ?x) (emptyhand) (collision_free) (not(canGrasp ?x)))" + "\n"
        out_str+= "   " + ":effect (and (holding ?x) (not (clear ?x)) (not (on-table ?x)) (not (emptyhand))))\n" 
        return out_str

    def make_str_stack_action(self):
        out_str = "(:action stack \n   :parameters(?x ?y - objects ) \n   :precondition (and (clear ?x) (holding ?x))" + "\n"
        out_str+= "   " + ":effect (and (on ?x ?y) (clear ?x) (not (clear ?y)) (emptyhand) (not (holding ?x)) ))\n" 
        return out_str


    def make_str_stack_obstruct_action(self):
        sequence_of_obstacles = gct.graspable_checker() 
        out_str = " "
        sequence_of_obstacles = sequence_of_obstacles[:-1]
        seq = len(sequence_of_obstacles)-1
        for idx, element in enumerate(sequence_of_obstacles):
            out_str+="(:action stack_obstruct \n   :parameters(?x ?y - objects ) \n   :precondition (and (clear ?y) (holding ?x) " 
            out_str+=" (pick_obstacle" + str(idx) + " " + ")"   
            out_str+= ")\n"
            out_str+= "   " + ":effect (and (on ?x ?y) (clear ?x) (not (clear ?y)) (emptyhand) (not (holding ?x)) "
        #for idx, element in enumerate(sequence_of_obstacles):
            if idx == seq:
                out_str += "(collision_free)"
            else: 
                out_str+=" (pick" + str(idx) + " " + ")"
            out_str+= "))\n"  
        return out_str
    
    def make_str_put_down_action(self):
        out_str = "(:action put_down \n   :parameters(?x - objects  ?s  - empty_slots ) \n   :precondition (and (holding ?x) (clean ?s)) " + "\n"
        out_str+= "   " + ":effect (and (clear ?x) (not (clean ?s)) (at ?x ?s) (emptyhand)  (on-table ?x) (not (holding ?x))   ))\n" 
        return out_str
    
    def make_str_put_down_obstruct_action(self):
        sequence_of_obstacles = gct.graspable_checker()
        out_str = " "
        sequence_of_obstacles = sequence_of_obstacles[:-1]
        seq = len(sequence_of_obstacles)-1
        seq = 2
        seq2 = len(sequence_of_obstacles)-1 
        for idx, element in enumerate(sequence_of_obstacles):
            out_str+="(:action put_down_obstruct \n   :parameters(?x - objects  ?s  - empty_slots ) \n   :precondition (and (holding ?x) (clean ?s) " 
            out_str+=" (pick_obstacle" + str(idx) + " " + ")"
            out_str+= ")\n"
            out_str+= "   " + ":effect (and (clear ?x) (not (clean ?s)) (at ?x ?s) (emptyhand)  (on-table ?x) (not (holding ?x))" 
            if idx == seq:
                out_str += "(collision_free)"
            #elif idx == seq2:
                #out_str+=" "
            else:
                out_str+=" (pick" + str(idx) + " " + ")"
            out_str+= "))\n"
        return out_str

    def make_str_unstack_action(self):
        out_str = "(:action unstack \n   :parameters(?x ?y - objects ) \n   :precondition (and (on ?x ?y) (clear ?x) (emptyhand)) " + "\n"
        out_str += "   " + ":effect (and (holding ?x) (clear ?y) (not (on ?x ?y)) (not (clear ?x)) (not (emptyhand))  ))\n" 
        return out_str

    def make_str_unstack_obstruct_action(self):
        sequence_of_obstacles = gct.graspable_checker() 
        out_str = " " 
        sequence_of_obstacles = sequence_of_obstacles[:-1]
        seq = 0
        seq2 = len(sequence_of_obstacles)-1
        #sequence_of_obstacles = list(reversed(sequence_of_obstacles))
        for idx, element in enumerate(sequence_of_obstacles):
            out_str+="(:action unstack_obstruct \n   :parameters(?x ?y - objects ) \n   :precondition (and (on ?x ?y) (clear ?x) (emptyhand) "
            out_str+=" (obstruct" + str(idx) + " " + "?x" + " " + "?x" + ")"  
            if idx == seq:
                out_str+=" "
            else:
                idx = idx - 1
                out_str+=" (pick" + str(idx) + ")" 
            out_str += ")\n"
            out_str += "   " + ":effect (and (holding ?x) (clear ?y) (not (on ?x ?y)) (not (clear ?x)) (not (emptyhand)) "
        #for idx, element in enumerate(sequence_of_obstacles):
            out_str+=" (pick_obstacle" + str(idx) + " " + ")"
            out_str+= "))\n"  
        return out_str
    
    def make_str_complete(self):
        out_str = "(define (domain test)\n"
        out_str += "(:requirements :strips :typing :fluents :disjunctive-preconditions :negative-preconditions )\n"
        out_str += "(:types \n objects \n empty_slots \n)\n"  
        out_str += "(:predicates \n"
        out_str += "(holding ?x - objects) \n(emptyhand) \n(on ?x ?y - objects) \n(clear ?x - objects) \n(on-table ?x - objects) \n(at ?x - objects ?s - empty_slots) \n(clean ?s - empty_slots)\n"
        out_str += "" + self.make_str_param_obstruct() + "\n"
        out_str += "(canGrasp ?x - objects)\n(collision_free)\n"
        out_str += "" + self.make_str_pick_obstacles() + "\n"
        out_str += "" +  self.make_str_pick() + "\n"
        out_str += ")" + "\n"
        out_str += "" + self.make_str_pick_up_action() + "\n" 
        out_str += "" + self.make_str_pick_up_obstruct_action() + "\n" 
        #out_str += "" + self.make_str_pick_up_obstruct2_action() + "\n" 
        out_str += "" + self.make_str_pick_up_target_action() + "\n" 
        out_str += "" + self.make_str_put_down_obstruct_action() + "\n" 
        out_str += "" + self.make_str_put_down_action() + "\n" 
        out_str += "" + self.make_str_stack_action() + "\n"
        out_str += "" + self.make_str_stack_obstruct_action() + "\n" 
        out_str += "" + self.make_str_unstack_action() + "\n"
        out_str += "" + self.make_str_unstack_obstruct_action() + "\n"
        out_str += ")"
        return out_str

def modify_pddl_random(map,pddl_file):
    #map.clear()
   # map.set_obstacles(n_obj)
   # print(map.make_str_objects_param()) 
   # print(map.make_str_slots_param())
    pddl_content = map.make_str_complete()
    #print(pddl_content)

    save_path = '/home/umka/catkin_ws/src/try/common/PDDL/'
    pddl_file2 = os.path.join(save_path, pddl_file)

    f = open(pddl_file2, "w")
    f.write(pddl_content)
    f.close()

    return map
    
def run_terminal(cmd):
    return os.system(cmd)

class parameter_set:
    def __init__(self,file=""):
        self.repeat_n = -1
        #self.objects_number = -1
        #self.slots_number = -1
        self.pddl_file = ""
        self.run_cmd = ""
        if(file!=""):
            with open(file) as f:
                lines = f.read().splitlines()
            for line in lines:
                temp = line.split(":")
                if(temp[0] == "repeat_n"):
                    self.repeat_n = int(temp[1])
                elif(temp[0] == "pddl_file"):
                    self.pddl_file = temp[1]
                elif(temp[0] == "run_cmd"):
                    self.run_cmd = temp[1]
                else:
                    print("unknown parameter name")


param_file_name = "domain.csv"
#print("Read Parameters from File: " + param_file_name)
param_set = parameter_set(param_file_name)

grid_N = gca.graspable_checker()
grid_S = cmake.graspable_checker()
#print("Generating workspace with "+ str(grid_N) + str(grid_S))
print("Processing...Please wait a few second")
map = workspace(grid_N,grid_S)

log_list = []
number_of_objects = gca.graspable_checker()
n_repeat = param_set.repeat_n
slots_number = cmake.graspable_checker()
#the loop
#for obj in range(number_of_objects):
    #for slot in range(slots_number):
for repeat in range(n_repeat):
    modified_map = modify_pddl_random(map,param_set.pddl_file)
        
print("Finished")
sys.exit()
