#Look for #IMPLEMENT tags in this file. These tags indicate what has
#to be implemented.

from collections import deque

'''
This file will contain different constraint propagators to be used within
bt_search.

propagator == a function with the following template
    propagator(csp, newly_instantiated_variable=None)
        ==> returns (True/False, [(Variable, Value), (Variable, Value) ...])

    csp is a CSP object---the propagator can use this to get access to the
    variables and constraints of the problem. The assigned variables can be
    accessed via methods, the values assigned can also be accessed.

    newly_instaniated_variable is an optional argument.
    if newly_instantiated_variable is not None:
        then newly_instantiated_variable is the most
        recently assigned variable of the search.
    else:
        propagator is called before any assignments are made
        in which case it must decide what processing to do
        prior to any variables being assigned. SEE BELOW

    The propagator returns True/False and a list of (Variable, Value) pairs.

    Returns False if a deadend has been detected by the propagator.
        in this case bt_search will backtrack
    Returns True if we can continue.

    The list of variable values pairs are all of the values
    the propagator pruned (using the variable's prune_value method).
    bt_search NEEDS to know this in order to correctly restore these
    values when it undoes a variable assignment.

    NOTE propagator SHOULD NOT prune a value that has already been
    pruned! Nor should it prune a value twice

    PROPAGATOR called with newly_instantiated_variable = None
        PROCESSING REQUIRED:
            for plain backtracking (where we only check fully instantiated
            constraints) we do nothing...return (true, [])

            for forward checking (where we only check constraints with one
            remaining variable) we look for unary constraints of the csp
            (constraints whose scope contains only one variable) and we
            forward_check these constraints.

            for gac we establish initial GAC by initializing the GAC queue with
            all constaints of the csp

    PROPAGATOR called with newly_instantiated_variable = a variable V
        PROCESSING REQUIRED:
            for plain backtracking we check all constraints with V (see csp
            method get_cons_with_var) that are fully assigned.

            for forward checking we forward check all constraints with V that
            have one unassigned variable left

            for gac we initialize the GAC queue with all constraints containing
            V.
'''

def prop_BT(csp, newVar=None):
    '''Do plain backtracking propagation. That is, do no
    propagation at all. Just check fully instantiated constraints'''

    if not newVar:
        return True, []
    for c in csp.get_cons_with_var(newVar):
        if c.get_n_unasgn() == 0:
            vals = []
            vars = c.get_scope()
            for var in vars:
                vals.append(var.get_assigned_value())
            if not c.check(vals):
                return False, []
    return True, []

        
def prop_FC(csp, newVar=None):
    '''Do forward checking.  That is, check constraints with only one
    uninstantiated variable, and prune appropriately.  (i.e., do not prune a
    value that has already been pruned; do not prune the same value twice.)
    Return if a deadend has been detected, and return the variable/value pairs
    that have been pruned.  See beginning of this file for complete description
    of what propagator functions should take as input and return.

    Input: csp, (optional) newVar.
        csp is a CSP object---the propagator uses this to
        access the variables and constraints.

        newVar is an optional argument.
        if newVar is not None:
            then newVar is the most recently assigned variable of the search.
            run FC on all constraints that contain newVar.
        else:
            propagator is called before any assignments are made in which case
            it must decide what processing to do prior to any variable
            assignment.

    Returns: (boolean,list) tuple, where list is a list of tuples:
             (True/False, [(Variable, Value), (Variable, Value), ... ])

        boolean is False if a deadend has been detected, and True otherwise.

        list is a set of variable/value pairs that are all of the values the
        propagator pruned.
    '''
      
    FC_pruned_list = []    
      
    constraints = csp.get_all_cons() if not newVar else csp.get_cons_with_var(newVar)
    for C in constraints:  
        # we check only constraints that have one unassigned variable left            
        if C.get_n_unasgn() == 1:
            unasgnVar = C.get_unasgn_vars()[0]
            for d in unasgnVar.cur_domain():
                # making unasgnVar = d together with previous assignments to 
                # variables in scope C and check if it satisfies the constraint
                vals = [var.get_assigned_value() if var.is_assigned() else d for var in C.get_scope()]
                if not C.check(vals):
                    if (unasgnVar, d) not in FC_pruned_list:
                        FC_pruned_list.append((unasgnVar, d))
                        unasgnVar.prune_value(d)
                    if unasgnVar.cur_domain() == []:
                        return False, FC_pruned_list  # DWO occured
    return True, FC_pruned_list

        

def prop_GAC(csp, newVar=None):
    '''Do GAC propagation, as described in lecture. See beginning of this file
    for complete description of what propagator functions should take as input
    and return.

    Input: csp, (optional) newVar.
        csp is a CSP object---the propagator uses this to access the variables
        and constraints.

        newVar is an optional argument.
        if newVar is not None:
            do GAC enforce with constraints containing newVar on the GAC queue.
        else:
            Do initial GAC enforce, processing all constraints.

    Returns: (boolean,list) tuple, where list is a list of tuples:
             (True/False, [(Variable, Value), (Variable, Value), ... ])

    boolean is False if a deadend has been detected, and True otherwise.

    list is a set of variable/value pairs that are all of the values the
    propagator pruned.
    '''

    GAC_pruned_list = []
    
    constraints = csp.get_all_cons() if not newVar else csp.get_cons_with_var(newVar)
    GAC_queue = deque(constraints)
    
    while GAC_queue:
        C = GAC_queue.pop()
        for v in C.get_scope():
            for d in v.cur_domain():
                # Find an assignment A for all other variables in scope(C) such 
                # that C (A U V=d). If A is not found.
                if not C.has_support(v, d):
                    if (v, d) not in GAC_pruned_list:
                        GAC_pruned_list.append((v, d))
                        v.prune_value(d)
                        if v.cur_domain() == []:
                            GAC_queue.clear()
                            return False, GAC_pruned_list # DWO occured
                        else:
                            # push all constraints C" such that V is in scope(C�)
                            # and C" is not in GAC_queue                           
                            for c in csp.get_cons_with_var(v):
                                if c not in GAC_queue:
                                    GAC_queue.append(c)
    return True, GAC_pruned_list


