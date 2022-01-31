(define (domain test)
(:requirements :strips :typing :fluents :disjunctive-preconditions :negative-preconditions )
(:types 
 objects 
 empty_slots 
)
(:predicates 
(holding ?x - objects) 
(emptyhand) 
(on ?x ?y - objects) 
(clear ?x - objects) 
(on-table ?x - objects) 
(at ?x - objects ?s - empty_slots) 
(clean ?s - empty_slots)
(obstruct0 ?x ?y - objects)
(obstruct1 ?x ?y - objects)
(obstruct2 ?x ?y - objects)

(canGrasp ?x - objects)
(collision_free)
(pick_obstacle0)
(pick_obstacle1)
(pick_obstacle2)
(stackable ?x - objects)
(unstackable ?x - objects)
(pick0)
(pick1)

)
(:action pick_up 
   :parameters(?x - objects ) 
   :precondition (and (clear ?x) (on-table ?x) (emptyhand) (canGrasp ?x)(not (obstruct0 ?x ?x ))(not (obstruct1 ?x ?x ))(not (obstruct2 ?x ?x )))
   :effect (and (holding ?x) (not (clear ?x)) (not (on-table ?x)) (not (emptyhand))))

 (:action pick_up_obstruct 
   :parameters(?x - objects ) 
   :precondition (and (clear ?x) (on-table ?x) (emptyhand)  (obstruct0 ?x ?x ) )
   :effect (and (holding ?x) (not (clear ?x)) (not (on-table ?x)) (pick_obstacle0 )(not (emptyhand))))
(:action pick_up_obstruct 
   :parameters(?x - objects ) 
   :precondition (and (clear ?x) (on-table ?x) (emptyhand)  (obstruct1 ?x ?x ) (pick0))
   :effect (and (holding ?x) (not (clear ?x)) (not (on-table ?x)) (pick_obstacle1 )(not (emptyhand))))
(:action pick_up_obstruct 
   :parameters(?x - objects ) 
   :precondition (and (clear ?x) (on-table ?x) (emptyhand)  (obstruct2 ?x ?x ) (pick1))
   :effect (and (holding ?x) (not (clear ?x)) (not (on-table ?x)) (pick_obstacle2 )(not (emptyhand))))

(:action pick_up_target 
   :parameters(?x - objects ) 
   :precondition (and (clear ?x) (on-table ?x) (emptyhand) (collision_free) (not(canGrasp ?x)))
   :effect (and (holding ?x) (not (clear ?x)) (not (on-table ?x)) (not (emptyhand))))

 (:action put_down_obstruct 
   :parameters(?x - objects  ?s  - empty_slots ) 
   :precondition (and (holding ?x) (clean ?s)  (pick_obstacle0 ))
   :effect (and (clear ?x) (not (clean ?s)) (at ?x ?s) (emptyhand)  (on-table ?x) (not (holding ?x)) (pick0 )))
(:action put_down_obstruct 
   :parameters(?x - objects  ?s  - empty_slots ) 
   :precondition (and (holding ?x) (clean ?s)  (pick_obstacle1 ))
   :effect (and (clear ?x) (not (clean ?s)) (at ?x ?s) (emptyhand)  (on-table ?x) (not (holding ?x)) (pick1 )))
(:action put_down_obstruct 
   :parameters(?x - objects  ?s  - empty_slots ) 
   :precondition (and (holding ?x) (clean ?s)  (pick_obstacle2 ))
   :effect (and (clear ?x) (not (clean ?s)) (at ?x ?s) (emptyhand)  (on-table ?x) (not (holding ?x))(collision_free)))

(:action put_down 
   :parameters(?x - objects  ?s  - empty_slots ) 
   :precondition (and (holding ?x) (clean ?s)) 
   :effect (and (clear ?x) (not (clean ?s)) (at ?x ?s) (emptyhand)  (on-table ?x) (not (holding ?x))   ))

(:action stack 
   :parameters(?x ?y - objects ) 
   :precondition (and (clear ?x) (holding ?x))
   :effect (and (on ?x ?y) (clear ?x) (not (clear ?y)) (emptyhand) (not (holding ?x)) ))

 (:action stack_obstruct 
   :parameters(?x ?y - objects ) 
   :precondition (and (clear ?y) (holding ?x) (stackable ?x) (pick_obstacle0 ))
   :effect (and (on ?x ?y) (clear ?x) (not (clear ?y)) (emptyhand) (not (holding ?x))  (pick0 )))
(:action stack_obstruct 
   :parameters(?x ?y - objects ) 
   :precondition (and (clear ?y) (holding ?x) (stackable ?x) (pick_obstacle1 ))
   :effect (and (on ?x ?y) (clear ?x) (not (clear ?y)) (emptyhand) (not (holding ?x))  (pick1 )))
(:action stack_obstruct 
   :parameters(?x ?y - objects ) 
   :precondition (and (clear ?y) (holding ?x) (stackable ?x) (pick_obstacle2 ))
   :effect (and (on ?x ?y) (clear ?x) (not (clear ?y)) (emptyhand) (not (holding ?x)) (collision_free)))

(:action unstack 
   :parameters(?x ?y - objects ) 
   :precondition (and (on ?x ?y) (clear ?x) (emptyhand)) 
   :effect (and (holding ?x) (clear ?y) (not (on ?x ?y)) (not (clear ?x)) (not (emptyhand))  ))

 (:action unstack_obstruct 
   :parameters(?x ?y - objects ) 
   :precondition (and (on ?x ?y) (clear ?x) (emptyhand)  (obstruct0 ?x ?x) )
   :effect (and (holding ?x) (clear ?y) (not (on ?x ?y)) (not (clear ?x)) (not (emptyhand))  (pick_obstacle0 )))
(:action unstack_obstruct 
   :parameters(?x ?y - objects ) 
   :precondition (and (on ?x ?y) (clear ?x) (emptyhand)  (obstruct1 ?x ?x) (pick0))
   :effect (and (holding ?x) (clear ?y) (not (on ?x ?y)) (not (clear ?x)) (not (emptyhand))  (pick_obstacle0 )))
(:action unstack_obstruct 
   :parameters(?x ?y - objects ) 
   :precondition (and (on ?x ?y) (clear ?x) (emptyhand)  (obstruct2 ?x ?x) (pick1))
   :effect (and (holding ?x) (clear ?y) (not (on ?x ?y)) (not (clear ?x)) (not (emptyhand))  (pick_obstacle1 )))

)
