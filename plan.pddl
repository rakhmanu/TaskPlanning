
ff: parsing domain file
domain 'TEST' defined
 ... done.
ff: parsing problem file
problem 'TEST_P' defined
 ... done.


no metric specified. plan length assumed.
setting gtt = 1.0 to simulate STRIPS planning.


checking for cyclic := effects --- OK.display info is 1

ff: search configuration is EHC, if that fails then  best-first on 1*g(s) + 5*h(s) where
    metric is  plan length

Real initial cost 8.000000, with 8 actions


Cueing down from goal distance:   8.00 into depth [1]
                                  6.00             [1]
                                  5.00             [1]
                                  4.00             [1][2]
                                  2.00             [1]
                                  1.00             [1]
                                  0.00             

ff: found legal plan (steps: 7) as follows
   0: (PICK_UP_OBSTRUCT OBSTACLE3)
   1: (PUT_DOWN_OBSTRUCT OBSTACLE3 SLOT0)
   2: (PICK_UP_OBSTRUCT OBSTACLE5)
   3: (PUT_DOWN_OBSTRUCT OBSTACLE5 SLOT1)
   4: (PICK_UP_OBSTRUCT OBSTACLE0)
   5: (PUT_DOWN_OBSTRUCT OBSTACLE0 SLOT2)
   6: (PICK_UP_TARGET TARGET)


Total cost of plan: 7.000000 

time spent:    0.00 seconds instantiating 418 easy, 0 hard action templates
               0.00 seconds reachability analysis, yielding 101 facts and 390 actions
               0.00 seconds creating final representation with 101 relevant facts, 0 relevant fluents
               0.00 seconds computing LNF
               0.00 seconds building connectivity graph
               0.00 seconds searching, evaluating 35 states, to a max depth of 2
               0.00 seconds total time

