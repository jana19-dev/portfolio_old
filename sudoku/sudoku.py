'''
Construct and return Sudoku CSP model.
'''

from .cspbase import *
from .propagators import *
import itertools
import random
import copy

def sudoku_csp_model(initial_sudoku_board):
    '''Return a CSP object representing a Sudoku CSP problem along with an
    array of variables for the problem. 
    
    That is return: sudoku_csp, variable_array

    where sudoku_csp is a csp representing the initial board of sudoku and
    variable_array is a list of lists

    such that variable_array[i][j] is the Variable (object) that you built to
    represent the value to be placed in cell i,j of the sudoku board
    (indexed from (0,0) to (n-1,n-1))

    The input board is specified as a list of n lists. Each of the n lists
    represents a row of the board. If a 0 is in the list it represents an empty
    cell. Otherwise if a number between 1--n is in the list then this
    represents a pre-set board position.

    E.g., the board
    initial_sudoku_board = [[0,8,0,0,0,0,3,0,0],
                            [0,0,0,2,0,7,0,0,9],
                            [9,0,0,0,0,0,0,7,5],
                            [0,7,0,5,0,2,0,0,0],
                            [2,4,0,0,0,9,0,6,0],
                            [0,5,0,7,0,4,0,0,0],
                            [4,0,0,0,0,0,0,9,8],
                            [0,0,0,1,0,5,0,0,4],
                            [0,1,0,0,0,0,6,0,0]]

    This routine returns a model which consists of a variable for each cell of
    the board, with domain equal to [1,...,n] if the board has a 0 at that
    position, and domain equal [i] if the board has a fixed number i at that
    cell.

    This ontains BINARY CONSTRAINTS OF NOT-EQUAL between all relevant
    variables (e.g., all pairs of variables in the same row, etc.).

    '''

    # construct the domains for all variables
    domains = construct_domain(initial_sudoku_board)
   
    # construct all the variables with their domain values
    variable_array = construct_variables(domains)

    board_size = len(variable_array)
    
    cons = []   # constraints

    # construct the not-equal constraints between all pairs of variables in the same row
    for row in range(board_size):
        for left_col in range(board_size):
            
            right_col = left_col + 1
            while right_col != board_size:

                left_var = variable_array[row][left_col]
                right_var = variable_array[row][right_col]
    
                con = Constraint("C(V{}{}!=V{}{})".format(row,left_col, row,right_col), [left_var, right_var])
                
                # check for binary not-equal constraints in row
                domains = [left_var.cur_domain(), right_var.cur_domain()]
                sat_tuples = [t for t in itertools.product(*domains) if t[0] != t[1]]                
                con.add_satisfying_tuples(sat_tuples)
                cons.append(con)
                
                right_col += 1

    # construct the not-equal constraints between all pairs of variables in the same col
    for top_row in range(board_size):
        for col in range(board_size):
            
            bottom_row = top_row + 1
            while bottom_row != board_size:
                
                top_var = variable_array[top_row][col]
                bottom_var = variable_array[bottom_row][col]
    
                con = Constraint("C(V{}{}!=V{}{})".format(top_row,col,bottom_row,col), [top_var, bottom_var])
                
                # check for binary not-equal constraints in col
                domains = [top_var.cur_domain(), bottom_var.cur_domain()]
                sat_tuples = [t for t in itertools.product(*domains) if t[0] != t[1]]
                con.add_satisfying_tuples(sat_tuples)
                cons.append(con)
                
                bottom_row += 1

    # construct the not-equal constraints between all variables in the same 3x3 box 
    for x,y in [(1,1), (1,4), (1,7), (4,1), (4,4), (4,7), (7,1), (7,4), (7,7)]:
        vars = [variable_array[x-1][y-1], variable_array[x-1][y], variable_array[x-1][y+1],
                variable_array[x][y-1], variable_array[x][y],variable_array[x][y+1],
                variable_array[x+1][y-1], variable_array[x+1][y], variable_array[x+1][y+1]]

        for top_var,bottom_var in itertools.combinations(vars, 2):

            con = Constraint("C({}{}".format(top_var,bottom_var), [top_var, bottom_var])

            # check for binary not-equal constraints in col
            domains = [top_var.cur_domain(), bottom_var.cur_domain()]
            sat_tuples = [t for t in itertools.product(*domains) if t[0] != t[1]]
            con.add_satisfying_tuples(sat_tuples)
            cons.append(con)

    # construct a single list with all variables in variable_array as input to CSP __init__
    vars = list(itertools.chain(*variable_array))

    # create the CSP object
    futoshiki_csp = CSP("Model_1 {}x{}-Board".format(board_size,board_size), vars)

    # add all the constraints into CSP
    for c in cons:
        futoshiki_csp.add_constraint(c)

    return futoshiki_csp, variable_array

    

# .........Helper Functions.......... #

def construct_domain(initial_suduko_board):
    '''Construct the domains for all variables in initial_suduko_board
       and return the 2D domain list.
    '''    
    domains = []
    n = len(initial_suduko_board)
    for row in initial_suduko_board:
        row_dom = []
        for col in row:
            if col == 0: # domain equal to [1,...,n]
                row_dom.append([i+1 for i in range(n)])
            elif col in range(n+1): # domain equal [i] if the board has a fixed number 
                row_dom.append([col])
        domains.append(row_dom)

    return domains


def construct_variables(domains):
    '''Construct all the variables with their respective domain values and
       return the 2D variable list.
    '''    
    variable_array = []
    i, j = 0, 0 # to create the variables with appropriate names
    for row in domains:
        row_vars = []
        for dom in row:
            row_vars.append(Variable('V{}{}'.format(i,j), dom))
            j += 1
        variable_array.append(row_vars)
        i += 1
        j = 0

    return variable_array



# .........Verifying Final Solutions.......... #

def print_sudo_soln(var_array):
    result = []
    for row in var_array:
        result.append([var.get_assigned_value() for var in row])
    return result


def solved(csp):
    for c in csp.get_all_cons():
        if len(c.get_unasgn_vars()) != 0:
            print("unsassigned variables left {}".format(c.get_unasgn_vars()))
            return False
        vals = [v.get_assigned_value() for v in c.get_scope()]
        if not c.check(vals):
            print("constraint {} not satisfied".format(c))
            for v in c.get_scope():
                print("{} = {}".format(v, v.get_assigned_value()))
            return False
    return True
    

# .........Generating Sudoku Puzzles.......... #
    
def create_random_final_board():
    '''http://stackoverflow.com/questions/18908287/sudoku-generator'''

    while True:
        # init array
        puzzle = [[0 for j in range(9)] for i in range(9)]  
        # assign random value for each cell while satisfying sudoku rules
        for row in range(9):
            for col in range(9):
                thisRow=puzzle[row]
                thisCol=[puzzle[h][col] for h in range(9)]          
                subCol, subRow = col // 3, row // 3
                subMat = []
                for subR in range (3):
                    for subC in range (3):
                        subMat.append(puzzle[subRow*3 + subR][subCol*3 + subC])

                choosing_list = {1,2,3,4,5,6,7,8,9} - set(thisRow + thisCol + subMat)
                if not choosing_list:	break
                puzzle[row][col] = random.sample(choosing_list, 1)[0]

            if not choosing_list:    break

        if choosing_list:    return puzzle 

    


def create_initial_board(puzzle, level=0):
    ''' 0: Very Easy, 1: Easy, 2: Medium, 3: Hard, 4: Evil, 5: Impossible. 
        According to the level of difficulty, make a certain number of holes in the puzzle.
    ''' 
    puzzle = copy.deepcopy(puzzle)
    to_remove = 30 # Very Easy mode
    if level == 1:
        to_remove = 35 # Easy mode
    elif level == 2:
        to_remove = 40 # Medium mode  
    elif level == 3:
        to_remove = 45 # Hard mode    
    elif level == 4:
        to_remove = 50 # Evil mode    
    elif level == 5:
        to_remove = 55 # Impossible mode   	    
    
    cells_to_remove = random.sample(range(81),  to_remove)
    for num in cells_to_remove:
        row = num // 9
        col = num - (row * 10)
        puzzle[row][col] = 0

    return puzzle




def get_solution(puzzle):
    csp,var_array = sudoku_csp_model(puzzle)
    solver = BT(csp)
    solver.bt_search(prop_GAC)
    return print_sudo_soln(var_array)
  

def check_solution(puzzle):
    return puzzle == get_solution(puzzle)



