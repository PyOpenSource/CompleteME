# Todos
# - Non-physical answers are still options (would need error checking)
# - Put the given/find code in it's own function as it is problem independent
# - Include a standard set of units
# - Have a standard order for printing parameters?

import heat_transfer_util as htu
import numpy as np
import sympy
import random


def fouriers_law_prob_gen():
    qpp, k, t1, t2, l = sympy.symbols("qpp k T1 T2 L")
    param_set = [qpp, k, t1, t2, l]
    solve_for = random.choice(param_set)
    param_set.remove(solve_for)

    params = {}
    if qpp in param_set:
        params[qpp] = random.choice(heat_fluxes)
    if k in param_set:
        params[k] = random.choice(thermal_conductivity)
    if t1 in param_set:
        params[t1] = random.choice(temperatures)
    if t2 in param_set:
        params[t2] = random.choice(temperatures)
    if l in param_set:
        params[l] = random.choice(lengths)

    print("Given")
    for key, value in params.items():
        print("\t", key, ": ", value)
    print("Find", solve_for)
    guess = input()
    solution = htu.fouriers_law(params)
    if guess == solution:
        print("Correct")
    else:
        print("Incorrect, correct answer was %f" % solution)

# Set up standard parameter ranges

thermal_conductivity = np.arange(1, 5, 0.1)
temperatures = np.arange(800, 1700)
lengths = np.arange(0.05, 0.5, 0.001)
heat_fluxes = np.arange(-3000, 3000, 50)

fouriers_law_prob_gen()
