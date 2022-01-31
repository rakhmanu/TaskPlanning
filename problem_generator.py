import numpy as np 
import random as rn
import os 
import sys
import graspable_checker_tree as gct
import graspable_checker_all as gca
import candidate_make as cmake
class workspace:
    def __init__(self,rows=0,cols=0):
        #self.grid_act = np.array(False)
        #self.grid_act.resize(rows,cols)
        #self.neighbor_name = ["lower","higher","before","after"]
        self.goal = -1
        self.obstacles = []

    def clear(self):
        for i in range(len(self.grid_act)):
            for j in range(len(self.grid_act[0])):
                self.grid_act[i][j] = False

    def index2xy(self,ind):
        return ind//len(self.grid_act[0]), ind%len(self.grid_act[0])

    def xy2index(self,i,j):
        return i*len(self.grid_act[0]) + j
    
    def make_str_objects_param(self):
        #cell_number = len(self.grid_act) 
        objects_number = gca.graspable_checker()
        out_str="(:objects "
        for n in range(objects_number):
            out_str+="obstacle" + str(n) + " "
        out_str += "target"
        out_str += " - objects"
        return out_str

    def make_str_slots_param(self):
        slots_number = cmake.graspable_checker()  
        out_str=" "
        for n in range(len(slots_number)):
            out_str+="slot" + str(n) + " "
        out_str += "- empty_slots)"
        return out_str

   # def make_str_param_amount(self):
    #    cell_number = len(self.grid_act) 
    #    out_str=" "
    #    for cell in range(cell_number):
    #        out_str+="(=(amount obstacle" + str(cell) + " " + "slot0" + ")" + " " + "0)" +"\n"
    #        out_str+="(=(amount obstacle" + str(cell) + " " + "slot1" + ")" + " " + "0)" + "\n"
    #        out_str+="(=(amount obstacle" + str(cell) + " " + "slot2" + ")" + " " +  "0)" + "\n"
    #        out_str+="(=(amount obstacle" + str(cell) + " " + "slot3" + ")" + " " + "0)"  + "\n"
    #       out_str+="(=(amount obstacle" + str(cell) + " " + "slot4" + ")" + " " + "0)"  + "\n"
    #        out_str+="(=(amount obstacle" + str(cell) + " " + "slot5" + ")" + " " + "0)"  + "\n"
    #    out_str+="(=(amount target"  + " " + "slot0" + ")" + " " + "0)" +"\n"
    #    out_str+="(=(amount target"  + " " + "slot1" + ")" + " " + "0)" +"\n"
    #    out_str+="(=(amount target"  + " " + "slot2" + ")" + " " + "0)" +"\n"
    #    out_str+="(=(amount target"  + " " + "slot3" + ")" + " " + "0)" +"\n"
    #    out_str+="(=(amount target"  + " " + "slot4" + ")" + " " + "0)" +"\n"
    #    out_str+="(=(amount target"  + " " + "slot5" + ")" + " " + "0)" +"\n"
    #    return out_str

    #def make_str_param_numberOf(self):
    #    cell_number = len(self.grid_act) 
    #    out_str=" "
    #    for cell in range(cell_number):
    #        out_str+="(=(numberOf obstacle0"  + " " + "obstacle" + str(cell) + ")" +" "+ "0)" + "\n"
    #       out_str+="(=(numberOf obstacle1" + " " + "obstacle" + str(cell)  +  ")" +" "+ "0)" + "\n"
    #        out_str+="(=(numberOf obstacle2" + " " + "obstacle" + str(cell)  +  ")" + " " + "0)" + "\n"
    #        out_str+="(=(numberOf obstacle3" + " " + "obstacle" + str(cell)  + ")" + " " + "0)" + "\n" 
    #    return out_str

    def make_str_param_on_table(self):
        objects_number = gca.graspable_checker() 
        out_str=" "
        for cell in range(objects_number):
            out_str+="(on-table obstacle" + str(cell) + ")"
        out_str+="(on-table target" + ")"
        return out_str

    def make_str_param_canGrasp(self):
        objects_number = gca.graspable_checker() 
        out_str=""
        for cell in range(objects_number):
            out_str+="(canGrasp obstacle" + str(cell)  + ")"  
        return out_str

    def make_str_param_clear(self):
        objects_number = gca.graspable_checker() 
        out_str=""
        for cell in range(objects_number):
            out_str+="(clear obstacle" + str(cell)  + ")"
        out_str+="(clear target" + ")"   
        return out_str

    def make_str_param_obstruct(self):
        sequence_of_obstacles = gct.graspable_checker()
        out_str = ""
        sequence_of_obstacles = sequence_of_obstacles[:-1]
        for idx, element in enumerate(sequence_of_obstacles):
            out_str+="(obstruct" + str(idx) + " " + "target" + " " + "obstacle" + str(element) + ")" 

    
        if gct.graspable_checker is None:
            out_str="(obstruct target" + " " + "target" + ")"  
        return out_str

    def make_str_param_clean_slots(self):
        slots_number = cmake.graspable_checker()
        out_str=""
        for cell in range(len(slots_number)):
            out_str += "(clean" + " " + "slot" + str(cell) + ")"  
        return out_str


    def make_str_param_clean(self):
        out_str = " "
        cell_number = len(self.grid_act)
        for cell in range(cell_number):
            rand_cell = rn.randint(0,cell)
            out_str +=  "(" + " " + "obstacle" + str(rand_cell) + ")"  
        return out_str
    

    def mark_occupancy(self,ind,b):
        i,j = self.index2xy(ind)
        self.grid_act[i][j] = b

    def is_occupied(self,ind):
        i,j = self.index2xy(ind)
        return self.grid_act[i][j]

    def set_obstacles(self, n_of_obs):
        cell_number = len(self.grid_act) 
        obstacles_ind = []
        while(len(obstacles_ind) != n_of_obs):
            obs_candidate = rn.randint(0,cell_number-1)
            if(self.is_occupied(obs_candidate) != True):
                #add to obstables list
                obstacles_ind.append(obs_candidate)
                #mark as occupied
                self.mark_occupancy(obs_candidate,True)

        self.obstacles = sorted(obstacles_ind)
    
    def make_str_complete(self):
        out_str = "(define (problem test_p)\n (:domain test)\n"
        out_str += "  "  +  self.make_str_objects_param() + "\n"
        out_str += " " + "\n" 
        out_str += "  "  +  self.make_str_slots_param() + "\n"
        out_str += " " + "\n" 
        out_str += " (:init\n"
        #out_str += self.make_str_param_amount() + "\n"
        #out_str += " " + "\n" 
        #out_str += self.make_str_param_numberOf() + "\n"  
        #out_str += " " + "\n" 
        #out_str += " " + "(=(maxItems) 2)" + "\n" 
        out_str += "  " + self.make_str_param_on_table() + "\n"
        out_str += " " + "\n" 
        out_str += self.make_str_param_obstruct() + "\n" 
        out_str += " " + "\n" 
        out_str += self.make_str_param_canGrasp() + "\n" 
        out_str += " " + "\n" 
        out_str += self.make_str_param_clear() + "\n"
        out_str += " " + "\n"  
        out_str += self.make_str_param_clean_slots() + "\n" 
        out_str += " " + "\n" 
        #out_str += self.make_str_param_on() + "\n" 
        out_str += " " + "\n"  
        out_str += "(emptyhand)" + "\n"  
        out_str += " " + ")\n"
        out_str += " " + "(:goal (and (holding target" + ") ))\n"
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
                #elif(temp[0] == "objects_number"):
                    #self.objects_number = temp[1]
                #elif(temp[0] == "slots_number"):
                    #self.slots_number = temp[1]
                elif(temp[0] == "run_cmd"):
                    self.run_cmd = temp[1]
                else:
                    print("unknown parameter name")


param_file_name = "parameters.csv"
print("Read Parameters from File: " + param_file_name)
param_set = parameter_set(param_file_name)

grid_N = gca.graspable_checker()
grid_S = cmake.graspable_checker()
print("Generating workspace with "+ str(grid_N) + str(grid_S))
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
