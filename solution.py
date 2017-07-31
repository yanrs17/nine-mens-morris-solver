# import os for time functions
import os
from search import * #for search engines
from state import * #for snowball specific classes and problems
from test_problems import PROBLEMS #20 test problems

#snowball HEURISTICS
def heur_simple(state):
    '''trivial admissible snowball heuristic'''
    '''INPUT: a snowball state'''
    '''OUTPUT: a numeric value that serves as an estimate of the distance of the state (# of moves required to get) to the goal.'''   
    return len(state.snowballs)

def heur_zero(state):
    return 0

def heur_manhattan_distance(state):
#IMPLEMENT
    '''admissible snowball puzzle heuristic: manhattan distance'''
    '''INPUT: a snowball state'''
    '''OUTPUT: a numeric value that serves as an estimate of the distance of the state to the goal.'''      
    return sum(list(map(lambda coord:
                abs(state.destination[0]-coord[0]) +
                abs(state.destination[1]-coord[1]),
                state.snowballs)))

def heur_alternate(state):
#IMPLEMENT
    '''a better heuristic'''
    '''INPUT: a snowball state'''
    '''OUTPUT: a numeric value that serves as an estimate of the distance of the state to the goal.'''        
    #heur_manhattan_distance has flaws.   
    #Write a heuristic function that improves upon heur_manhattan_distance to estimate distance between the current state and the goal.
    #Your function should return a numeric value for the estimate of the distance to the goal.

    # To make it shorter
    obs = state.obstacles

    result = (abs(state.robot[0] - state.destination[0]) + abs(state.robot[1] - state.destination[1]))

    for ball in state.snowballs:
        x = ball[0]
        y = ball[1]

        # If the position of the ball is not the destination
        if ball != state.destination:

            # if state.snowballs[ball] in [3, 4, 5]:
            #     return float("inf")

            # If the ball is in the dead corner, i.e.
            #  # or #  or #s or s#
            # #s    s#     #    #
            # then means there is no solution
            if (x+1, y) in obs and (x,y+1) in obs:
                return float("inf")
            if (x+1, y) in obs and (x,y-1) in obs:
                return float("inf")
            if (x-1, y) in obs and (x,y+1) in obs:
                return float("inf")
            if (x-1, y) in obs and (x,y-1) in obs:
                return float("inf")

            if x != 0 and y != 0 and x != state.width - 1 and y != state.height - 1:

                if (x-1, y) in obs:
                    isBlocked1 = False
                    for i in range(y+1, state.height):
                        if (x, i) in obs:
                            isBlocked1 = True
                            break
                        if (x-1, i) not in obs:
                            break
                    if isBlocked1:
                        isBlocked2 = True
                        for j in range(y):
                            if (x, j) in obs:
                                isBlocked2 = True
                                break
                            if (x-1, i) not in obs:
                                break
                        if isBlocked1 and isBlocked2:
                            return float("inf")

                if (x+1, y) in obs:
                    isBlocked1 = False
                    for i in range(y+1, state.height):
                        if (x, i) in obs:
                            isBlocked1 = True
                            break
                        if (x+1, i) not in obs:
                            break
                    if isBlocked1:
                        isBlocked2 = True
                        for j in range(y):
                            if (x, j) in obs:
                                isBlocked2 = True
                                break
                            if (x+1, i) not in obs:
                                break
                        if isBlocked1 and isBlocked2:
                            return float("inf")

                if (x, y-1) in obs:
                    isBlocked1 = False
                    for i in range(x+1, state.width):
                        if (i,y) in obs:
                            isBlocked1 = True
                            break
                        if (i, y-1) not in obs:
                            break
                    if isBlocked1:
                        isBlocked2 = True
                        for j in range(x):
                            if (j, y) in obs:
                                isBlocked2 = True
                                break
                            if (j, y-1) not in obs:
                                break
                        if isBlocked1 and isBlocked2:
                            return float("inf")

                if (x, y+1) in obs:
                    isBlocked1 = False
                    for i in range(x+1, state.width):
                        if (i,y) in obs:
                            isBlocked1 = True
                            break
                        if (i, y+1) not in obs:
                            break
                    if isBlocked1:
                        isBlocked2 = True
                        for j in range(x):
                            if (j, y) in obs:
                                isBlocked2 = True
                                break
                            if (j, y+1) not in obs:
                                break
                        if isBlocked1 and isBlocked2:
                            return float("inf")

                # Same as above, but one obstacle is replaced by a stack of snowballs.
                # There are in total 4 (Up, Down, Left, Right) * 2 (Left, Right)
                # possibilities.
                if state.snowballs[ball] in [4, 5]:
                    if (x-1, y) in obs:
                        if (x-1, y-1) in obs and (x, y-1) in state.snowballs:
                            return float("inf")
                        if (x-1, y+1) in obs and (x, y+1) in state.snowballs:
                            return float("inf")

                    if (x+1, y) in obs:
                        if (x+1, y-1) in obs and (x, y-1) in state.snowballs:
                            return float("inf")
                        if (x+1, y+1) in obs and (x, y+1) in state.snowballs:
                            return float("inf")

                    if (x, y-1) in obs:
                        if (x-1, y-1) in obs and (x-1, y) in state.snowballs:
                            return float("inf")
                        if (x+1, y-1) in obs and (x+1, y) in state.snowballs:
                            return float("inf")

                    if (x, y+1) in obs:
                        if (x-1, y+1) in obs and (x-1, y) in state.snowballs:
                            return float("inf")
                        if (x+1, y+1) in obs and (x+1, y) in state.snowballs:
                            return float("inf")

        if x == 0 and state.destination[0] != 0:
            return float("inf")
        if y == 0 and state.destination[1] != 0:
            return float("inf")
        if x == state.width - 1 and state.destination[0] != state.width - 1:
            return float("inf")
        if y == state.height - 1 and state.destination[1] != state.height - 1:
            return float("inf")

        # if state.snowballs[ball] == 0: # Big
        #     result += (abs(state.destination[0]-x) +
        #         abs(state.destination[1]-y)) / 3
        # elif state.snowballs[ball] == 1: # Mid
        #     result += (abs(state.destination[0]-x) +
        #         abs(state.destination[1]-y)) / 2
        # else:
        result += abs(state.destination[0]-x) + abs(state.destination[1]-y)
        # result += (abs(state.robot[0]-x) + abs(state.robot[1]-y)) / 1.3

    return result

def fval_function(sN, weight):
#IMPLEMENT
    """
    Provide a custom formula for f-value computation for Anytime Weighted A star.
    Returns the fval of the state contained in the sNode.

    @param sNode sN: A search node (containing a SnowballState)
    @param float weight: Weight given by Anytime Weighted A star
    @rtype: float
    """
  
    #Many searches will explore nodes (or states) that are ordered by their f-value.
    #For UCS, the fvalue is the same as the gval of the state. For best-first search, the fvalue is the hval of the state.
    #You can use this function to create an alternate f-value for states; this must be a function of the state and the weight.
    #The function must return a numeric f-value.
    #The value will determine your state's position on the Frontier list during a 'custom' search.
    #You must initialize your search engine object as a 'custom' search engine if you supply a custom fval function.
    return sN.gval + weight * sN.hval

def anytime_gbfs(initial_state, heur_fn, timebound = 10):
#IMPLEMENT
    '''Provides an implementation of anytime greedy best-first search, as described in the HW1 handout'''
    '''INPUT: a snowball state that represents the start state and a timebound (number of seconds)'''
    '''OUTPUT: A goal state (if a goal is found), else False''' 
    # Initialize
    t = os.times()[0]
    cost = float("inf")

    # Use search engine
    se = SearchEngine("best_first", "full")
    se.init_search(initial_state, snowman_goal_state, heur_fn)
    local_best = se.search(timebound)
    global_best = local_best

    # Optimize
    while (os.times()[0] - t < timebound):
        # Search with cost bound
        local_best = se.search(timebound, (float("inf"), float("inf"), global_best.gval + heur_fn(global_best)))

        # If a better state is found, update it
        if local_best != False and local_best.gval < cost:
            cost = local_best.gval
            global_best = local_best
        else:
            # If not found: Just return it
            return global_best
    return global_best

def anytime_weighted_astar(initial_state, heur_fn, weight=1., timebound = 10):
#IMPLEMENT
    '''Provides an implementation of anytime weighted a-star, as described in the HW1 handout'''
    '''INPUT: a snowball state that represents the start state and a timebound (number of seconds)'''
    '''OUTPUT: A goal state (if a goal is found), else False''' 
    # Initialize
    t = os.times()[0]
    cost = float("inf")
    wrapped_fval_function = (lambda sN: fval_function(sN, weight))

    # Use search engine
    se = SearchEngine("custom", "full")
    se.init_search(initial_state, snowman_goal_state, heur_fn, wrapped_fval_function)
    local_best = se.search(timebound)
    global_best = local_best

    # Optimize
    while (os.times()[0] - t < timebound):
        # Search with cost bound
        local_best = se.search(timebound, (float("inf"), float("inf"), global_best.gval + heur_fn(global_best)))

        # If a better state is found, update it
        if local_best != False and local_best.gval < cost:
            cost = local_best.gval
            global_best = local_best
        else:
            # If not found: Just return it
            return global_best
    return global_best

if __name__ == "__main__":
  #TEST CODE
  solved = 0; unsolved = []; counter = 0; percent = 0; timebound = 2; #2 second time limit for each problem
  print("*************************************")  
  print("Running A-star")     

  for i in range(0, 10): #note that there are 20 problems in the set that has been provided.  We just run through 10 here for illustration.

    print("*************************************")  
    print("PROBLEM {}".format(i))
    
    s0 = PROBLEMS[i] #Problems will get harder as i gets bigger

    se = SearchEngine('astar', 'full')
    se.init_search(s0, goal_fn=snowman_goal_state, heur_fn=heur_alternate)
    final = se.search(timebound)

    if final:
      final.print_path()
      solved += 1
    else:
      unsolved.append(i)    
    counter += 1

  if counter > 0:  
    percent = (solved/counter)*100

  print("*************************************")  
  print("{} of {} problems ({} %) solved in less than {} seconds.".format(solved, counter, percent, timebound))  
  print("Problems that remain unsolved in the set are Problems: {}".format(unsolved))      
  print("*************************************") 

  solved = 0; unsolved = []; counter = 0; percent = 0; timebound = 8; #8 second time limit 
  print("Running Anytime Weighted A-star")   

  for i in range(0, 10):
    print("*************************************")  
    print("PROBLEM {}".format(i))

    s0 = PROBLEMS[i] #Problems get harder as i gets bigger
    weight = 10 
    final = anytime_weighted_astar(s0, heur_fn=heur_alternate, weight=weight, timebound=timebound)

    if final:
      final.print_path()   
      solved += 1 
    else:
      unsolved.append(i)
    counter += 1      

  if counter > 0:  
    percent = (solved/counter)*100   
      
  print("*************************************")  
  print("{} of {} problems ({} %) solved in less than {} seconds.".format(solved, counter, percent, timebound))  
  print("Problems that remain unsolved in the set are Problems: {}".format(unsolved))      
  print("*************************************")