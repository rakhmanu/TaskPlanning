(define (problem test_p)
 (:domain test)
  (:objects obstacle0 obstacle1 obstacle2 obstacle3 obstacle4 obstacle5 target - objects
 
   slot0 slot1 slot2 slot3 - empty_slots)
 
 (:init
   (on-table obstacle0)(on-table obstacle1)(on-table obstacle2)(on-table obstacle3)(on-table obstacle4)(on-table obstacle5)(on-table target)
 
(obstruct target obstacle3)(obstruct2 target obstacle5)(obstruct3 target obstacle0) (obstruct4 target obstacle1) (obstruct5 target obstacle2)
(obstruct6 target obstacle4)
 
(canGrasp obstacle0)(canGrasp obstacle1)(canGrasp obstacle2)(canGrasp obstacle3)(canGrasp obstacle4)(canGrasp obstacle5)
 
(clear obstacle0)(clear obstacle1)(clear obstacle2)(clear obstacle3)(clear obstacle4)(clear obstacle5)(clear target)
 
(clean slot0)(clean slot1)(clean slot2)(clean slot3) 
 
 
(emptyhand)
 )
 (:goal (and (holding target) ))
)